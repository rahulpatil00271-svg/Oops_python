

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

# class Car:
#     def __init__(self):
#         ##:- At the Begining car is not started so everything is False
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#         ##:- To start it,s True again
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print(" Car Started....!!!")

# car1= Car() #Obj is created
# car1.start() # Unnecessary features are hidden

#----------------------------------------------------------
#----------------------------------------------------------
     ###### 2.Encapsulation ######

#:-Wrapping data and functions into a single unit (obj)


###Question###

# : creat Account class with 2 attributes - balance & Account no. 
#   creat methods for debit, credit & printing the Balance.


# class Account :
#     def __init__(self,balc,acc):
#         self.balc = balc 
#         self.acc = acc

#     def debit(self,amount):
#         self.balc -= amount
#         print(" Rs. ", amount," Was debited ")
#         print("Total Balance = ", self.get_balc())

#     def credit(self,amount):
#         self.balc += amount
#         print(" Rs. ", amount," was credited ")
#         print("Total Balance = ", self.get_balc())

#     def get_balc(self):
#         return self.balc

# acc1 = Account(10000, 123777)
# print(acc1.balc)
# print(acc1.acc)

# acc1.debit(1000)
# acc1.credit(5000)

# acc2 = Account(40000,443947)
# print(acc2.balc)
# print(acc2.acc)

# acc2.debit(300)
# acc2.credit(9000)




#### Del Keyword####
# : Used to delete Obj properties or obj itself


# class Student:
#     def __init__(self,name):
#         self.name = name

# s1 = Student("Rahul")
# print(s1.name)
# del s1.name   # deletes s1.name
# print(s1.name) # This will give error as attribute s1.name is deleted

#---------------------------------------
########### private(like)  method and attributes  ########
# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass # Here underscore __ is used make a obj private 

# acc1 = Account(" 12221", "abcdefg")

# print(acc1.acc_no) #it can be public
# print(acc1.__acc_pass) #can't be public

#-----------------------------------------

# class Person:
#     __name = " annonymous"

#     def __hello(self):
#         print(" Hello, Guysss!!!!!!!")

#     def wellcome(self):
#         self.__hello()
#     # Note : As it's defined under class method so it can be accesed even though it's private (__)
# p1 = Person()
# print(p1.wellcome()) # No error it will give Hello Guysss

##print(p1.__hello()) # : Will give error as it,s outside the class




####### 3. Inheritance ######

# : when one class(child/derived) derives the properties & methods of another class(parent/base)


# # : Parent Class
# class Car:
#   color = " Black "
#   @staticmethod
#   def start():
#     print(" Car Started.. ")

#   @staticmethod
#   def stop():
#     print(" Car Stopped ")

# # : Child Class 
# class ToyotaCar(Car): ### : characteristics inherited are mentioned inside parenthsis()
#   def __init__(self,name):
#     self.name = name

# car1 = ToyotaCar(" Fortuner")
# car2 = ToyotaCar(" Prius")

# print(car1.name) #: Name of car will be printed
# print(car1.start()) #: Even though Start is not in in ToyotaCar(chld) it's inherited from Car(parent) 
# print(car1.color)


#_____ # Types In INheritance # ______#

#------------------------------
# single Inheritance #
#:- Base --> derived(child)
#------------------------------

#------------------------------
# Multi-level Inheritance #
#----------------------------
# #Ex.
# # Parent 
# class Car:
#   color = " Black "
#   @staticmethod
#   def start():
#     print(" Car Started.. ")

#   @staticmethod
#   def stop():
#     print(" Car Stopped ")

# # : Child Class 
# class ToyotaCar(Car):
#   def __init__(self,brand):
#     self.brand = brand

# # : Properties of both ToyotaCar & Car
# class Fortuner(ToyotaCar):
#   def __init__(self,type):
#     self.type= type



#---------------------------------------------
# multiple inheritance #

# #Base 1 + #base2 ---> #Derived

# #Parent 1
# class A:
#   varA = " Wellcome to class A"

# #parent 2
# class B:
#   varB = " wellcome to Class B "

# #Child 
# class C(A,B):
#   varC = " Wellcome to Class C"
# #obj of C
# c1 = C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

#----------------------------------
# Super Method # (Related to inheritance)
#Super() method is uded to access methods of parent Class
#