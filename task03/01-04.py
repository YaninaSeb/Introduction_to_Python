# Создать класс “Человек”
# Атрибуты - Имя, фамилия, год рождения, номер паспорта, пол.
# Методы для ввода/вывода всех атрибутов по отдельности, метод вычисления возраста (на 2023 г), метод проверки на совершеннолетие/выход на пенсию(в зависимости от возраста).

class Person():
  def __init__(self, fN, sN, b, pN, s):
    self.firstName = fN
    self.secondName = sN
    self.yearOfBirth = b
    self.passNumber = pN
    self.sex = s

  def setFirstName(self, newFirstName):
    self.firstName = newFirstName
  def getFirstName(self):
    return self.firstName

  def setSecondName(self, newSecondName):
    self.secondName = newSecondName
  def getSecondName(self):
    return self.secondName

  def setYearOfBirth(self, newYearOfBirth):
    self.yearOfBirth = newYearOfBirth
  def getYearOfBirth(self):
    return self.yearOfBirth

  def setPassNumber(self, newPassNumber):
    self.passNumber = newPassNumber
  def getPassNumber(self):
    return self.passNumber

  def setSex(self, newSex):
    self.sex = newSex
  def getSex(self):
    return self.sex

  def getAge(self):
    currentYear = 2023
    return currentYear - self.getYearOfBirth()

  def isAdult(self):
    return True if self.getAge() >= 18 else False

  def isRetirement(self):
    if self.sex == 'Male':
      return True if self.getAge() >= 63 else False
    if self.sex == 'Female':
      return True if self.getAge() >= 58 else False

# Производные классы - служащий с почасовой оплатой, служащий в штате(на окладе).  
# Служащий с почасовой оплатой – атрибуты – почасовой тариф, количество отработанных часов
# Служащий в штате – атрибуты – оклад, размер премии, размер ставки
# Сделать методы для увеличения почасового тарифа/оклада/премии, для расчета зарплаты сотрудника.
# Если служащий пенсионер – почасовой тариф/оклад увеличивается на 5% автоматически

class hourlyWorker(Person):
  def __init__(self, fN, sN, b, pN, s, t, h):
    super().__init__(fN, sN, b, pN, s)
    self.tariff = t * 1.05 if self.isRetirement() else t
    self.hours = h

  def tariffIncrease(self, percent):
    self.tariff += (self.tariff * percent / 100)

  def getSalary(self):
    return self.tariff * self.hours


class regulaWorker(Person):
  def __init__(self, fN, sN, b, pN, s, fP, p, r):
    super().__init__(fN, sN, b, pN, s)
    self.fixedPayment = fP * 1.05 if self.isRetirement() else fP
    self.premium = p
    self.rate = r

  def fixedPaymentIncrease(self, percent):
    self.fixedPayment += (self.fixedPayment * percent / 100)

  def premiumIncrease(self, percent):
    self.premium += (self.premium * percent / 100)

  def getSalary(self):
    return self.fixedPayment * self.rate + ((self.fixedPayment * self.rate) * self.premium / 100)


# Сделать список сотрудников компании (максимум 5 объектов разных классов, например 1, 3, 5 – с почасовой, 2, 4 – на окладе). Написать функцию для расчета общей суммы выплат для этой компании учитывая ФСЗН на каждого сотрудника 35% (платит компания, в зп служащих не учитывается).

Elena = hourlyWorker('Elena', 'Ivanova', 1988, 165325723, 'Female', 10, 110)
Artem = regulaWorker('Artem', 'Tuzov', 1960, 987453012, 'Male', 1700, 15, 1.5)
Petr = hourlyWorker('Petr', 'Simonov', 1991, 123892345, 'Male', 8, 80)
Yana = regulaWorker('Yana', 'Petrova', 1994, 171537008, 'Female', 1500, 10, 1)
Anna = hourlyWorker('Anna', 'Kireeva', 1965, 343592305, 'Female', 15, 130)


def getPaymentAmount(tax, w1, w2, w3, w4, w5):
  amountOfSalaries = w1.getSalary() + w2.getSalary() + w3.getSalary() + w4.getSalary() + w5.getSalary()
  amountOfTaxes = amountOfSalaries * tax / 100
  paymentAmount = amountOfSalaries + amountOfTaxes
  
  print('The total amount paid by this company to these employees is', paymentAmount)
  

getPaymentAmount(35, Elena, Artem, Petr, Yana, Anna)
