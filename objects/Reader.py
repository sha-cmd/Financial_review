"""
Cette classe execute une fonction execute() qui tente de trouver le ticket dans la base de données.
Elle peut néanmoins rapporter le cadre de données par une sous-fonction de lecture, une fois la table contrôlée,
par une fonction read().
"""
import yfinance as yf
import pandas as pd
import numpy as np
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
from objects.Ticket import DATE_DEBUT
from objects.Clock import Clock

logger = log_init()


class Reader:

    def __init__(self, ticket: Ticket, info: str=''):
        self.name = ticket.name
        self.info = info if (info == 'info') else ''
        self.table = ticket.name_table

    def execute(self):
        conn = connexion()
        suffix = '_info' if self.info == 'info' else ''

        try:
            df = pd.read_sql_query("SELECT * FROM " + self.table + suffix, conn, index_col='date')
            return True, str(df.index[0]).split(' ')[0], str(df.index[-1]).split(' ')[0]

        except (OperationalError, DatabaseError) as e:
            logger.debug(self.name + ' n\'est pas dans la table')
            print(e, 'Class Reader')
            return False, DATE_DEBUT, Clock().last_day

    def read(self):
        conn = connexion()
        suffix = '_info' if self.info == 'info' else ''

        try:
            df = pd.read_sql_query("SELECT * FROM " + self.table + suffix, conn, index_col='date')
            return df

        except (OperationalError, DatabaseError) as e:
            logger.debug(self.name + ' n\'est pas dans la table')
            print(e, 'Class Reader')