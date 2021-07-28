"""
06 Prepare : Checkpoint B

You are to write a program to track cell phones.
You determine that there are two types of cell phones:
traditional phones that have a phone number, and smart phones that have
a phone number but also contain an email address.
"""



""" Phone class that contais three integers for
the different parts of a phone number"""
class Phone:
    #initing three variables
    def __iit__(self):
        self.area_code = 0
        self.prefix = 0
        self.suffix = 0

    #ask user cell number
    def prompt_number(self):
        self.area_code = int(input("Area Code: "))
        self.prefix = int(input("Prefix: "))
        self.suffix = int(input("Suffix: "))

    #display the number to the user
    def display(self):
        print("Phone info:")
        print(f"({self.area_code}){self.prefix}-{self.suffix}")


""" SmartPhone clcass will inherit some funcs from Phone class"""
class SmartPhone(Phone):
    #new init constructor that will override the parent init
    def __init__(self):
        super().__init__() #super() call the parent init overriden
        #Notice you don’t need to pass self into the parent init!
        self.email = ""
       

    #ask user email
    def prompt(self):
        self.prompt_number()
        self.email = str(input("Email: "))

    #display the email to the user
    def display(self):
        super().display()
        print(f"{self.email}")


"""In main function, create a Phone object,
call its prompt_number method, and then its display method. """

def main():
    phone = Phone() #creating an object called phone
    smartphone = SmartPhone() #creating an object called smartphone
    
    print("Phone:")
    phone.prompt_number()
    print()
    phone.display()
    print()
    
   
    print("Smart phone:")
    smartphone.prompt()
    print()
    smartphone.display() 

if __name__ == "__main__":
    main()
