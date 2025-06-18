# Option menu for the banking system
def menu():
    menu_text = '''
    [n] New Account
    [c] New Client
    [l] List Clients
    [d] Deposit
    [w] Withdraw
    [e] Extract
    [x] Exit
    '''
    return input(menu_text).strip().lower()

# Main loop of the banking system
def main():
    balance = 0
    LIMIT = 500
    extract = []
    number_withdrawls = 0
    LIMIT_WITHDRAW = 3
    AGENCY = '0001'
    users = []
    accounts = []
    while True:
        option = menu()
        if option == 'n':
            account_number = len(accounts) + 1
            account = new_account(AGENCY, account_number, users)
            if account:
                accounts.append(account)
        elif option == 'c':
            new_client(users)
        elif option == 'l':
            list_clients(users)
            list_accounts(accounts)
        elif option == 'd':
            deposit = float(input('Inform the deposit amount: '))
            balance, extract = depositing(balance, deposit, extract)
        elif option == 'w':
            withdrawal = float(input('Inform the withdrawal amount: '))
            balance, extract, number_withdrawls = withdraw(
                balance=balance,
                withdrawal=withdrawal,
                extract=extract,
                LIMIT=LIMIT,
                number_withdrawls=number_withdrawls,
                LIMIT_WITHDRAW=LIMIT_WITHDRAW
            )
        elif option == 'e':
            show_extract(balance, extract=extract)
        elif option == 'x':
            print('Exiting system...')
            break
        else:
            print('Invalid operation! Please select a valid option.')


# Deposit function to handle deposits
def depositing(balance, deposit, extract, /):
    if deposit > 0:
        balance += deposit
        extract.append(f'Deposit: ${deposit:.2f}')
        print(f'Deposit: ${deposit:.2f}, completed successfully!')
        return balance, extract
    else:
        print('Operation failed! The value entered is invalid.')

# Withdraw function to handle withdrawals
def withdraw(*, balance, withdrawal, extract, LIMIT, number_withdrawls, LIMIT_WITHDRAW):
    if withdrawal > balance:
        print("Operation failed! Insufficient balance.")
    elif withdrawal > LIMIT:
        print(f'Operation failed! The limit for withdrawal is ${LIMIT:.2f}.')
    elif number_withdrawls >= LIMIT_WITHDRAW:
        print('Operation failed! Maximum withdraws exceeded.')
    elif withdrawal > 0:
        balance -= withdrawal
        extract.append(f'Withdrawal: ${withdrawal:.2f}')
        number_withdrawls += 1
        print(f'Withdrawal: ${withdrawal:.2f}, completed successfully!')
    return balance, extract, number_withdrawls

# Extract function to display the banking extract
def show_extract(balance, /, *, extract):
    if not extract:
        print('No transactions were made.')
    else:
        print('Extract:')
        for operation in extract:
            print(operation)
        print(f'Current Balance: ${balance:.2f}')

# Function to register a new client
def new_client(users):
    ssn = input('Enter the SSN: ')
    user = filter_client(ssn, users)
    if user:
        print('Client already registered!')
        return
    else:
        name = input('Enter the name: \n')
        birth_date = input('Enter the birth date (dd/mm/yyyy): \n')
        address = input('Enter the address (street, number, district, city/state):\n')

        users.append({
            'name': name,
            'ssn': ssn,
            'birth_date': birth_date,
            'address': address
        })
        print(f'Client {name} registered successfully!')

# Function to create a new account
def new_account(agency, account_number, users):
    ssn = input('Enter the SSN of the client: \n')
    user = filter_client(ssn, users)
    if user:
        print(f'Account created successfully! \nUser: {user['name']}\n Account Number: {account_number}, \nAgency: {agency}')
        return {
            'agency': agency,
            'account_number': account_number,
            'user': user
        }
    else:
        print('Client not found! Please register the client first.')
        return None

# Function to filter a client by SSN
def filter_client(ssn, users):
    for user in users:
        if user['ssn'] == ssn:
            return user
    return None

# Function to list all clients
def list_clients(users):
    if not users:
        print('No clients registered.')
    else:
        print('Clients:')
        for user in users:
            print(f"SSN: {user['ssn']}, Name: {user['name']}, Birth Date: {user['birth_date']}, Address: {user['address']}")

# Function to list all accounts
def list_accounts(accounts):
    if not accounts:
        print('No accounts registered.')
    else:
        print('Accounts:')
        for account in accounts:
            user = account['user']
            print(f"Account Number: {account['account_number']}, Agency: {account['agency']}, User: {user['name']}, SSN: {user['ssn']}")




if __name__ == '__main__':
    main()