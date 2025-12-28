class Account:
  def __init__(self,balence,accno):
         self.balence=balence
         self.accno=accno
  def debit (self,amount):
             if self.balence>amount:
                 self.balence-=amount
                 print(f"{amount} is debited ,bal is{self.getbal()}")
             else:
                     print("in sufficient funds")
  def credit (self,amount): 
            self.balence+=amount
            print(f"{amount} iscredited ,bal is{self.getbal()}")
  def getbal(self):
            return self.balence
acc1=Account(1000,"acc12")
acc1.credit(500)
acc1.debit(1000)
        
class SavingsAccount(Account):
  def __init__(self,interest):
         self.interest=interest
         super()._init__(1000,"acc123")
  def interestrate(self):
      interest1=self.balence*(self.interest/100)
      self.balence+=interest1
      print(self.getbal())
acc1=Account(1000,"acc12")
acc1.credit(500)
acc1.debit(1000)
