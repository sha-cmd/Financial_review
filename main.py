"""
Ce projet permet de prendre des décisions pour les décideurs, sur le marché financier.
"""
from objects.Update import Update
from objects.Analyse import Analyse

def main():
   # Update('ATOS')
    Analyse().to_xlsx()

if __name__ == '__main__':
    main()
