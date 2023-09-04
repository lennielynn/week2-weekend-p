class ParkingGarage:
    pass

    def __init__(self,tickets, parking_spaces, current_ticket):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_ticket = current_ticket
        
        
    def displayTicket(self):
        print(self.current_ticket)
        
    def payForTicket(self):
        pay_ticket = input ("please input payment and enter [purchase] ").lower()
        if pay_ticket == 'purchase':
            self.current_ticket["Paid"] = True
            print(self.current_ticket)
            print('Thank you, purchase complete.')
        else:
            print('Please enter [purchase] to complete transaction')
            my_ticket.payForTicket()
    
    def takeTicket(self):
       if self.tickets < 1 or self.parking_spaces < 1:
           print('Garage Full')
       elif self.tickets  >= 1 or self.parking_spaces >= 1 : 
           self.tickets = self.tickets - 1
           print(f'There are {self.tickets}/300 tickets remaining')
           self.parking_spaces = self.parking_spaces - 1   
           print(f'There are {self.parking_spaces}/300 parking spaces remaining')
           
    def leaveGarage(self):
         if self.current_ticket['Paid'] == False:
            print ('Your balance in unpaid. redirecting to payment..')
            my_ticket.payForTicket()
         elif self.current_ticket['Paid'] == True:
          self.tickets = self.tickets + 1
          self.parking_spaces = self.parking_spaces + 1
          print('Thank you, have a nice day!')
       
       
def driver():
        while True:
          response = input("Pay, Enter, Leave, or View? ")
        
          if response.lower() == 'view':
             my_ticket.displayTicket()
          elif response.lower() == 'pay':
             my_ticket.payForTicket()
          elif response.lower() == 'enter':
             my_ticket.takeTicket()
          elif response.lower() == 'leave':
             my_ticket.leaveGarage()
            
my_ticket = ParkingGarage(300, 300, {'Paid': False})

driver()