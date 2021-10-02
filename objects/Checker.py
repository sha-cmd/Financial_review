"""
Cette classe lit en base de données, puis informe de la présence du titre par un booléen en liste.
Elle donne en plus les dates de commencement et de fin du Ticket.
"""
from objects.Reader import Reader
from objects.Ticket import Ticket
from objects.logger import log_init as log
logger = log()


class Checker:

    def __init__(self, ticket: Ticket):
        self.is_in_db, self.date_begin, self.date_end = Reader(ticket).execute()
        self.check: list = [x.split()[0] for x in self.__str__().split('->')[1::2]]
        self.check[0] = bool(self.check[0])

    def __str__(self):
        return f"Est en base -> {self.is_in_db} -> date début -> {self.date_begin} -> date fin -> {self.date_end}"
