class ParkingGarage:
    pass

    def __init__(self,tickets, parking_spaces, current_ticket):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_ticket = current_ticket
        
        
    def displayTicket(self):
        print(self.current_ticket)
        
    def payForTicket(self):
        pay_ticket = input ("please enter payment amouunt and enter [purchase] ").lower()
        if pay_ticket == 'purchase':
            self.current_ticket["Paid"] = True
            return self.current_ticket
    
    def takeTicket(self):
       self.tickets = self.tickets - 1
       print(f'There are {self.tickets} tickets remaining')
       self.parking_spaces = self.parking_spaces - 1
       print(f'There are {self.parking_spaces} parking spaces remaining')
       
    def leaveGarage(self):
        if self.current_ticket == False:
            my_ticket.payForTicket()
            
        elif self.current_ticket.values() is True:
          self.tickets = self.tickets + 1
          self.parking_spaces = self.parking_spaces + 1
          print(f'There are {self.parking_spaces} parking spaces remaining')
        # print("Thank you, come again!")
    
def driver():
        while True:
          response = input("Pay, Enter, View, or Exit? ")
        
          if response.lower() == 'view':
             my_ticket.displayTicket()
             break
          elif response.lower() == 'pay':
             my_ticket.payForTicket()
          elif response.lower() == 'enter':
             my_ticket.takeTicket()
          elif response.lower() == 'exit':
            my_ticket.leaveGarage()
            
my_ticket = ParkingGarage(300, 300, {'Paid': False})

driver()