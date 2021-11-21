"""
Cette classe récupère les dates à télécharger et les ranges dans la base de données.
Elle mélange le téléchargement et le rangement dans le conteneur de données.
"""
import yfinance as yf
import pandas as pd
import numpy as np

from objects.Ticket import Ticket
from objects.Checker import Checker
from objects.DateGiver import DateGiver
from objects.Reader import Reader
from objects.Clock import Clock
from objects.db_conn import connexion, write_to_db, close_connexion, db_exist
from objects.logger import log_init as log

logger = log()


class Update:

    def __init__(self, name):
        self.ticket = Ticket(name)
        self.checked = Checker(self.ticket)
        self.date = DateGiver(self.checked, Clock())
        self.reader: pd.DataFrame = Reader(self.ticket).read()
#        print(self.date.conclusion)
        if (self.date.conclusion) & (pd.to_datetime(self.date.from_date) < pd.to_datetime(self.date.to_date)):
            print(self.date.from_date, self.date.to_date)
            self.data_update = yf.download(self.ticket.mnemo, start=self.date.from_date, end=self.date.to_date)
            self.sharpen()
            self.rename_columns()
            if not self.data_update.empty:
                if (pd.to_datetime(self.reader.index[-1]) < pd.to_datetime(self.data_update.index[0])):
                    #print('ok', self.ticket.name_table, self.data_update)
                    self.df = self.reader.append(self.data_update)
                    if db_exist():
                        conn = connexion()
                        for it, row in self.data_update.iterrows():
                            sql = "INSERT INTO `" \
                                  + self.ticket.name_table \
                                  + "`  VALUES (?,?,?,?,?,?);"

                            conn.execute(sql, (str(it), row['open'], row['high'], row['low'], row['close'], row['volume']))

                            conn.commit()
                        close_connexion(conn)
        else:
            logger.debug('Problème de dates dans les indexes, nom: ' + self.ticket.name_table
                         + ", date: " + self.reader.index[-1] + " et " + str(self.date.from_date))
            print('Problème de dates dans les indexes, nom: ' + self.ticket.name_table
                  + ", date: " + self.reader.index[-1] + " et " + str(self.date.from_date))

    def rename_columns(self):
        col_list = [col.lower().replace(' ', '_') for col in list(self.data_update.columns)]
        self.data_update.columns = pd.Index(col_list)
        self.data_update.index.name = self.data_update.index.name.lower()

    def sharpen(self):
        self.data_update.drop('Adj Close', axis=1, inplace=True)
