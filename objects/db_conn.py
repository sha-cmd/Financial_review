
from sqlite3 import connect
from os.path import exists
from objects.logger import log_init as log


DB_PATH = "data/financial_db.sqlite"
IF_EXIST = "replace"
logger = log()

def db_exist():
    """
        Contrôle existence de la base de données.
        :return:
        """
    file_exists = exists('data/financial_db.sqlite')
    return file_exists


def connexion():
    conn = connect(DB_PATH)
    logger.debug('Connexion à la base ' + DB_PATH)
    return conn

def write_to_db(df, name, con, if_exist=IF_EXIST):
    df.to_sql(name, con, if_exists=if_exist)
    logger.debug('Écriture de ' + name + ' en base')

def close_connexion(conn):
    conn.close()
    logger.debug('Déconnexion de la base ' + DB_PATH)
    # data_frame.to_sql(table_nom, conn)
    ##conn.close()
    # c = conn.cursor()
    # Replacing spaces by underscores in table names.
    # c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='" + self._table_nom.replace(' ', '_') + "';")
