
from objects.ReadTicket import ReadTicket
from objects.Ticket import Ticket
from objects.logger import log_init as log
logger = log()


class Checker:

    def __init__(self, ticket: Ticket):
        self.is_in_db, self.date_begin, self.date_end = ReadTicket(ticket).execute()
        self.check: list = [x.split()[0] for x in self.__str__().split('->')[1::2]]
        self.check[0] = bool(self.check[0])

    def __str__(self):
        return f"Est en base -> {self.is_in_db} -> date début -> {self.date_begin} -> date fin -> {self.date_end}"