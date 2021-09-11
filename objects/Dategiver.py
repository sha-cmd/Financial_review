import numpy as np

from objects.Checker import Checker
from objects.Clock import Clock
from objects.Ticket import DATE_DEBUT
from objects.logger import log_init as log
logger = log()


class Dategiver:

    def __init__(self, checker: Checker, clock: Clock):
        self.checker = checker
        if checker.is_in_db:
            self.conclusion: bool = not (clock.last_day == np.datetime64(checker.date_end))
            if self.conclusion:
                self.from_date = np.busday_offset(np.datetime64(checker.date_end), 1)
                self.to_date = clock.last_day
        else:
            self.from_date = DATE_DEBUT
            self.to_date = clock.last_day
            self.conclusion = False

    def __str__(self):
        return f"Il y a besoin de mise à jour {self.conclusion}, est dans la base {self.checker.is_in_db}"
