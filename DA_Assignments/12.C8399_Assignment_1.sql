-- CREATING TABLE

CREATE TABLE C8399Transaction
(
Sender INT,
Receiver INT,
Amount INT,
TransDate DATE
);

--INSERTING VALUES

INSERT INTO C8399Transaction
	(Sender, 
	Receiver, 
	Amount, 
	TransDate)

SELECT 5, 2, 10, '2-12-20'
UNION
SELECT 1, 3, 15, '2-13-20'
UNION
SELECT 2, 1, 20, '2-13-20'
UNION
SELECT 2, 3, 25, '2-14-20'
UNION
SELECT 3, 1, 20, '2-15-20'
UNION
SELECT 3, 2, 15, '2-15-20'
UNION
SELECT 1, 4, 5, '2-16-20'

SELECT *
FROM C8399Transaction

SELECT sender, SUM(amount) debited
INTO debits
FROM C8399Transaction
GROUP BY Sender

SELECT receiver, SUM(amount) credited
INTO credits
FROM C8399Transaction
GROUP BY receiver

SELECT *
FROM credits

SELECT *
FROM debits

SELECT coalesce(sender, receiver) "user", 
coalesce(credited, 0) - coalesce(debited, 0) net_change 
FROM debits D
FULL JOIN credits C
ON C.receiver = D.sender
ORDER BY 2 DESC
