"""
Cette classe récupère les dates à télécharger et les ranges dans la base de données.
Elle mélange le téléchargement et le rangement dans le conteneur de données.
"""
import yfinance as yf
import pandas as pd

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
        self.data_update = yf.download(name, start=self.date.from_date, end=self.date.to_date)
        self.sharpen()
        if self.reader.table.index[-1] != self.data_update.index[0]:
            self.df = self.reader.append(self.data_update)
            if db_exist():
                conn = connexion()
                for it, row in self.df.iterrows():
                    sql = "INSERT INTO `" \
                          + self.ticket.name_table \
                          + "` (`date`, `open`, `high`, `low`, `close`, `volume`) VALUES (%s, %s, %s, %s, %s, %s)"

                    conn.execute(sql, (it, row['open'], row['high'], row['low'], row['close'], row['volume']))

                    conn.commit()
                close_connexion(conn)
        else:
            logger.debug('Problème de dates dans les indexes, nom: ' + self.ticket.name_table
                         + ", date: " + self.reader.table.index[-1] + " et " + self.data_update.index[0])
            print('Problème de dates dans les indexes, nom: ' + self.ticket.name_table
                         + ", date: " + self.reader.table.index[-1] + " et " + self.data_update.index[0])

    def sharpen(self):
        self.data.drop('Adj Close', axis=1, inplace=True)
