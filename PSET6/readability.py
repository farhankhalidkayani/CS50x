from cs50 import get_string, get_int, get_float  # type: ignore


def calculation(l, s, w):
    L = (float(l) / float(w)) * 100
    S = (float(s) / float(w)) * 100
    si = 0.0588 * L - 0.296 * S - 15.8
    return round(si)


def result(i):

    if i > 16:
        print("Grade 16+")
    elif i < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {i}")


t = get_string("Text: ")

l = 0
w = 1
s = 0

for i in range(len(t)):
    if t[i].isalpha() != False:
        l += 1

    if t[i] == " ":
        w += 1
    if t[i] == "." or t[i] == "!" or t[i] == "?":
        s += 1
index = calculation(l, s, w)

result(index)
