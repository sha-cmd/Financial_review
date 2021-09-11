import yfinance as yf
import pandas as pd

from objects.logger import log_init as log
from objects.Dategiver import Dategiver
from objects.Checker import Checker
from objects.Ticket import Ticket
from objects.DownloadTicket import record_data
from data.securities import liste_complete
from objects.db_conn import write_to_db
from objects.db_conn import connexion
from objects.Ticket import DATE_DEBUT
logger = log()

class Downloader:

    def __init__(self, date_given: Dategiver, checker: Checker, ticket: Ticket):
        if checker.is_in_db:
            if date_given.conclusion:
                #self.data = yf.download(ticket.mnemo, start=str(dategiver.from_date), end=str(dategiver.to_date))
                #self.data.to_pickle('data.pkl')
                self.data = pd.read_pickle('data.pkl')
                self.rename_columns()
                print(self.data)
                #conn = connexion()
                #write_to_db(self.data, name=ticket.name_table, con=conn, if_exist='append')
                #conn.close()
#                record_data(data, ticket.name, 'append')
        else:
            self.data = yf.download(ticket.mnemo, start=str(date_given.from_date), end=DATE_DEBUT)
            self.data.to_pickle('data.pkl')
            self.data = pd.read_pickle('data.pkl')
            self.rename_columns()
            print(self.data)

    def rename_columns(self):
        col_list = [col.lower().replace(' ', '_') for col in list(self.data.columns)]
        self.data.columns = pd.Index(col_list)
        print(self.data.index.name)
        self.data.index.name = self.data.index.name.lower()

