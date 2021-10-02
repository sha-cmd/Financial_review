"""
Cette classe rapporte et sauvegarde les données en base.
"""

from objects.Writer import Writer
from objects.Ticket import Ticket
from objects.Downloader import Downloader


class FetchAndSave:

    def __init__(self, name):
        t = Ticket(name)
        self.downloader = Downloader(t)
        self.sharpen()
        Writer(self.downloader)


