menu = '''
[d] Deposit
[w] Withdraw
[e] Extract
[x] Exit
'''

balance = 0
LIMIT = 500
extract = []
number_withdrawls = 0
LIMIT_WITHDRAW = 3

# Deposit function to handle deposits
def depositing(deposit):
    global balance
    if deposit > 0:
        balance += deposit
        extract.append(f'Deposit: ${deposit:.2f}')
        print(f'Deposit: ${deposit:.2f}, completed successfully!')
        return balance
    else:
        print('Operation failed! The value entered is invalid.')

# Withdraw function to handle withdrawals
def withdraw(withdrawal):
    global balance, number_withdrawls, LIMIT_WITHDRAW, LIMIT
    if withdrawal > balance:
        print("Operation failed! Insufficient balance.")
    elif withdrawal > LIMIT:
        print(f'Operation failed! The limit for withdrawal is ${LIMIT:.2f}.')
    elif number_withdrawls >= LIMIT_WITHDRAW:
        print('Operation failed! Maximum withdraws exceeded.')
    else:
        balance -= withdrawal
        extract.append(f'Withdrawal: ${withdrawal:.2f}')
        number_withdrawls += 1
        print(f'Withdrawal: ${withdrawal:.2f}, completed successfully!')
    return balance

# Extract function to display the banking extract
def show_extract():
    if not extract:
        print('No transactions were made.')
    else:
        print('Extract:')
        for operation in extract:
            print(operation)
        print(f'Current Balance: ${balance:.2f}')

# Main loop of the banking system
while True:
    option = input(menu).strip().lower()

    if option == 'd':
        deposit = float(input('Inform the deposit amount: '))
        depositing(deposit)
    elif option == 'w':
        withdrawal = float(input('Inform the withdrawal amount: '))
        withdraw(withdrawal)
    elif option == 'e':
        show_extract()
    elif option == 'x':
        print('Exiting system...')
        break
    else:
        print('Invalid operation! Please select a valid option.')