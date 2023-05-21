"""
Ce projet permet de prendre des décisions pour les décideurs, sur le marché financier.
"""
from objects.Downloader import Downloader
from objects.Update import Update
from objects.Analyse import Analyse
from objects.Ticket import Ticket
from objects.Report import Report
from objects.API_request import API_request
from data.securities import liste_complete


def create_db():
    for key, value in liste_complete()[1].items():
        print(key)
        ticket = Ticket(key)
        Downloader(ticket)

def maj_db():
    for key, value in liste_complete()[1].items():
        print(key)
        Update(key)


def excel_report():
    Analyse().to_xlsx()

def text_report():
    Analyse().to_txt()

def pdf_report():
    r = Report()
    r.plot()
    r.create()
    r.compiler()

def api_report():
    a = API_request()
    a.to_xlsx(4)

def main():
    #create_db()
    #maj_db()
    #text_report()
    excel_report()
    #pdf_report()
    #api_report()

if __name__ == '__main__':
    main()
