class Ticket:
    def __init__(self, movie_name, ticket_price, total_tickets, language="Geo"):
        self.movie_name = movie_name
        self.ticket_price = ticket_price
        self.total_tickets = total_tickets
        self.language = language

    def __str__(self):
        return f"{self.movie_name} ({self.language}): {self.total_tickets} tickets available at {self.ticket_price} each"

    #

    def __gt__(self, other):
        return self.total_tickets > other.total_tickets

    def __lt__(self, other):
        return self.total_tickets < other.total_tickets

    def __ge__(self, other):
        return self.total_tickets >= other.total_tickets

    def __le__(self, other):
        return self.total_tickets <= other.total_tickets

    def __eq__(self, other):
        return self.total_tickets == other.total_tickets

    def __ne__(self, other):
        return self.total_tickets != other.total_tickets


class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.name}: {self.balance} balance"

    def buy_ticket(self, ticket, num_tickets):
        if num_tickets <= ticket.total_tickets and num_tickets * ticket.ticket_price <= self.balance:
            self.balance -= num_tickets * ticket.ticket_price
            ticket.total_tickets -= num_tickets
            print(f"{self.name}, you bought {num_tickets} tickets to {ticket.movie_name} ({ticket.language})")
        elif num_tickets > ticket.total_tickets:
            print(f"Sorry, only {ticket.total_tickets} tickets left for {ticket.movie_name} ({ticket.language})")
        else:
            print(
                f"Sorry {self.name} you don't have enough balance to buy {num_tickets} tickets to {ticket.movie_name} ({ticket.language})")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. Balance: {self.balance}")

t1 = Ticket("Creed III", 10, 20)
t2 = Ticket("Puss in Boots: The Last Wish", 8, 15, "Eng")
u1 = User("Datuna", 100)
u2 = User("Bachana", 60)
print(t1)
print(t2)
print(u1)
print(u2)
print()
print()
u1.deposit(50)
u1.buy_ticket(t1, 3)
u1.buy_ticket(t2, 5)
print(f"Balance:{u1.balance}") #sachvenebeli
print()
print()
u2.buy_ticket(t1,5)
u2.buy_ticket(t2,2)
print(f"Balance:{u2.balance}") #sachv
print()
print()


#shedareba

print(t1 > t2)
print(t1 < t2)
print(t1 >= t2)
print(t1 <= t2)
print(t1 == t2)
print(t1 != t2)
print(t1.total_tickets > 10)
