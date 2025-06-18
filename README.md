# Banking System in Python

In this project proposed by [DIO](dio.me), I created a Banking System in Python.

The goal is to implement three essential operations: deposit, withdrawal and showing extract. The system is developed for a fictitious bank that seeks to monetize its operations. During the challenge, I applied my knowledge in Python programming and created a functional system that simulates banking operations.

## Challenge

We were hired by a large bank to develop its new system. This bank wants to monetize its operations and for this they chose the Python language. For the first version of the system, we must implement only 3 operations: deposit, withdrawal and showing extract.

## 1. Deposit Operation

It must be possible to deposit positive amounts to my bank account. The v1 of the project works with only 1 user, so we do not need to worry about identifying the branch and bank account number.

All deposits must be stored in a variable and displayed in the statement operation.

## 2. Withdrawal Operation

The system must allow 3 daily withdrawals with a maximum limit of $500.00 per withdrawal.

If the user does not have a balance in the account, the system must display a message stating that the withdrawal will not be possible due to insufficient funds.

All withdrawals must be stored in a variable and displayed in the showing extract operation.

## 3. Showing Extract Operation

This operation must list all deposits and withdrawals made in the account. At the end of the list, the current account balance must be displayed.

The amounts must be displayed using the format $xxx.xx, for example:

1500.45 = $1500.45

## Challenge 2 - Optimizing the Bank System with Python Functions

We need to modularize our code. We will create functions for new operations.

* Create User (bank customer)
* Create Checking Account (vinculating user and bank)

Changes are done on former operations as well.

## Withdrawal

Receives arguments per keyword only.

## Deposit

Receives positional arguments only.

## Showing Extract

Positional only and Keyword only.

## New Functions

We create new functions: create user and create checking account. It's possible to create more functions, like account listing.

### Create User

The program must store users in a list.

User:

* Name
* Birthday
* SSN (just one per user)
* Address (street, number - district - city, state)

### Create Checking Account

Store accounts in a list:

* Agency (always 0001)
* Account Number
* User (Name and SSN)
