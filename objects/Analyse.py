import copy
import numpy as np

from data.securities import liste_actions_pme, liste_complete
from decimal import Decimal
from objects.Clock import Clock
from objects.Reader import Reader
from objects.Ticket import Ticket
from joblib import Parallel, delayed


class Analyse:

    def __init__(self, list_of_stocks=liste_complete()[1]):
        self.date_last_day = Clock()
        self.list_of_stocks = list_of_stocks
        self.avg = {str(): Decimal()}
        self.avg_d_log = {str(): Decimal()}
        self.avg_a_log = {str(): Decimal()}
        self.avg_d_dis = {str(): Decimal()}
        self.avg_a_dis = {str(): Decimal()}
        self.perf_shot = {str(): Decimal()}
        self.price = {str(): Decimal()}

    def perf_du_dernier_jour(self, data, name):
        data
        self.perf_shot.update({name: round(((data['close'][-1] /
                                             data['close'][-2]) - 1) * 100
                                           , 2)})
        self.price.update(
            {name: copy.deepcopy(round(data.iloc[-1]['close'], 2))})

        self.avg.update({name: round(((data.iloc[-1]['close'] /
                                       data.iloc[0]['close']) - 1) * 100, 2)})
        data['Log_ror'] = np.log(
            data['close'] /
            data['close']
            .shift(1))
        self.avg_d_log.update({name: round(data['Log_ror'].mean() * 100, 2)})
        self.avg_a_log.update({name: round(data['Log_ror'].mean() * 250 * 100, 2)})
        data['Dis_ror'] = (data['close'] / data['close'].shift(1)) - 1
        self.avg_d_dis.update({name: round(data['Dis_ror'].mean() * 100, 2)})
        self.avg_a_dis.update({name: round(data['Dis_ror'].mean() * 250 * 100, 2)})
        return data

    def to_txt(self):
        fichier = open("reports_txt/performance_du_jour.txt", "w")
        Parallel(n_jobs=1)(delayed(self.make_txt)(name, fichier) for name, mnemonic in self.list_of_stocks.items())

        fichier.close()

    def make_txt(self, name, fichier):
        data = Reader(Ticket(name)).read()
        data = self.perf_du_dernier_jour(data, name)
        fichier.write(
            f'****************************\nPour {name:>36}  \naujourd\'hui: {self.perf_shot[name]:>+5}% -> {self.price[name]:5}€\n')
        fichier.write(
            f'sur période du  {data.index[0]} au {data.index[-1]} :\n')
        fichier.write(f'plus value sur la période          {self.avg[name]:+5}%\n')
        fichier.write(f'moyenne journalière suivi intégral {self.avg_d_log[name] :+5}%\n')
        if data['Log_ror'].count() > 250:
            fichier.write(f'moyenne annuel suivi intégral      {self.avg_a_log[name] :+5}%\n')
        fichier.write(f'moyenne journalière suivi sommé    {self.avg_d_dis[name]:+5}%\n')
        if data['Dis_ror'].count() > 250:
            fichier.write(f'moyenne annuelle suivi sommé       {self.avg_a_dis[name]:+5}%\n')
