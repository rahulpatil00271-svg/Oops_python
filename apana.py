

# Note : In Python Class is a blueprint(It contains Atrributees,Info )
# Note : Obj is created using Class

#### Class is a collection of Data and Methods ###
###____Methods are Function which belong to Class___###


#Ex.1
# class Student :
#     name="Raj"

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)

#--------------------------------------
#Ex.2
#--------------------------------------

# class Car:
#     color = "blue"

# c1 = Car()
# print(c1.color)


#-------------------------------------
#-------------------------------------
# __init__ Function


###########################
#Constructor (__init__)
###########################
#function is Executed when class is Initiated


# class Student :
    
#     #Parametriced Constructor
#     def __init__(self,name,marks): #self is argument
#                                  #Self used to acces variables which Belong to class
#         self.name = name
#         self.marks= marks
#         print(" Adding new student in Data-Base ")
    

# s1 = Student("Rahul",98) #parenthesis() To call constructor
# print(s1.name,s1.marks)

# s2 = Student("Rohan",94)
# print(s2.name,s1.marks)


#####Attributes#####
#instance attribute : Obj having Diferent name
#class attribute : Common in all Obj is called Class Attribute

# class Student :
    
#     #class attribute
#     colledge_name = "VIT Pune " #Stores only once 
#     def __init__(self,name,marks): 
                                 
#         self.name = name
#         self.marks= marks
#         print(" Adding new student in Data-Base ")
    

# s1 = Student("Rahul",98)
# # To print Class attribute : syntax :- class.attribute
# print(s1.name,s1.marks,Student.colledge_name)

# s2 = Student("Rohan",94)
# print(s2.name,s1.marks)


#Note: priority - Obj attr > Class attr



#### Class is a collection of Data and Methods ###
###____Methods are Function which belong to Class___###

    
    
# class Student:
#     def __init__(self,name,marks): 
                                 
#         self.name = name
#         self.marks= marks
      
#     def wellcome(self): # if self not return it will give error
#         print(" Wellcome To My-Channel, ", self.name)
    
#     def get_marks(self):
#         return self.marks 

# s1 = Student("Rahul",98)

# s1.wellcome()
# print(s1.get_marks())


#Question!!!!!!

#____Creat student class that takes name & marks of 3 subjects as arguments in constructor.
#____Then creat a method to print the Average


# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
    
#     def get_avg(self):
#         sum = 0
#         for i in self.marks: #We create a loop 
#             sum += i
#         print("Hi ",self.name, " Your avg score is : ",sum/3 )

# s1 = Student(" Tony Stark ",[99,98,97])

# s1.name = " Ironman " #in clss and obj we can manipulate values
# s1.get_avg()

#----------------------------------------------------------
# STATIC METHOD #
#_____ Methods that don't use the self parameter( It Works at Class Level )

# class Student:
#     @staticmethod # Decorator <changing the behaviour of Normal Functiom>
#     def hello():
#         print(" Hello GUys!!!!!!!")
# s1 = Student()
# s1.hello() #Prints Hello Guys without Wrtning self in ()



####### 4 Pillars of OOPs#######
 
  ###### 1. Abstraction ######
  #:- Hinding the impletion details of a class and only showing the essentials features to the user.
  #: Basically hiding unnecessary stuff

class Car:
    def __init__(self):
        ##:- At the Begining car is not started so everything is False
        self.acc = False
        self.brk = False
        self.clutch = False

        ##:- To start it,s True again
    def start(self):
        self.clutch = True
        self.acc = True
        print(" Car Started....!!!")

car1= Car() #Obj is created
car1.start() # Unnecessary features are hidden

#----------------------------------------------------------
#----------------------------------------------------------
     ###### 2.Encapsulation ######

#:-Wrapping data and functions into a single unit (obj)


###Question###

# : creat Account class with 2 attributes - balance & Account no. 
#   creat methods for debit, credit & printing the Balance.


class Account :
    def __init__(self,balc,acc):
        self.balc = balc 
        self.acc = acc

    def debit(self,amount):
        self.balc -= amount
        print(" Rs. ", amount," Was debited ")
        print("Total Balance = ", self.get_balc())

    def credit(self,amount):
        self.balc += amount
        print(" Rs. ", amount," was credited ")
        print("Total Balance = ", self.get_balc())

    def get_balc(self):
        return self.balc

acc1 = Account(10000, 123777)
print(acc1.balc)
print(acc1.acc)

acc1.debit(1000)
acc1.credit(5000)

acc2 = Account(40000,443947)
print(acc2.balc)
print(acc2.acc)

acc2.debit(300)
acc2.credit(9000)