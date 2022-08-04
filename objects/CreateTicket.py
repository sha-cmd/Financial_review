
from objects.logger import log_init as log
logger = log()


class CreateTicketGroup:

    def __init__(self, names):
        self.names = [key for key, value in names[1].items()]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= len(self.names) - 1:
            val = self.names[self.index]
            self.index += 1
            return val
        else:
            raise StopIteration()

    def __str__(self):
        return "Classe de Groupe de Ticket"
