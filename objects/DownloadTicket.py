import yfinance as yf
import pandas as pd

from .CreateTicket import CreateTicketGroup
from .logger import log_init
from .db_conn import connexion
from .db_conn import write_to_db
from .db_conn import close_connexion
from data.securities import liste_complete as lst_cplt
from objects.Ticket import DATE_DEBUT

logger = log_init()


def record_info(mnemo, name):
    data = yf.Ticker(mnemo)
    col_list = [key for key, value in data.info.items() if 'index' not in key]

    data_df = pd.DataFrame().from_dict(data.info, orient='index').astype('string')\
        .reset_index().T.drop('index', axis=0)
    data_df.columns = col_list
    data_df.index.name = 'index'
    #col_list = [col.lower().replace(' ', '_') for col in list(data_df.columns)]
    #data_df.columns = pd.Index(col_list)
    conn = connexion()
    table_name = name.lower().replace(' ', '_') + '_info'
    print(table_name)
    write_to_db(data_df, table_name, conn)
    close_connexion(conn)
    logger.debug('Écriture dans la base de la table ' + table_name)


def record_data(mnemo, name, if_exist):
    data = yf.Ticker(mnemo)
    data_df = pd.DataFrame(data.history(period='max'))
    col_list = [col.lower().replace(' ', '_') for col in list(data_df.columns)]
    data_df.columns = pd.Index(col_list)
    data_df.index.name = 'index'
    conn = connexion()
    table_name = name.lower().replace(' ', '_')
    print(table_name)
    write_to_db(data_df, table_name, conn, if_exist)
    close_connexion(conn)
    logger.debug('Écriture dans la base de la table ' + table_name)


class DownloadTicket:

    def __init__(self, ticketgroup: CreateTicketGroup):
        self.group = ticketgroup

    def execute(self):
        team_it = iter(self.group.names)
        for i in range(len(self.group.names)):
            name = next(team_it)
            logger.info('Processus de téléchargement et d\'écriture en base de la table ' + name)
            mnemo = lst_cplt()[1][name]
            record_data(mnemo, name)
            record_info(mnemo, name)
