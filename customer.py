"""
customer.py to prove assignment 04
"""

#customer class
class Customer:

    #initing the variables
    def __init__(self):
        self.id = ""
        self.name = ""
        self.order = []

    #get order count  ---- using len built func
    def get_order_count(self):
        return len(self.order)
        
    #get total -- for loop
    def get_total(self):
        total = 0
        for order in self.order:
            total += order.get_total()
        return total
        
        
    #add order
    def add_order(self, order):
        self.order.append(order)
        
    #display summary
    def display_summary(self):
        
        #in order to get the information and format it 
        total = self.get_total()
        order = self.get_order_count()
        
        print(f"Summary for customer '{self.id}':")
        print(f"Name: {self.name}")
        print(f"Orders: {order}")
        print(f"Total: {total:.2f}")
        
        
    #display receipts
    def display_receipts(self):
        print(f"Detailed receipts for customer '{self.id}':")
        print(f"Name: {self.name}")
        
        #iterating through the orders
        for order in self.order:
            print()
            order.display_receipt()
            
        

    
