
from objects.logger import log_init as log
logger = log()

class Ticket():

    def __init__(self, name: str):
        self.name = name