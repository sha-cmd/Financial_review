"""
Cette classe rapporte et sauvegarde les données en base.
"""

from objects.Writer import Writer
from objects.Ticket import Ticket
from objects.Downloader import Downloader
from objects.Checker import Checker
from data.securities import liste_complete


class FetchAndSave:

    def __init__(self, name):
        t = Ticket(name)
        self.downloader = Downloader(t)
        # self.sharpen()
        Writer(self.downloader)

    @staticmethod
    def download_securities():
        for name, value in liste_complete()[1].items():

            t = Ticket(name)
            c = Checker(t)

            if not c.is_in_db:
                FetchAndSave(name)
                print(t.name_table + " télécharger et sauvegarder")
