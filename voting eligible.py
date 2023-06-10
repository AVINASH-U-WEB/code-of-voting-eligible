cont="yes"
class voter:
    name=""
    yob=0
    def __init__(self,name,yob):
        self.name=name
        self.yob=yob
    def show(self):
        print("The voter name is ",self.name)
        print("The year of birth".self.yob)
from datetime import datetime
from time import strftime
try:
    while cont=="yes":
        month=["January", "February", " March" ,"April","May" ,"June" ,"July" ,"August ","September ","October ","November ","December"] 
        name=input("Enter the voter name  =")
        if name==" ":
            raise ValueError("Do not give space!")
        
        yob=int(input("Etner the year of birth ="))
        if yob=="":
            raise ValueError("Do not give space!")
        ag=strftime("%Y")
        age=int(ag)-yob
        print("The Voter age is",age)
        if age==18:
            m=input("Enter the month and day ( Do not give zero at first !)= ")
            print("Your  eligible for voting in at after month of ",month[int(m[0])-1])
        if age>18:
            print("You are eligible for voting")
        else:
            print("The Voter is not eligible of voting")
        print("Today date and time",datetime.now())
        cont=input("Enter the do you want  to continue [yes/no] =")
    m1=voter(name.yob)
    m1.show()
except:
    print("Something went wrong")

