-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Checked the crime scene reports from 2023-07-28 and Found
 SELECT * FROM crime_scene_reports;
-- 295|2023|7|28|Humphrey Street|Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
-- Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.


SELECT * FROM interviews WHERE year=2023 AND day=28 AND month=07;
-- 161|Ruth|2023|7|28|Sometime within ten minutes of the theft, 10:25am
--  I saw the thief get into a car in the bakery parking lot and drive away.
--   If you have security footage from the bakery parking lot, 
--   you might want to look for cars that left the parking lot in that time frame.
-- 162|Eugene|2023|7|28|I don't know the thief's name,
--  but it was someone I recognized. Earlier this morning,
--   before I arrived at Emma's bakery,
--    I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.
-- 163|Raymond|2023|7|28|As the thief was leaving the bakery, 
-- they called someone who talked to them for less than a minute. 
-- In the call, I heard the thief say that they were planning to take the earliest 
-- flight out of Fiftyville tomorrow.2023-29-07 The thief then asked the person on the other end 
-- of the phone to purchase the flight ticket.
SELECT * FROM atm_transactions WHERE year=2023 AND day=28 AND month=07 and atm_location ='Leggett Street';
-- 246|28500762|2023|7|28|Leggett Street|withdraw|48
-- 264|28296815|2023|7|28|Leggett Street|withdraw|20
-- 266|76054385|2023|7|28|Leggett Street|withdraw|60
-- 267|49610011|2023|7|28|Leggett Street|withdraw|50
-- 269|16153065|2023|7|28|Leggett Street|withdraw|80
-- 288|25506511|2023|7|28|Leggett Street|withdraw|20
-- 313|81061156|2023|7|28|Leggett Street|withdraw|30
-- 336|26013199|2023|7|28|Leggett Street|withdraw|35
SELECT * FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year=2023 AND day=28 AND month=07 and atm_location ='Leggett Street' and transaction_type='withdraw'));
-- 395717|Kenny|(826) 555-1652|9878712108|30G67EN
-- 396669|Iman|(829) 555-5269|7049073643|L93JTIZ
-- 438727|Benista|(338) 555-6650|9586786673|8X428L0
-- 449774|Taylor|(286) 555-6063|1988161715|1106N58
-- 458378|Brooke|(122) 555-4581|4408372428|QX4YZN3
-- 467400|Luca|(389) 555-5198|8496433585|4328GD8
-- 514354|Diana|(770) 555-1861|3592750733|322W7JE
-- 686048|Bruce|(367) 555-5533|5773159633|94KL13X
SELECT * from phone_calls WHERE year=2023 and month=07 and day=28 and duration<60 and caller IN (SELECT phone_number FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year=2023 AND day=28 AND month=07 and atm_location ='Leggett Street' and transaction_type='withdraw')));
-- 233|(367) 555-5533|(375) 555-8161|2023|7|28|45
-- 255|(770) 555-1861|(725) 555-3243|2023|7|28|49
SELECT * from people WHERE phone_number IN (SELECT caller from phone_calls WHERE year=2023 and month=07 and day=28 and duration<60 and caller IN (SELECT phone_number FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year=2023 AND day=28 AND month=07 and atm_location ='Leggett Street' and transaction_type='withdraw'))));
-- 514354|Diana|(770) 555-1861|3592750733|322W7JE
-- 686048|Bruce|(367) 555-5533|5773159633|94KL13X
SELECT * from people WHERE phone_number IN (SELECT receiver from phone_calls WHERE year=2023 and month=07 and day=28 and duration<60 and caller IN (SELECT phone_number FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year=2023 AND day=28 AND month=07 and atm_location ='Leggett Street' and transaction_type='withdraw'))));
-- 847116|Philip|(725) 555-3243|3391710505|GW362R6
-- 864400|Robin|(375) 555-8161||4V16VO0
SELECT * FROM bakery_security_logs WHERE year=2023 and month=7 and day=28 and hour=10 and minute<25 and minute>15;
-- 261|2023|7|28|10|18|exit|94KL13X
-- 266|2023|7|28|10|23|exit|322W7JE
SELECT * FROM passengers WHERE passport_number=3592750733 OR passport_number=5773159633;
-- 18|3592750733|4C
-- 24|3592750733|2C
-- 36|5773159633|4A
-- 54|3592750733|6C
SELECT * FROM flights WHERE id IN (SELECT flight_id FROM passengers WHERE passport_number=3391710505);
-- 10|8|4|2023|7|30|13|55
