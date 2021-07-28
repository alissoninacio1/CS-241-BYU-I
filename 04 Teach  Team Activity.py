class Date:
    def __init__(self):
        self.day = 1
        self.month = 1
        self.year = 2000

    def prompt_user(self):
        self.day = int(input("Day: "))
        self.month = int(input("Month: "))
        self.year = int(input("Year: "))

    def display_date(self):
        print(f"{self.month}/{self.day}/{self.year}")



class Assignment:
     def __init__(self):
         self.name = "Untitled"
         self.start_date = Date()
         self.due_date = Date()
         self.end_date =  Date()

     def ask_user(self):
         self.name = str(input("Name: "))
         print()
         print("Start Date:")
         self.start_date.prompt_user()
         print()
         print("Due Date:")
         self.due_date.prompt_user()
         print()
         print("End Date:")
         self.end_date.prompt_user()
         print()
         
     def display_data(self):
         print("Assignment:" + self.name)
         print("Start Date:")
         self.start_date.display_date()
         print("Due Date:")
         self.due_date.display_date()
         print("End Date:")
         self.end_date.display_date()


def main():
    my = Assignment()
    my.ask_user()
    my.display_data()

if __name__ == "__main__":
    main()
