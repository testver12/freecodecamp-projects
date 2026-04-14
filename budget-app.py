import math
class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []
        self.total = 0
        self.spend = 0
    def __str__(self):
        st = (f"{self.name:*^30}\n")
        for i in (self.ledger):
            st += f"{i['description']:<23.23}{i['amount']:>7.2f}\n"
        st += f"Total: {self.total:.2f}"
        return st


    def deposit(self,amount,description = ''):
        self.ledger.append({'amount': amount,'description': description})
        self.total += amount
    def withdraw(self,amount,description = ''):
        if amount <= self.total:
            self.ledger.append({'amount': -amount,'description': description})
            self.total -= amount
            self.spend += amount
            return True
        else:
            return False
    def get_balance(self):
        return(self.total)  
    def check_funds(self,amt):
        if amt <= self.total:
            return True
        else:
            return False
    def transfer(self,amt,destination):
        if self.check_funds(amt) == True:
            self.withdraw(amt,f'Transfer to {destination.name}')
            self.spend -= amt
            destination.deposit(amt,f'Transfer from {self.name}')
            return True
        else:
            return False
def create_spend_chart(cats):
    num = len(cats)
    total = 0
    centile = 11
    row = ""
    standard = []
    standardnum = 0
    for index,item in enumerate(cats):
        total += item.spend
        standard.append([item.spend,index,item.name])
    standardnum = standard
    row = f"Percentage spent by category\n"
    r = 10
    while r < 11:
        pc = r*10
        r -= 1
        row += f"{pc:>3}|"
        for j in range (num):
            if ((100.*standardnum[j][0]/total)//10)*10 >= pc:
                row += " o "
            else:
                row += "   "
        row += ' \n'
        if r < 0 : break
    row += '    '
    row += num * '---'
    row += f"-\n"
    cols = len(standardnum)
    maxlen = 0
    for nm in standardnum:
        if len(nm[2]) >= maxlen: maxlen = len(nm[2])
    titles = [["" for col in range(num)] for row in range(maxlen)]
    for col in range(num):
        for r in range(maxlen):
            titles[r][col]=standardnum[col][2][r:r+1]
            if len(titles[r][col]) == 0:
                titles[r][col] = ' '
    for n in range(maxlen):
        row += '    '
        for col in range(num):
           row += f" {titles[n][col]} "
        row +=  " \n"   
    return row[:-1]


food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
clothing = Category('Clothing')
food.transfer(250, clothing)
clothing.withdraw(100,'jacket')
auto = Category('Auto')
auto.deposit(750, 'qtrly deposit')
auto.withdraw(250, 'monthly payment')
auto.withdraw(25, 'fuel')
auto.withdraw(30, 'fuel')
business = Category('Business')
business.deposit(500, 'monthly deposit')
business.withdraw(250, 'retirement fund')
clothing.withdraw(25,'laundry')
food.withdraw(45.67,'milk, cereal, eggs, bacon')
entertainment = Category('Entertainment')
entertainment.deposit(200,'deposit')
entertainment.withdraw(1.00,'movies')
business.withdraw(200)
print(create_spend_chart([food,business,entertainment]))



