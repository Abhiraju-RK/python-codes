# print pattern 1

for i in range(1,6):
    print((str(i)+' ')*i)

for i in range(1,6):
    for k in range(1,i+1):
        print(k,end=' ')
    print()

n=1
for i in range(1,6):
    for j in range(i):
        print(n,end=' ')
        n+=1
    print()


# without isupper() method 2

a="WELcomE TO the WORLD of PYTHON"
count=0
for value in a:
    if 'A'<=value<='Z':
        count+=1
print('counts :',count)

# adding in nested list  3

a=[10,20,[300,400,[5000,6000],500],30,40]
a[2][2].append(7000)
print(a)

# find the half of each element 4

s=[10,20,30,40,50]
half=[i//2 for i in s]
print(half)


# common value in list 5

list1=[1,2,4,6]
list2=[3,4,5,44]
common=[c for c in list1 if c in list2]
print(common)

# find longest word 6

words="she is reading a book"
long_word=words.split()
longer=max(long_word,key=len)
print(longer)

# changing order to negative to positive 7

num=[1,-1,-2,-3,4,5]
neg=[x for x in num if x<=0]
pos=[x for x in num if x>=0]
order=neg+pos
print(order)


# balance checking oops 8

class BankAccount:
    def __init__(self,account_number,holder_name,balance=0):
        self.account_number=account_number
        self.holder_name=holder_name
        self.balance=balance
                 
    def deposit(self,amount):
        self.balance+=amount
        print("RS :",amount,"deposit successfully")
    def withdraw(self,amount):
        if self.balance<amount:
            print("insufficent balance")
        else:
            self.balance-=amount
            print("RS :",amount,"withdraw successfully")
    def show_balance(self):
        print("Balance : RS :",self.balance)
acc=BankAccount("2944849307","abhi")
acc.deposit(30000)
acc.withdraw(2500)
acc.show_balance()


# find area and perimeter of rectangle 9

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2 *(self.length + self.width)
cal=Rectangle(4,5)
print("Area :",cal.area())
print("perimeter :",cal.perimeter())


# sum of target 10

num=[1,7,11,15]
target=9
for i in range(len(num)):
    for j in range(i+1, len(num)):
        if num[i] + num[j] == :
            print([i, j])
            break 











