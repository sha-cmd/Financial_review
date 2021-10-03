import datetime
import numpy as np
import pandas as pd

from objects.logger import log_init as log
logger = log()


class Clock:

    def __init__(self):
        self.date = datetime.datetime.now()
        if not (np.is_busday(str(self.date.date()))):
            self.last_day = str(self.date).split(' ')[0]  # Pour télécharger les données du vendredi également
        else:
            self.last_day = np.busday_offset(str(self.date.date()), -1, roll='forward')
            # Attention à ne pas prendre les données en cours de journée
        self.next_day = np.busday_offset(str(self.date.date()), 0, roll='forward')
