"""
Ce projet permet de prendre des décisions pour les décideurs, sur le marché financier.
"""
from multiprocessing import Process
from objects.Downloader import Downloader
from objects.Update import Update
from objects.Analyse import Analyse
from objects.Ticket import Ticket
from objects.Report import Report
from objects.API_request import API_request
from os.path import exists
from data.securities import liste_complete


def create_db():
    file_exists = exists('data/financial_db.sqlite')
    if not file_exists:
        con = sqlite3.connect("data/financial_db.sqlite")
    for key, value in liste_complete()[1].items():
        print(key)
        ticket = Ticket(key)
        p = Process(target=Downloader, args=[ticket])
        p.run()

def maj_db():
    for key, value in liste_complete()[1].items():
        print(key)
        p = Process(target=Update, args=[key])
        p.run()


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
    a.to_xlsx(2)  # 2 et 4 et 8 et 10
    a.to_xlsx(4)  # 2 et 4 et 8 et 10
    a.to_xlsx(10)  # 2 et 4 et 8 et 10

def main():
    create_db()  # Pour recréer une base avec 10 ans de données
    #maj_db()
    #text_report()  # Select portfolio in data/selection.txt
    #excel_report()
    #pdf_report()
    #api_report()  # Need an API KEY to https://site.financialmodelingprep.com/developer/docs/pricing

if __name__ == '__main__':
    main()
