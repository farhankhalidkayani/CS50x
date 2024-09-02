import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

db.execute(
    "CREATE TABLE IF NOT EXISTS shares(user_id INTEGER NOT NULL, stock_name TEXT NOT NULL, no_shares INTEGER NOT NULL, FOREIGN KEY(user_id) REFERENCES users(id))"
)
db.execute(
    """
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        stock_name TEXT NOT NULL,
        no_shares INTEGER NOT NULL,
        price REAL NOT NULL,
        type TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
"""
)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    stocks = db.execute(
        "SELECT stock_name, no_shares FROM shares WHERE user_id = ?", session["user_id"]
    )
    rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    cash = rows[0]["cash"]

    total = 0
    for stock in stocks:
        stock_data = lookup(stock["stock_name"])
        stock_price = stock_data["price"]
        total += stock_price * stock["no_shares"]

    value = cash + total

    return render_template(
        "index.html", lookup=lookup, stocks=stocks, cash=cash, value=value, usd=usd
    )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        stock = request.form.get("symbol")
        if not stock:
            return apology("No stock symbol entered")
        no_shares = request.form.get("shares")
        try:
            no_shares = int(no_shares)
        except ValueError:
            return apology("Shares must be a positive integer")
        if not no_shares or no_shares <= 0:
            return apology("Invalid number of stocks entered")
        stock = lookup(stock)
        if not stock:
            return apology("No such stock")
        rows = db.execute("SELECT cash FROM users WHERE id= ?", session["user_id"])
        cash = rows[0]["cash"]
        stock_price = stock["price"] * no_shares
        if cash < stock_price:
            return apology("Not enough cash")
        db.execute(
            "CREATE TABLE IF NOT EXISTS shares(user_id INTEGER NOT NULL, stock_name TEXT NOT NULL, no_shares INTEGER NOT NULL, FOREIGN KEY(user_id) REFERENCES users(id))"
        )
        db.execute(
            "UPDATE users SET cash= ? WHERE id= ?",
            (cash - stock_price),
            session["user_id"],
        )
        db.execute(
            "INSERT INTO shares(user_id,stock_name,no_shares) VALUES(?, ?, ?)",
            session["user_id"],
            stock["symbol"],
            no_shares,
        )
        return redirect("/")
    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        stock_name = request.form.get("symbol")
        if not stock_name:
            return apology("No Stock symbol entered")
        stock = lookup(stock_name)
        if not stock:
            return apology("No such stock", 400)
        stock = usd(stock["price"])
        return render_template("quote_result.html", name=stock_name, stock=stock)
    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        if not username:
            return apology("No Username Entered")
        password = request.form.get("password")
        if not password:
            return apology("No password Entered")
        if password != request.form.get("confirmation"):
            return apology("Confirmed password not matching")
        check_username = db.execute(
            "SELECT username FROM users WHERE username= ? ", username
        )
        if check_username:
            return apology("Username Already Taken")
        id = db.execute(
            "INSERT INTO users(username,hash) VALUES(?, ?)",
            username,
            generate_password_hash(password),
        )
        session["user_id"] = id
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    stocks = db.execute("SELECT * FROM shares WHERE user_id = ?", session["user_id"])
    if request.method == "POST":
        if not stocks:
            return apology("No stocks owned")
        name = request.form.get("symbol")
        if not name:
            return apology("No such stock")
        shares = request.form.get("shares")
        try:
            shares = int(shares)
        except ValueError:
            return apology("Invalid number of shares")
        if not shares or shares < 0:
            return apology("Invalid number of shares")
        rows = db.execute(
            "SELECT no_shares FROM shares WHERE user_id = ? AND stock_name = ?",
            session["user_id"],
            name,
        )
        no_shares = rows[0]["no_shares"]
        if not no_shares or shares > no_shares:
            return apology("Invalid number of shares")
        price = lookup(name) * shares
        rows = db.execute(
            "SELECT cash FROM users WHERE id = ?",
            session["user_id"],
        )
        cash = rows[0]["cash"]
        db.execute(
            "UPDATED users SET cash = ? WHERE id = ? ", cash + price, session["user_id"]
        )
        return redirect("/")

    return render_template("sell.html", stocks=stocks)
