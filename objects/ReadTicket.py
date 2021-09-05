import yfinance as yf
import pandas as pd
import sqlite3

from sqlite3 import OperationalError
from pandas.io.sql import DatabaseError
from .CreateTicket import CreateTicketGroup
from .Ticket import Ticket
from .logger import log_init
from .db_conn import connexion
from .db_conn import write_to_db
from .db_conn import close_connexion
from data.securities import liste_complete as lst_cplt


logger = log_init()

class ReadTicket:

    def __init__(self, ticket: Ticket, info: str=''):
        self.name = ticket.name
        self.info = info if (info == 'info') else ''
        self.table = self.name.lower().replace(' ', '_')

    def execute(self):
        conn = connexion()
        suffix = '_info' if self.info == 'info' else ''
        try:
            self.df = pd.read_sql_query("SELECT * FROM " + self.table + suffix, conn, index_col='index')
            print(self.df)

        except (OperationalError, DatabaseError) as e:
            logger.debug(self.name + ' n\'est pas dans la table')
            print(e, 'Class ReadTicket')



