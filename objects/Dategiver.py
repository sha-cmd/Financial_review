import numpy as np

from objects.Checker import Checker
from objects.Clock import Clock
from objects.logger import log_init as log
logger = log()


class Dategiver():

    def __init__(self, checker: Checker, clock: Clock):
        self.conclusion: bool = not (clock.last_day == np.datetime64(checker.date_end))
        if self.conclusion:
            self.from_date = np.datetime64(checker.date_end)
            self.to_date = clock.last_day

    def __str__(self):
        return f"Il y a besoin de mise à jour {self.conclusion}"
