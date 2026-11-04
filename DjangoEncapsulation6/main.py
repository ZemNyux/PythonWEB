from finance.account import BankAccount

try:
  acc = BankAccount(
      owner='Олександр',
      account_number='UA1234567890123456',
      balance=1000.0,
      pin=1234,
  )

  print(acc.get_account_info())
  print('-' * 30)

  acc.deposit(500)
  print('Після поповнення:', acc.balance)

  acc.withdraw(200)
  print('Після зняття:', acc.balance)

except ValueError as e:
  print('Помилка:', e)