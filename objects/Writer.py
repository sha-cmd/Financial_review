"""
Il s’agit avec cette classe d’écrire les données en base de données
"""

from objects.Downloader import Downloader
from objects.db_conn import write_to_db, db_exist, connexion, close_connexion


class Writer:

    def __init__(self, downloader: Downloader):

        if db_exist():
            conn = connexion()
            write_to_db(downloader.data, downloader.ticket.name_table, conn)
            close_connexion(conn)


