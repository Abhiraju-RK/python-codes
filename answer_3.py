# program for check eligible for job 1

def job_eligible(age,experience):
    if age>=21:
        if age<=30 and experience>3:
            return("you are eligible for job")
        elif experience<3:
            return("3+ year experience required ")
    else:
        return("you not eligible")
print(job_eligible(22,4))
print(job_eligible(20,1))

#calculate total and average marks 2

class student():
    def __init__(self,*mark):
        self.mark=mark
        self.total=sum(mark)
        self.average=self.total/len(mark)

    def display_total(self):
        print("your total mark :",self.total)
    def display_average(self):
        print("your average mark :",self.average)

result=student(73,66,77)
result.display_total()
result.display_average()


#calculator using multiple inheritance 3

class simple_calculator():
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b

class scientific_cal():
    def cube(self,a):
        return a**3
    def square(self,a):
        return a**2
class calculator(simple_calculator,scientific_cal):
    pass

cal=calculator()
print("your output :",cal.cube(5))
print("your output :",cal.mul(2,5))

# bank pin change 4

class Bank_account():
    def __init__(self,holder_name,acc_num,pin_num,balance=0):
        self.holder_name=holder_name
        self.acc_num=acc_num
        self.pin_num=pin_num
        self.balance=balance
    
    def deposit(self,amount):
        self.balance+=amount
        print("your",amount,"deposit successfully")

    def check_bal(self,pin):
        if self.pin_num==pin:
            print("your current balance is :",self.balance)
        elif self.pin_num!=pin:
            print("your pin is not correct")
        else:
            print("unable to check balance")

    def withdraw(self,amount,pin):
        if self.pin_num==pin:
            if amount<=self.balance:
                self.balance-=amount
                print("you",amount,"is withdrawed successfuly")
            elif amount>self.balance:
                print("you have insufficent balance")
        else:
            print("your pin does not match")

    def change_pin(self,new_pin,old_pin):
        if self.pin_num==old_pin:
            self.pin_num=new_pin
            print("your PIN chnage succesfully")
        else:
            print("old PIN didnt match")

bal=Bank_account('Abhi',4654231335,1245)
bal.deposit(2500)
bal.check_bal(1245)
bal.withdraw(250,1245)
bal.change_pin(12345,1245)


# sorted array 5

def sorted_list(num1,num2):
    both_num=sorted(num1+num2)
    n=len(both_num)
    if n%2==1:
        return float(both_num [n // 2])
    else:
        return (both_num[n//2 - 1] + both_num[n//2])/2.0

print(sorted_list([1,3],[4,6]))
print(sorted_list([1,3],[4]))


















        
        

            






























    




























    

