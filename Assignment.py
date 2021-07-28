from Date import Date

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
