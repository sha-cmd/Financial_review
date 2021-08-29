import yfinance as yf
import pandas as pd

from .CreateTicket import CreateTicketGroup
from .logger import log_init
from .db_conn import connexion
from .db_conn import write_to_db
from .db_conn import close_connexion
from data.securities import liste_complete as lst_cplt


logger = log_init()

class ReadTicket:

    def __init__(self, name, info):
        self.name = name
        self.info = info if (info == 'info') else ''
        self.table = name.lower().replace(' ', '_')

    def execute(self):
        conn = connexion()
        suffix = '_info' if self.info == 'info' else ''
        df = pd.read_sql_query("SELECT * FROM " + self.table + suffix, conn, index_col='index')
        print(df)
