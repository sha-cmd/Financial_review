import datetime
import numpy as np

from objects.logger import log_init as log
logger = log()


class Clock:

    def __init__(self):
        self.date = datetime.datetime.now()
        self.last_day = np.busday_offset(str(self.date.date()), -1, roll='forward')
        self.next_day = np.busday_offset(str(self.date.date()), 0, roll='forward')
