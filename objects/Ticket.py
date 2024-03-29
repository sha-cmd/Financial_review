from data.securities import liste_complete
from objects.logger import log_init as log

DATE_DEBUT = '1983-01-01'
logger = log()


class Ticket:

    def __init__(self, name: str):
        self.name = name
        self.mnemo = liste_complete()[1][self.name]
        self.name_table = self.name.lower().replace("&", "").replace("/", "").replace("-",
                                                                                      "").replace(
            "  ", " ").replace("  ", " ").replace(' ', '_').replace("(", "").replace(")", "").replace("é", "e").replace(
            "è", "e")
