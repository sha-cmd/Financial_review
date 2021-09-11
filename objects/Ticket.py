
from data.securities import liste_complete
from objects.logger import log_init as log

DATE_DEBUT = '1983-01-01'
logger = log()

class Ticket:

    def __init__(self, name: str):
        self.name = name.upper()
        self.mnemo = liste_complete()[1][self.name]
        self.name_table = self.name.lower().replace(' ', '_')