import yfinance as yf
import pandas as pd

from objects.logger import log_init as log
from objects.Ticket import Ticket
from objects.db_conn import write_to_db
from objects.db_conn import connexion

logger = log()


class Downloader:

    def __init__(self, ticket: Ticket):
        self.ticket = ticket

        mnemonic = yf.Ticker(ticket.mnemo)
        self.data = mnemonic.history(period="max")

        self.rename_columns()
        self.sharpen()

        conn = connexion()
        write_to_db(self.data, self.data.index.name, conn)

    def rename_columns(self):
        col_list = [col.lower().replace(' ', '_') for col in list(self.data.columns)]
        self.data.columns = pd.Index(col_list)
        self.data.index.name = self.data.index.name.lower()

    def sharpen(self):
        try:
            self.data.drop(['dividends', 'stock_splits'], axis=1, inplace=True)
        except KeyError as e:
            print(f"Pas de données dans {self.ticket.name}")
