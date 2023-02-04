#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:15:02 2020
Ce programme analyse et crée un rapport financier
@author: romain Boyrie
"""
from data.securities import liste_complete
import time
import matplotlib.pyplot as plt
import mplfinance as mpf
from glob import glob
from scipy import stats
import pandas as pd
from prophet import Prophet
import numpy as np
from scipy.stats import norm
from decimal import Decimal
import os
import sys
import gc
from objects.latexFile import START, CORPS, CORPSSITE, CORPSWIKI, CORPSSECTION, CORPSLEREVENU, CORPSLAPOSTE, \
    CORPSBOURSORAMA, \
    CHAPITRE, DESCRIPTION, TABLE, END

from objects.Ticket import Ticket
from objects.Reader import Reader
from objects.Clock import Clock
from objects.Analyse import Analyse
from joblib import Parallel, delayed

STOCK_LEVEL = 'Cours de l\'action '
SOURCE_DIR = "reports_pdf/"


class Report:
    def __init__(self):  # , analyse):
        print('Report')
        self.data = Analyse()
        self.df = pd.read_excel('tex/Strategie_PME.xlsx')
        self.secteurs = pd.unique(self.df['Secteur'])

    def plot(self):
        Parallel(n_jobs=-1)(
            delayed(self.graph_01)(name) for name, mnemonic in liste_complete()[1].items())
        Parallel(n_jobs=-1)(
            delayed(self.graph_02)(name) for name, mnemonic in liste_complete()[1].items())
        Parallel(n_jobs=-1)(
            delayed(self.graph_03)(name) for name, mnemonic in liste_complete()[1].items())
        Parallel(n_jobs=-1)(
            delayed(self.graph_04)(name) for name, mnemonic in liste_complete()[1].items())
        Parallel(n_jobs=-1)(
            delayed(self.graph_05)(name) for name, mnemonic in liste_complete()[1].items())

        Parallel(n_jobs=-1)(
            delayed(self.graph_06)(name) for name, mnemonic in liste_complete()[1].items())
        Parallel(n_jobs=-1)(
            delayed(self.graph_07)(name) for name, mnemonic in liste_complete()[1].items())

        Parallel(n_jobs=-1)(
            delayed(self.graph_08)(name) for name, mnemonic in liste_complete()[1].items())
        Parallel(n_jobs=-1)(
            delayed(self.graph_09)(name) for name, mnemonic in liste_complete()[1].items())
        Parallel(n_jobs=-1)(
            delayed(self.graph_10)(name) for name, mnemonic in liste_complete()[1].items())
        Parallel(n_jobs=-1)(
            delayed(self.graph_11)(name) for name, mnemonic in liste_complete()[1].items())
        Parallel(n_jobs=-1)(
            delayed(self.graph_12)(name) for name, mnemonic in liste_complete()[1].items())

        Parallel(n_jobs=-1)(
            delayed(self.sim_monte_carlo)(name) for name, mnemonic in liste_complete()[1].items())
        Parallel(n_jobs=-1)(
            delayed(self.prophet)(name) for name, mnemonic in liste_complete()[1].items())

    def compiler(self):
        os.chdir("reports_pdf")

        os.system("pdflatex " + str(Clock().date.date()) + '.tex')
        os.system("pdflatex " + str(Clock().date.date()) + '.tex')

    def create(self):
        # Automation of a report
        # Check if the file exists
        if os.path.isfile(SOURCE_DIR + str(Clock().date.date()) + '.tex'):
            files_to_erase = glob(SOURCE_DIR + str(Clock().date.date()) + '*')
            for file in files_to_erase:
                os.remove(file)
        with open(SOURCE_DIR + str(Clock().date.date()) + '.tex', 'w', encoding='utf8') as fout:
            fout.write(START.replace('DATE', str(Clock().date.date())))

            for secteur in self.secteurs:
                noms = [x for x in liste_complete()[1] if
                        x in self.df.loc[self.df['Secteur'] == secteur]['Nom'].values.ravel()]
                fout.write(CHAPITRE.replace('TITRE', str(secteur)))
                for name in noms:
                    values_list = [('TITRE', name), ('SITE', self.df.loc[self.df['Nom'] == name]['Adresse'].values[0]),
                                   ('WIKI', self.df.loc[self.df['Nom'] == name]['Wiki'].values[0]),
                                   ('BOURSORAMA', self.df.loc[self.df['Nom'] == name]['Boursorama'].values[0]),
                                   ('LAPOSTE', self.df.loc[self.df['Nom'] == name]['Laposte'].values[0]),
                                   ('LEREVENU', self.df.loc[self.df['Nom'] == name]['Lerevenu'].values[0])]
                    bodies_list = [CORPSSECTION, CORPSSITE, CORPSWIKI, CORPSBOURSORAMA, CORPSLAPOSTE, CORPSLEREVENU]
                    for index, corps in enumerate(bodies_list):
                        try:
                            fout.write(corps.replace(values_list[index][0], values_list[index][1]))
                        except Exception:
                            pass

                    name_us = str(name).replace(' ', '_')
                    fout.write(CORPS.replace('TITRE', name_us))
                    self.data = Analyse()
                    if name in liste_complete()[1]:
                        data = Reader(Ticket(name)).read()
                        self.data.perf_du_dernier_jour(data, name)
                        fout.write(
                            TABLE.replace('PRIX', str(round(Decimal(self.data.price[name]), 2))).replace('TITRE',
                                                                                                         name)
                                .replace('ROR', str(round(Decimal(self.data.perf_shot[name]), 2)))
                                .replace('LOG', str(round(Decimal(self.data.avg_a_log[name]))))
                                .replace('CINQ', str(round(Decimal(self.data.avg5[name]), 2)) if self.data.avg5[
                                                                                                     name] is not None else str(
                                0))
                                .replace('TROIS', str(round(Decimal(self.data.avg3[name]), 2)) if self.data.avg3[
                                                                                                      name] is not None else str(
                                0))
                                .replace('UN', str(round(Decimal(self.data.avg1[name]), 2)) if self.data.avg1[
                                                                                                   name] is not None else str(
                                0))
                                .replace('RISQUE', str(round(Decimal(self.data.risk[name]), 2))))

                    try:
                        fout.write(DESCRIPTION.replace('ACTIVITE',
                                                       self.data.df.loc[self.data.df['Nom'] == name]['Activité'].values[
                                                           0]))
                    except Exception:
                        pass
                    fout.write(r'\newpage')
            fout.write(END)

    def graph_01(self, nom):

        print('Graph 01', nom)
        methode = 'close'
        data = Reader(Ticket(nom)).read()
        if(len(data) == 0):
            sys.exit(nom, "n'a pas de données dans la base, retirer là des securities")
        data.index = pd.DatetimeIndex([pd.to_datetime(x).tz_localize(None) for x in data.index])
        methode = 'close'
        plt.figure(figsize=(10, 6))
        mpf.plot(data.iloc[:, 0:5], type='line', title=STOCK_LEVEL + nom
                 , savefig='OutputFiles/stockprice_' + methode + '_' + str(nom).replace(' ', '_') + '.png')
        plt.close()
        mpf.plot(data.iloc[-500:, 0:5], type='line', mav=(12, 20, 50), volume=True, title=STOCK_LEVEL + nom
                 , savefig='OutputFiles/mva_' + methode + '_' + str(nom).replace(' ', '_') + '.png')
        plt.close()

    def graph_02(self, nom):
        print('Graph 02', nom)
        methode = 'close'
        data = Reader(Ticket(nom)).read()
        data.index = pd.DatetimeIndex([pd.to_datetime(x).tz_localize(None) for x in data.index])
        top = plt.subplot2grid((4, 4), (0, 0), rowspan=3, colspan=4)
        top.plot(data.index, data[methode], label='Prix à la Clôture')
        plt.title("{}{}".format(STOCK_LEVEL, nom))
        plt.legend(loc=2)
        # The bottom plot consisting of daily trading volume
        bottom = plt.subplot2grid((4, 4), (3, 0), rowspan=1, colspan=4)
        bottom.bar(data.index, data['volume'])
        plt.title("Volume de l'action {}".format(nom))
        plt.gcf().set_size_inches(10, 6)
        plt.subplots_adjust(hspace=0.75)
        plt.savefig('OutputFiles/stockprice_' + methode + '_' + str(nom).replace(' ', '_') + '.png')
        plt.close()

    def graph_03(self, nom):
        print('Graph 03', nom)
        methode = 'close'
        data = Reader(Ticket(nom)).read()
        data.index = pd.DatetimeIndex([pd.to_datetime(x).tz_localize(None) for x in data.index])
        # Volatility plot
        df_filled = data[[methode]].asfreq('D', method='ffill')
        df_returns = df_filled.pct_change()
        df_std = df_returns[-500:].rolling(window=30, min_periods=30).std()
        df_std.plot(label='Volatilité à la Clôture 30')
        plt.savefig('OutputFiles/volatility_30_' + methode + '_' + str(nom).replace(' ', '_') + '.png')

        plt.clf()
        plt.close()

    def graph_04(self, nom):
        print('Graph 04', nom)
        methode = 'close'
        data = Reader(Ticket(nom)).read()
        data.index = pd.DatetimeIndex([pd.to_datetime(x).tz_localize(None) for x in data.index])
        df_filled = data[[methode]].asfreq('D', method='ffill')
        df_returns = df_filled.pct_change()
        df_std = df_returns[-250:].rolling(window=15, min_periods=15).std()
        df_std.plot(label='Volatilité à la Clôture 15')
        plt.savefig('OutputFiles/volatility_15_' + methode + '_' + str(nom).replace(' ', '_') + '.png')

        plt.clf()
        plt.close()

    def graph_05(self, nom):
        print('Graph 05', nom)
        methode = 'close'
        data = Reader(Ticket(nom)).read()
        data.index = pd.DatetimeIndex([pd.to_datetime(x).tz_localize(None) for x in data.index])
        df_filled = data[[methode]].asfreq('D', method='ffill')
        df_returns = df_filled.pct_change()
        df_std = df_returns[-50:].rolling(window=7, min_periods=7).std()
        df_std.plot(label='Volatilité à la Clôture 7')
        plt.savefig('OutputFiles/volatility_7_' + methode + '_' + str(nom).replace(' ', '_') + '.png')

        plt.clf()
        plt.close()

    def graph_06(self, nom):
        print('Graph 06', nom)
        methode = 'close'
        data = Reader(Ticket(nom)).read()
        data.index = pd.DatetimeIndex([pd.to_datetime(x).tz_localize(None) for x in data.index])
        df_filled = data[[methode]].asfreq('D', method='ffill')
        df_returns = df_filled.pct_change()
        df_std = df_returns[-25:].rolling(window=3, min_periods=3).std()
        df_std.plot(label='Volatilité à la Clôture 3')
        plt.savefig('OutputFiles/volatility_3_' + methode + '_' + str(nom).replace(' ', '_') + '.png')
        del df_filled, df_returns, df_std
        plt.clf()
        plt.close()

    def graph_07(self, nom):
        print('Graph 07', nom)

        methode = 'close'
        data = Reader(Ticket(nom)).read()
        data.index = pd.DatetimeIndex([pd.to_datetime(x).tz_localize(None) for x in data.index])
        # Volatility plot
        df_filled = data[['volume']].asfreq('D', method='ffill')
        df_returns = df_filled.pct_change()
        df_std = df_returns[-500:].rolling(window=30, min_periods=30).std()
        df_std.plot(label='Volatilité au Volume 30')
        plt.savefig('OutputFiles/volat_volub_30_' + methode + '_' + str(nom).replace(' ', '_') + '.png')

        plt.clf()
        plt.close()

    def graph_08(self, nom):
        print('Graph 08', nom)
        methode = 'close'
        data = Reader(Ticket(nom)).read()
        data.index = pd.DatetimeIndex([pd.to_datetime(x).tz_localize(None) for x in data.index])
        df_filled = data[['volume']].asfreq('D', method='ffill')
        df_returns = df_filled.pct_change()
        df_std = df_returns[-250:].rolling(window=15, min_periods=15).std()
        df_std.plot(label='Volatilité au Volume 15')
        plt.savefig('OutputFiles/volat_volub_15_' + methode + '_' + str(nom).replace(' ', '_') + '.png')

        plt.clf()

        plt.close()

    def graph_09(self, nom):

        print('Graph 09', nom)
        methode = 'close'
        data = Reader(Ticket(nom)).read()
        data.index = pd.DatetimeIndex([pd.to_datetime(x).tz_localize(None) for x in data.index])
        df_filled = data[['volume']].asfreq('D', method='ffill')
        df_returns = df_filled.pct_change()
        df_std = df_returns[-50:].rolling(window=7, min_periods=7).std()
        df_std.plot(label='Volatilité au Volume 7')
        plt.savefig('OutputFiles/volat_volub_7_' + methode + '_' + str(nom).replace(' ', '_') + '.png')

        plt.clf()
        plt.close()

    def graph_10(self, nom):
        print('Graph 10', nom)
        methode = 'close'
        data = Reader(Ticket(nom)).read()
        data.index = pd.DatetimeIndex([pd.to_datetime(x).tz_localize(None) for x in data.index])
        df_filled = data[['volume']].asfreq('D', method='ffill')
        df_returns = df_filled.pct_change()
        df_std = df_returns[-25:].rolling(window=3, min_periods=3).std()
        df_std.plot(label='Volatilité au Volume 3')
        plt.savefig('OutputFiles/volat_volub_3_' + methode + '_' + str(nom).replace(' ', '_') + '.png')
        del df_filled, df_returns, df_std
        plt.clf()
        plt.close()

    def graph_11(self, nom):
        print('Grap 11', nom)

        methode = 'close'
        data = Reader(Ticket(nom)).read()
        data.index = pd.DatetimeIndex([pd.to_datetime(x).tz_localize(None) for x in data.index])
        # Quantile-quantile plot
        figure = plt.figure(figsize=(8, 4))
        ax = figure.add_subplot(111)
        stats.probplot(data[-500:][methode].pct_change(periods=1).dropna(), dist='norm', plot=ax)
        # plt.show();
        plt.savefig('OutputFiles/quantile_' + methode + '_' + str(nom).replace(' ', '_') + '.png')
        # figur.clear()
        del figure, ax
        figure = ''
        ax = ''
        plt.clf()
        plt.close()

    def graph_12(self, nom):
        print('Graph 12', nom)

        methode = 'close'
        data = Reader(Ticket(nom)).read()
        data.index = pd.DatetimeIndex([pd.to_datetime(x).tz_localize(None) for x in data.index])
        mpf.plot(data.iloc[-500:], type='line', mav=(5, 10, 25), volume=True, title=STOCK_LEVEL + nom
                 , savefig='OutputFiles/mva_short_' + methode + '_' + str(nom).replace(' ', '_') + '.png')
        plt.close()

    def sim_monte_carlo(self, nom, methode='close'):
        print('Simulation Monte Carlo', nom)

        data = Reader(Ticket(nom)).read()[methode]

        log_returns = np.log(1 + data.pct_change())
        u = log_returns.mean()
        var = log_returns.var()
        drift = pd.Series(u - (0.5 * var))
        stdev = pd.Series(log_returns.std())

        t_intervals = 250
        iterations = 10

        daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))
        price_list = np.zeros_like(daily_returns)
        price_list[0] = 100
        for t in range(1, t_intervals):
            price_list[t] = price_list[t - 1] * daily_returns[t]

        # Plot Monte-Carlo Simulation
        plt.figure(figsize=(10, 6))
        plt.xlabel('Jours')
        plt.ylabel('Prix prévisionnel')
        plt.title(
            'Méthode de Monte-Carlo (calculs d\'aléas sur les 250 jours de marché à venir) pour {}'.format(nom))
        plt.plot(price_list);
        plt.savefig('OutputFiles/monaco_' + methode + '_' + str(nom).replace(' ', '_') + '.png')
        plt.clf()
        plt.close()
        del price_list, log_returns, u, var, drift, stdev, daily_returns, data
        gc.collect()


    def prophet(self, nom, methode='close'):
        print('Prédiction Meta', nom)
        data = Reader(Ticket(nom)).read()[[methode]]
        data.index = pd.DatetimeIndex([pd.to_datetime(x).tz_localize(None) for x in data.index])
        data.reset_index(inplace=True)
        data = data.rename(columns={'index': 'ds', methode: 'y'})
        m = Prophet()
        m.fit(data)
        future = m.make_future_dataframe(periods=365)
        future.tail()
        forecast = m.predict(future)
        forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
        m.plot(forecast).savefig('OutputFiles/prophet_' + methode + '_' + str(nom).replace(' ', '_') + '.png')
        m.plot_components(forecast).savefig('OutputFiles/prophet_components_' + methode + '_' + str(nom).replace(' ', '_') + '.png')