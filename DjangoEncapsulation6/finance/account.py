class BankAccount:
  def __init__(
      self, owner: str, account_number: str, balance: float = 0.0, pin: int = 0
  ):
    self.owner = owner
    self._account_number = account_number
    self.__balance = balance
    self.__pin = pin


  @property
  def balance(self) -> float:
    return self.__balance

  @balance.setter
  def balance(self, value: float):
    if value < 0:
      raise ValueError('Баланс не може бути відємним!')
    self.__balance = value

  @property
  def account_number(self) -> str:
    return self._account_number

  def deposit(self, amount: float) -> float:
    """Метод поповнення рахунку з валідацією."""
    if amount <= 0:
      raise ValueError('Сума поповнення повинна бути більшою за нуль!')
    self.__balance += amount
    return self.__balance

  def withdraw(self, amount: float) -> float:
    """Метод зняття коштів з перевіркою балансу."""
    if amount <= 0:
      raise ValueError('Сума для зняття має бути більшою за нуль!')
    if amount > self.__balance:
      raise ValueError('Недостатньо коштів на рахунку!')
    self.__balance -= amount
    return self.__balance

  def change_pin(self, old_pin: int, new_pin: int) -> bool:
    """Зміна пін-коду з перевіркою старого та валідацією нового."""
    if old_pin != self.__pin:
      raise ValueError('Невірний старий пін-код!')
    if not (1000 <= new_pin <= 9999):
      raise ValueError('Пін-код повинен складатися з 4 цифр!')
    self.__pin = new_pin
    return True

  def get_account_info(self) -> str:
    """Метод роздрукування стану/інформації."""
    masked_acc = (
        '*' * (len(self._account_number) - 4) + self._account_number[-4:]
    )
    return (
        f'Рахунок власника: {self.owner}\n'
        f'Номер рахунку: {masked_acc}\n'
        f'Поточний баланс: {self.__balance:.2f} грн'
    )