"""
Ce projet permet de prendre des décisions pour les décideurs, sur le marché financier.
"""
from objects.Update import Update
from objects.Analyse import Analyse
from objects.Report import Report
from data.securities import liste_complete


def maj_db():
    for key, value in liste_complete()[1].items():
        print(key)
        Update(key)


def excel_report():
    Analyse().to_xlsx()


def pdf_report():
    r = Report()
    r.plot()
    r.create()
    r.compiler()


def main():
    # maj_db()
    excel_report()
    # pdf_report()

if __name__ == '__main__':
    main()
