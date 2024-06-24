# Customer Banking
A customer banking system that allows users to calculate and track interest earned on savings and CD accounts. By running this application, users will be able to enter their savings and CD account information, see the interest earned, and view the updated balances after a specified number of months.

## Savings Account Function in savings_account.py
1. The Account class from the Account.py file is imported. **_(line 3)_**
2. In the create_savings_account function, an instance of the Account class is created and the balance and interest parameters are passed to the Account class. **_(line 27)_**
3. The interest earned is calculated and assigned to a variable. **_(line 31)_**
4. The savings account balance is updated by adding the interest earned to the balance and assigned to a variable. **_(line 35)_**
5. The updated balance is passed to the set balance method using the instance of the Account class. **_(line 39)_**
6. The interest earned is passed to the set balance method using the instance of the Account class. **_(line 43)_**
7. The updated balance and interest earned are returned by the function. **_(line 45)_**

## CD Account Function in cd_account.py
1. The Account class from the Account.py file is imported. **_(line 3)_**
2. In the create_cd_account function, an instance of the Account class is created and the balance and interest parameters are passed to the Account class. **_(line 25)_**
3. The interest earned is calculated and assigned to a variable. **_(line 28)_**
4. The CD account balance is updated by adding the interest earned to the balance and assigned to a variable. **_(line 32)_**
5. The updated balance is passed to the set balance method using the instance of the Account class. **_(line 36)_**
6. The interest earned is passed to the set balance method using the instance of the Account class. **_(line 40)_**
7. The updated balance and interest earned are returned by the function. **_(line 43)_**

## Main Function in customer_banking.py
1. The user is prompted to set the savings balance, interest rate, and months for the savings account. **_(line 14, 15, 16)_**
2. Code is written to print out the interest earned and updated savings account balance with interest earned for the given months. The values are formatted to two decimal places and thousandths. **_(line 19, 23, 25)_**
3. The user is prompted to set the savings balance, interest rate, and months for the CD account. **_(line 28,29,30)_**
4. Code is written to print out the interest earned and updated CD account balance with interest earned for the given months. The values are formatted to two decimal places and thousandths. **_(line 33, 37, 38)_**
5. The main function is called to run the program. **_(line 40, 41, 42)_**