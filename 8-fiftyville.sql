-- thief 
-- Bruce

-- city thief escaped to
-- New York City

-- accomplice
-- Robin

-- only person is Bruce, people id = 686048
SELECT *
FROM passengers

JOIN atm_transactions
JOIN bank_accounts ON bank_accounts.account_number = atm_transactions.account_number

JOIN people ON passengers.passport_number = people.passport_number
AND flight_id = 36
AND bank_accounts.person_id = people.id

JOIN phone_calls ON people.phone_number = phone_calls.caller 
AND phone_calls.duration < 60 
AND phone_calls.day > 27

JOIN bakery_security_logs
ON bakery_security_logs.day = 28
AND bakery_security_logs.hour = 10
AND bakery_security_logs.minute > 14
AND bakery_security_logs.minute < 26
AND bakery_security_logs.license_plate = people.license_plate

WHERE atm_transactions.atm_location = 'Leggett Street'
AND atm_transactions.day = 28
AND atm_transactions.month = 7
AND atm_transactions.transaction_type = 'withdraw'

;

SELECT *
FROM people
WHERE people.id = 686048
;

-- recievers of phonecalls (possible accomplises)


SELECT *
FROM people

JOIN phone_calls ON people.phone_number = phone_calls.receiver 
AND phone_calls.duration < 60 
AND phone_calls.day > 27
AND phone_calls.caller = '(367) 555-5533'

;


SELECT *
FROM flights
;

--
SELECT *
FROM passengers
JOIN people ON passengers.passport_number = people.passport_number
WHERE passengers.flight_id = 36
;

-- quickest flight on the 29th is id 36
SELECT *
FROM flights
WHERE flights.day = 29
ORDER BY hour
LIMIT 1
;

SELECT *
FROM bank_accounts
JOIN people ON people.id = bank_accounts.person_id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE atm_transactions.transaction_type = 'withdraw'
;

-- duck crime is id 295
SELECT description
FROM crime_scene_reports
WHERE crime_scene_reports.id = 295
;

-- interviews
SELECT *
FROM interviews
WHERE interviews.id = 163 
OR interviews.id = 162
OR interviews.id = 161
;

-- possible cars
SELECT * 
FROM bakery_security_logs
WHERE day = 28
AND hour = 10
AND minute > 14
AND minute < 26
;

-- people who withdrew from the atm on leggett street on the day of the theft
SELECT *
FROM atm_transactions
JOIN bank_accounts ON bank_accounts.account_number = atm_transactions.account_number
JOIN people ON bank_accounts.person_id = people.id
WHERE atm_location = 'Leggett Street'
AND day = 28
AND month = 7
AND transaction_type = 'withdraw'
;