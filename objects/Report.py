#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:15:02 2020
Ce programme analyse et crée un rapport financier
@author: romain Boyrie
"""
# from data import listes
# import weakref
from data.securities import liste_complete
# import memory_profiler
import time
import matplotlib.pyplot as plt
import mplfinance as mpf
import seaborn as sns
from scipy import stats
import pandas as pd
import numpy as np
from scipy.stats import norm
from decimal import Decimal
# from data.listes import DATE_DE_DERNIERE_SEANCE
import os
import gc
from objects.latexFile import START, CORPS, CORPSSITE, CORPSWIKI, CORPSSECTION, CORPSLEREVENU, CORPSLAPOSTE, \
    CORPSBOURSORAMA, \
    CHAPITRE, DESCRIPTION, TABLE, END

# from objects.singleton import SingletonType
from objects.Ticket import Ticket
from objects.Reader import Reader
from objects.Clock import Clock
from objects.Analyse import Analyse
from joblib import Parallel, delayed


class PlotFinance:
    def __init__(self):
        pass

    def calc(self, data, nom, methode):
        # m1 = memory_profiler.memory_usage()
        t1 = time.perf_counter()
        # sns.set_style("darkgrid", {"axes.facecolor": ".9"})
        # top = plt.subplot2grid((4, 4), (0, 0), rowspan=3, colspan=4)
        # top.plot(data.index, data['close'], label='Prix à la Clôture')
        # plt.title("Cours de l'action {}".format(nom))
        # plt.legend(loc=2)
        # plt.gcf().set_size_inches(10, 10)
        # plt.savefig('OutputFiles/stockprice_' + methode + '_' + nom + '.png')

        # plt.show()
        # plt.clf()
        # plt.close()
        # p = mpf.plot(data.iloc[:,0:5], type='line',volume=False, title='Cours de l\'action ' + nom
        #            ,savefig='OutputFiles/stockprice_' + methode + '_' + nom + '.png')
        # plt.clf()
        # plt.close()
        # t2 = time.perf_counter()
        # m2 = memory_profiler.memory_usage()
        # time_diff = t2 - t1
        # mem_diff = m2[0] - m1[0]
        # print(f"It took {time_diff} Secs and {mem_diff} Mb to execute this p method")

        # m1 = memory_profiler.memory_usage()
        # t1 = time.perf_counter()

        # data.index = pd.Index([pd.to_datetime(x) for x in data.index])
        # q = mpf.plot(data.iloc[-500:, 0:5], type='line', mav=(12, 20, 50), volume=True,
        #             title='Cours de l\'action ' + nom
        #             , savefig='OutputFiles/mva_' + methode + '_' + nom + '.png')
        # plt.clf()
        # plt.close()
        # t2 = time.perf_counter()
        # m2 = memory_profiler.memory_usage()
        # time_diff = t2 - t1
        # mem_diff = m2[0] - m1[0]
        # print(f"It took {time_diff} Secs and {mem_diff} Mb to execute this q method")

        plt.close('all')
        # del data, nom, methode
        # data = ''
        # nom = ''
        # methode = ''
        # del data, nom, methode
        # gc.collect()
        # return 0


class Report:
    def __init__(self):  # , analyse):
        print('Report')
        self.data = Analyse()
        self.df = pd.read_excel('tex/Strategie_PME.xlsx')
        self.secteurs = pd.unique(self.df['Secteur'])
        # self.noms = {nom._nom: self.data.df.loc[self.data.df['Nom'] == nom._nom]['Secteur'].values for nom in
        #             self.data._portefeuille._liste_valeurs}

    def plot(self):
        # self.graph_pme('TRANSGENE')
        #Parallel(n_jobs=8)(
        #    delayed(self.graph_pme)(name) for name, mnemonic in liste_complete()[1].items())
        # self.graph_fonds()
        # Parallel(n_jobs=8)(
        #    delayed(self.graph_fonds)(name) for name, mnemonic in liste_complete()[1].items())
        # self.graph_indices()
        # self.graph_bitcoins()
        # self.graph_pea_vol()
        # self.graph_pea_quant()
        # self.graph_pea_cours()
        # self.sim_pea()
        #Parallel(n_jobs=8)(
         #   delayed(self.sim_pme)(name) for name, mnemonic in liste_complete()[1].items())
        # for name, mnemonic in liste_complete()[1].items():
        #    self.sim_pea(name)

        Parallel(n_jobs=8)(
            delayed(self.sim_pea)(name) for name, mnemonic in liste_complete()[1].items())
        # self.sim_fonds()
        # self.sim_indices()
        # self.sim_bitcoins()

    def compiler(self):
        os.chdir("reports_pdf")

        os.system("pdflatex " + str(Clock().date.date()) + '.tex')
        os.system("pdflatex " + str(Clock().date.date()) + '.tex')

    def create(self):  # (filename, noms, synthese, titre_chapitre, strategie):
        # os.chdir("reports_pdf")
        with open("reports_pdf/" + str(Clock().date.date()) + '.tex', 'w', encoding='utf8') as fout:
            fout.write(START.replace('DATE', str(Clock().date.date())))

            for secteur in self.secteurs:
                # print(secteur)
                # for nom in self.noms.keys():
                #   if (len(self.noms[nom]) == 0):
                #      print(nom)
                #     print(self.noms[nom])
                # if self.noms[nom][0] == secteur:
                #   print('ok')
                # noms=[]
                # for nom, value in self.noms.items():
                #     print(nom)
                #     print(value)
                #     if self.noms[nom][0] == secteur:
                #         noms.append(nom)
                noms = [x for x in liste_complete()[1] if x in self.df.loc[self.df['Secteur'] == secteur]['Nom'].values.ravel()]
                # if not secteur == 'Indice':
                fout.write(CHAPITRE.replace('TITRE', str(secteur)))
                for name in noms:

                    fout.write(CORPSSECTION.replace('TITRE', name))
                    try:
                        fout.write(CORPSSITE.replace('SITE',
                                                     self.df.loc[self.df['Nom'] == name]['Adresse'].values[
                                                         0]))
                    except:
                        pass
                    try:
                        fout.write(
                            CORPSWIKI.replace('WIKI', self.df.loc[self.df['Nom'] == name]['Wiki'].values[0]))
                    except:
                        pass
                    try:
                        fout.write(CORPSBOURSORAMA.replace('BOURSORAMA', self.df.loc[self.df['Nom'] == name][
                            'Boursorama'].values[0]))
                    except:
                        pass
                    try:
                        fout.write(CORPSLAPOSTE.replace('LAPOSTE',
                                                        self.df.loc[self.df['Nom'] == name]['Laposte'].values[
                                                            0]))
                    except:
                        pass
                    try:
                        fout.write(CORPSLEREVENU.replace('LEREVENU', self.df.loc[self.df['Nom'] == name][
                            'Lerevenu'].values[0]))
                    except:
                        pass
                    fout.write(CORPS.replace('TITRE', name))
                    self.data = Analyse()
                    if name in liste_complete()[1]:
                        data = Reader(Ticket(name)).read()
                        self.data.perf_du_dernier_jour(data, name)
                        fout.write(
                            TABLE.replace('PRIX', str(round(Decimal(self.data.price[name]), 2))).replace('TITRE',
                                                                                                         str(name))
                                .replace('ROR', str(round(Decimal(self.data.perf_shot[name]), 2)))
                                .replace('LOG', str(round(Decimal(self.data.avg_a_log[name]))))
                                .replace('CINQ', str(round(Decimal(self.data.avg5[name]), 2)) if self.data.avg5[
                                                                                                     name] is not None else str(0))
                                .replace('TROIS', str(round(Decimal(self.data.avg3[name]), 2)) if self.data.avg3[
                                                                                                      name] is not None else str(0))
                                .replace('UN', str(round(Decimal(self.data.avg1[name]), 2)) if self.data.avg1[
                                                                                                   name] is not None else str(0))
                                # .replace('10J',str(round(Decimal(synthese.loc[synthese['Nom'] == name]['10jours'].values[0]),2)))
                                # .replace('6J',str(round(Decimal(synthese.loc[synthese['Nom'] == name]['25jours'].values[0]),2)))
                                .replace('RISQUE', str(round(Decimal(self.data.risk[name]), 2))))

                    # if strategie.loc[strategie['Nom']==name].empty:
                    #    pass
                    # else:
                    try:
                        fout.write(DESCRIPTION.replace('ACTIVITE',
                                                       self.data.df.loc[self.data.df['Nom'] == name]['Activité'].values[
                                                           0]))
                    except:
                        pass
                    fout.write(r'\newpage')
            fout.write(END)

    def graph_pea_vol(self):
        print('Graphiques Vol')
        for nom, objet in self.data._portefeuille._actions_pea.items():
            m1 = memory_profiler.memory_usage()
            t1 = time.perf_counter()
            print('PEA', nom)

            methode = 'Adj Close'
            data = objet._donnees._panel[~objet._donnees._panel.index.duplicated()]

            # Volatility plot
            df_filled = data[[methode]].asfreq('D', method='ffill')
            df_returns = df_filled.pct_change()
            df_std = df_returns[-500:].rolling(window=30, min_periods=30).std()
            df_std.plot(label='Volatilité à la Clôture');
            plt.savefig('OutputFiles/volatility_' + methode + '_' + nom + '.png')
            plt.clf()
            plt.close('all')
            # del df_filled, df_returns, df_std, data
            # data = ''
            # df_filled = ''
            # df_returns = ''
            # df_std =''

            # del df_filled, df_returns, df_std, data
            # gc.collect()
            t2 = time.perf_counter()
            m2 = memory_profiler.memory_usage()
            time_diff = t2 - t1
            mem_diff = m2[0] - m1[0]
            print(f"It took {time_diff} Secs and {mem_diff} Mb to execute this pea vol method")

    def graph_pea_quant(self):
        print('Graphiques Quant')
        for nom, objet in self.data._portefeuille._actions_pea.items():
            m1 = memory_profiler.memory_usage()
            t1 = time.perf_counter()

            print('PEA quant : ', nom)

            # The top plot consisting of daily closing prices
            methode = 'Adj Close'
            data = objet._donnees._panel

            # Quantile-quantile plot
            figure = plt.figure(figsize=(8, 4))
            ax = figure.add_subplot(111)
            stats.probplot(data[-500:][methode].pct_change(periods=1).dropna(), dist='norm', plot=ax)
            plt.savefig('OutputFiles/quantile_' + methode + '_' + nom + '.png')
            plt.clf()
            plt.close('all')
            # del figure, ax, data
            # figure = ''
            # ax = ''
            # data = ''
            # del figure, ax, data
            # gc.collect()
            t2 = time.perf_counter()
            m2 = memory_profiler.memory_usage()
            time_diff = t2 - t1
            mem_diff = m2[0] - m1[0]
            print(f"It took {time_diff} Secs and {mem_diff} Mb to execute this pea quant method")

    def graph_pea_cours(self):
        print('Graphiques Cours')
        valeurs_iter = iter(self.data._portefeuille.pea_iter())

        for i in range(0, len(self.data._portefeuille._liste_pea)):
            objet = next(valeurs_iter)
            # for nom, objet in self.data._portefeuille._actions_pea.items():
            print('PEA cours: ', objet._nom)

            m1 = memory_profiler.memory_usage()
            t1 = time.perf_counter()
            p = PlotFinance()
            p.calc(objet._donnees._panel, objet._nom, 'Adj Close')
            t2 = time.perf_counter()
            m2 = memory_profiler.memory_usage()
            time_diff = t2 - t1
            mem_diff = m2[0] - m1[0]
            print(f"It took {time_diff} Secs and {mem_diff} Mb to execute this entire method")
            gc.collect()
        return 0

    def graph_pme(self, nom):
        # for nom, objet in self.data._portefeuille._actions_pme.items():
        print('PME', nom)
        # if isinstance(objet, Fonds):
        #     methode = 'Adj Close'
        #     # Plot the stock price
        #     data = objet._donnees._panel

        data = Reader(Ticket(nom)).read()
        data.index = pd.Index([pd.to_datetime(x) for x in data.index])
        methode = 'close'
        plt.figure(figsize=(10, 6))
        mpf.plot(data.iloc[:, 0:5], type='line', title='Cours de l\'action ' + nom
                 , savefig='OutputFiles/stockprice_' + methode + '_' + nom + '.png')
        mpf.plot(data.iloc[-500:, 0:5], type='line', mav=(12, 20, 50), volume=True, title='Cours de l\'action ' + nom
                 , savefig='OutputFiles/mva_' + methode + '_' + nom + '.png')
        #     del data
        # if isinstance(objet, Indice):
        #     methode = 'Adj Close'
        #     # Plot the stock price
        #     data = objet._donnees._panel
        #     plt.figure(figsize=(10,6))
        #     mpf.plot(data.iloc[:,0:5], type='line', title='Cours de l\'action ' + nom
        #              ,savefig='OutputFiles/stockprice_' + methode + '_' + nom + '.png')
        #     mpf.plot(data.iloc[-500:,0:5], type='line', mav=(12,20,50),volume=True, title='Cours de l\'action ' + nom
        #              ,savefig='OutputFiles/mva_' + methode + '_' + nom + '.png')
        #     del data
        # if isinstance(objet, Action)|isinstance(objet, Bitcoin) :
        # The top plot consisting of daily closing prices
        # print(nom, objet)
        # data = objet._donnees._panel
        # data = objet._donnees._panel[[methode,'Volume']]
        # data.index = pd.to_datetime(data.index)
        top = plt.subplot2grid((4, 4), (0, 0), rowspan=3, colspan=4)
        top.plot(data.index, data[methode], label='Prix à la Clôture')
        plt.title("Cours de l'action {}".format(nom))
        plt.legend(loc=2)
        # The bottom plot consisting of daily trading volume
        bottom = plt.subplot2grid((4, 4), (3, 0), rowspan=1, colspan=4)
        bottom.bar(data.index, data['volume'])
        plt.title("Volume de l'action {}".format(nom))
        plt.gcf().set_size_inches(10, 6)
        plt.subplots_adjust(hspace=0.75)
        plt.savefig('OutputFiles/stockprice_' + methode + '_' + nom + '.png')
        # Volatility plot
        df_filled = data[[methode]].asfreq('D', method='ffill')
        df_returns = df_filled.pct_change()
        df_std = df_returns[-500:].rolling(window=30, min_periods=30).std()
        df_std.plot(label='Volatilité à la Clôture')
        plt.savefig('OutputFiles/volatility_' + methode + '_' + nom + '.png')
        del df_filled, df_returns, df_std
        df_filled = ''
        df_returns = ''
        df_std = ''
        plt.clf()
        plt.close()
        # Quantile-quantile plot
        figure = plt.figure(figsize=(8, 4))
        ax = figure.add_subplot(111)
        stats.probplot(data[-500:][methode].pct_change(periods=1).dropna(), dist='norm', plot=ax)
        # plt.show();
        plt.savefig('OutputFiles/quantile_' + methode + '_' + nom + '.png')
        # figur.clear()
        del figure, ax
        figure = ''
        ax = ''
        plt.clf()
        plt.close()
        # mva plot data = data.iloc[:,0:5]
        mpf.plot(data.iloc[:, 0:5], type='line', volume=True, title='Cours de l\'action ' + nom
                 , savefig='OutputFiles/stockprice_' + methode + '_' + nom + '.png')
        mpf.plot(data.iloc[-500:, 0:5], type='line', mav=(12, 20, 50), volume=True, title='Cours de l\'action ' + nom
                 , savefig='OutputFiles/mva_' + methode + '_' + nom + '.png')
        plt.clf()
        plt.close()

        # valeurs_iter = iter(self.data._portefeuille.pea_iter())

        # m1 = memory_profiler.memory_usage()
        # t1 = time.perf_counter()
        p = PlotFinance()
        p.calc(Reader(Ticket(nom)).read(), nom, methode)
        # t2 = time.perf_counter()
        # m2 = memory_profiler.memory_usage()
        # time_diff = t2 - t1
        # mem_diff = m2[0] - m1[0]
        # print(f"It took {time_diff} Secs and {mem_diff} Mb to execute this pme entire method")

        # del data
        # data = ''
        # del df_filled, df_returns, df_std, figure, ax, data
        mpf.plot(data.iloc[-500:], type='line', mav=(5, 10, 25), volume=True, title='Cours de l\'action ' + nom
                 , savefig='OutputFiles/mva_short_' + methode + '_' + nom + '.png')
        # gc.collect()

    def graph_fonds(self, nom):
        # for nom, objet in self.data._portefeuille._titres_fonds.items():
        print('Fonds', nom)

        # The top plot consisting of daily closing prices
        methode = 'close'
        # print(nom, objet)
        data = Reader(Ticket(nom)).read()

        data.index = pd.Index([pd.to_datetime(x) for x in data.index])
        # Volatility plot
        df_filled = data[[methode]].asfreq('D', method='ffill')
        df_returns = df_filled.pct_change()
        df_std = df_returns[-500:].rolling(window=30, min_periods=30).std()
        df_std.plot(label='Volatilité à la Clôture');
        plt.savefig('OutputFiles/volatility_' + methode + '_' + nom + '.png')
        del df_filled, df_returns, df_std
        df_filled = ''
        df_returns = ''
        df_std = ''
        plt.clf()
        plt.close()
        # Quantile-quantile plot
        figure = plt.figure(figsize=(8, 4))
        ax = figure.add_subplot(111)
        stats.probplot(data[-500:][methode].pct_change(periods=1).dropna(), dist='norm', plot=ax)
        # plt.show();
        plt.savefig('OutputFiles/quantile_' + methode + '_' + nom + '.png')
        # figur.clear()
        del figure, ax
        figure = ''
        ax = ''
        plt.clf()
        plt.close()
        m1 = memory_profiler.memory_usage()
        t1 = time.perf_counter()
        p = PlotFinance()
        p.calc(objet._donnees._panel, objet._nom, 'Adj Close')
        t2 = time.perf_counter()
        m2 = memory_profiler.memory_usage()
        time_diff = t2 - t1
        mem_diff = m2[0] - m1[0]
        print(f"It took {time_diff} Secs and {mem_diff} Mb to execute this fonds cic entire method")

        del data
        data = ''
        del df_filled, df_returns, df_std, figure, ax, data
        gc.collect()

    def graph_indices(self):
        for nom, objet in self.data._portefeuille._titres_indices.items():
            print('Indices', nom)

            # The top plot consisting of daily closing prices
            methode = 'Adj Close'

            data = objet._donnees._panel[~objet._donnees._panel.index.duplicated()]

            # Volatility plot
            df_filled = data[[methode]].asfreq('D', method='ffill')
            df_returns = df_filled.pct_change()
            df_std = df_returns[-500:].rolling(window=30, min_periods=30).std()
            df_std.plot(label='Volatilité à la Clôture');
            plt.savefig('OutputFiles/volatility_' + methode + '_' + nom + '.png')
            del df_filled, df_returns, df_std
            df_filled = ''
            df_returns = ''
            df_std = ''
            plt.clf()
            plt.close()
            # Quantile-quantile plot
            figure = plt.figure(figsize=(8, 4))
            ax = figure.add_subplot(111)
            stats.probplot(data[-500:][methode].pct_change(periods=1).dropna(), dist='norm', plot=ax)
            # plt.show();
            plt.savefig('OutputFiles/quantile_' + methode + '_' + nom + '.png')
            # figur.clear()
            del figure, ax
            figure = ''
            ax = ''
            plt.clf()
            plt.close()
            plt.close()

            m1 = memory_profiler.memory_usage()
            t1 = time.perf_counter()
            p = PlotFinance()
            p.calc(objet._donnees._panel, objet._nom, 'Adj Close')
            t2 = time.perf_counter()
            m2 = memory_profiler.memory_usage()
            time_diff = t2 - t1
            mem_diff = m2[0] - m1[0]
            print(f"It took {time_diff} Secs and {mem_diff} Mb to execute this indices entire method")

            del data
            data = ''
            del df_filled, df_returns, df_std, figure, ax, data
            gc.collect()

    def graph_bitcoins(self):
        for nom, objet in self.data._portefeuille._titres_bitcoins.items():
            print('Bitcoins', nom)

            # The top plot consisting of daily closing prices
            methode = 'Adj Close'

            data = objet._donnees._panel[~objet._donnees._panel.index.duplicated()]

            # Volatility plot
            data = data[~data.index.duplicated()]
            # self.panel_filtre.update({nom:panel})
            df_filled = data[[methode]].asfreq('D', method='ffill')
            df_returns = df_filled.pct_change()
            df_std = df_returns[-500:].rolling(window=30, min_periods=30).std()
            df_std.plot(label='Volatilité à la Clôture');
            plt.savefig('OutputFiles/volatility_' + methode + '_' + nom + '.png')
            del df_filled, df_returns, df_std
            df_filled = ''
            df_returns = ''
            df_std = ''
            plt.clf()
            plt.close()
            # Quantile-quantile plot
            figure = plt.figure(figsize=(8, 4))
            ax = figure.add_subplot(111)
            stats.probplot(data[-500:][methode].pct_change(periods=1).dropna(), dist='norm', plot=ax)
            # plt.show();
            plt.savefig('OutputFiles/quantile_' + methode + '_' + nom + '.png')
            # figur.clear()
            del figure, ax
            figure = ''
            ax = ''
            plt.clf()
            plt.close()
            plt.close()

            m1 = memory_profiler.memory_usage()
            t1 = time.perf_counter()
            p = PlotFinance()
            p.calc(objet._donnees._panel, objet._nom, 'Adj Close')
            t2 = time.perf_counter()
            m2 = memory_profiler.memory_usage()
            time_diff = t2 - t1
            mem_diff = m2[0] - m1[0]
            print(f"It took {time_diff} Secs and {mem_diff} Mb to execute this bitcoin entire method")
            plt.clf()
            plt.close('all')

            del data
            data = ''
            del df_filled, df_returns, df_std, figure, ax, data
            gc.collect()

    def sim_pea(self, nom):
        # for nom, objet in self.data._portefeuille._actions_pea.items():
        data = Reader(Ticket(nom)).read()
        data.index = pd.Index([pd.to_datetime(x) for x in data.index])
        methode = 'close'
        print('Simulation Monte Carlo', nom)
        # methode = 'Adj Close'
        # data = objet._donnees._panel[methode]
        # data = self.data[methode]

        log_returns = np.log(1 + data.pct_change())
        u = log_returns.mean()
        var = log_returns.var()
        drift = pd.Series(u['close'] - (0.5 * var['close']))
        stdev = pd.Series(log_returns.std()['close'])

        t_intervals = 250
        iterations = 10
        #print(drift.values, stdev.values, u['close'], var['close'])
        daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))

        price_list = np.zeros_like(daily_returns)
        price_list[0] = 100
        for t in range(1, t_intervals):
            price_list[t] = price_list[t - 1] * daily_returns[t]
        # Recherche du potentiel plus haut et plus bas du Monaco

        # Plot Monte-Carlo Simulation
        plt.figure(figsize=(10, 6))
        plt.xlabel('Jours')
        plt.ylabel('Prix prévisionnel')
        # plt.title('Méthode de Monte-Carlo')
        plt.title(
            'Méthode de Monte-Carlo (calculs d\'aléas sur les 250 jours de marché à venir) pour {}'.format(nom))
        plt.plot(price_list);
        plt.savefig('OutputFiles/monaco_' + methode + '_' + nom + '.png')
        plt.clf()
        plt.close()
        del price_list, log_returns, u, var, drift, stdev, daily_returns, data
        price_list = ''
        log_returns = ''
        u = ''
        var = ''
        drift = ''
        stdev = ''
        daily_returns = ''
        data = ''
        del price_list, log_returns, u, var, drift, stdev, daily_returns, data
        gc.collect()

    def sim_pme(self, methode='close'):
        for nom, objet in self.data._portefeuille._actions_pme.items():
            print('Simulation Monte Carlo', nom)
            # methode = 'Adj Close'
            data = objet._donnees._panel[methode]
            # data = self.data[methode]

            log_returns = np.log(1 + data.pct_change())
            u = log_returns.mean()
            var = log_returns.var()
            drift = pd.Series(u - (0.5 * var))
            stdev = pd.Series(log_returns.std())

            t_intervals = 250
            iterations = 10

            daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))
            ## À la place du prix S0, je prends 100
            # S0 = data.iloc[-1]
            price_list = np.zeros_like(daily_returns)
            price_list[0] = 100
            for t in range(1, t_intervals):
                price_list[t] = price_list[t - 1] * daily_returns[t]

            # Plot Monte-Carlo Simulation
            plt.figure(figsize=(10, 6))
            plt.xlabel('Jours')
            plt.ylabel('Prix prévisionnel')
            # plt.title('Méthode de Monte-Carlo')
            plt.title(
                'Méthode de Monte-Carlo (calculs d\'aléas sur les 250 jours de marché à venir) pour {}'.format(nom))
            plt.plot(price_list);
            plt.savefig('OutputFiles/monaco_' + methode + '_' + nom + '.png')
            plt.clf()
            plt.close()
            del price_list, log_returns, u, var, drift, stdev, daily_returns, data
            price_list = ''
            log_returns = ''
            u = ''
            var = ''
            drift = ''
            stdev = ''
            daily_returns = ''
            data = ''
            del price_list, log_returns, u, var, drift, stdev, daily_returns, data
            gc.collect()

    def sim_fonds(self, methode='Adj Close'):
        for nom, objet in self.data._portefeuille._titres_fonds.items():
            print('Simulation Monte Carlo', nom)
            # methode = 'Adj Close'
            data = objet._donnees._panel[methode]
            # data = self.data[methode]

            log_returns = np.log(1 + data.pct_change())
            u = log_returns.mean()
            var = log_returns.var()
            drift = pd.Series(u - (0.5 * var))
            stdev = pd.Series(log_returns.std())

            t_intervals = 250
            iterations = 10

            daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))
            ## À la place du prix S0, je prends 100
            # S0 = data.iloc[-1]
            price_list = np.zeros_like(daily_returns)
            price_list[0] = 100
            for t in range(1, t_intervals):
                price_list[t] = price_list[t - 1] * daily_returns[t]

            # Plot Monte-Carlo Simulation
            plt.figure(figsize=(10, 6))
            plt.xlabel('Jours')
            plt.ylabel('Prix prévisionnel')
            # plt.title('Méthode de Monte-Carlo')
            plt.title(
                'Méthode de Monte-Carlo (calculs d\'aléas sur les 250 jours de marché à venir) pour {}'.format(nom))
            plt.plot(price_list);
            plt.savefig('OutputFiles/monaco_' + methode + '_' + nom + '.png')
            plt.clf()
            plt.close()
            del price_list, log_returns, u, var, drift, stdev, daily_returns, data
            price_list = ''
            log_returns = ''
            u = ''
            var = ''
            drift = ''
            stdev = ''
            daily_returns = ''
            data = ''
            del price_list, log_returns, u, var, drift, stdev, daily_returns, data
            gc.collect()

    def sim_indices(self, methode='Adj Close'):
        for nom, objet in self.data._portefeuille._titres_indices.items():
            print('Simulation Monte Carlo', nom)
            # methode = 'Adj Close'
            data = objet._donnees._panel[methode]
            # data = self.data[methode]

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
            # plt.title('Méthode de Monte-Carlo')
            plt.title(
                'Méthode de Monte-Carlo (calculs d\'aléas sur les 250 jours de marché à venir) pour {}'.format(nom))
            plt.plot(price_list);
            plt.savefig('OutputFiles/monaco_' + methode + '_' + nom + '.png')
            plt.clf()
            plt.close()
            del price_list, log_returns, u, var, drift, stdev, daily_returns, data
            price_list = ''
            log_returns = ''
            u = ''
            var = ''
            drift = ''
            stdev = ''
            daily_returns = ''
            data = ''
            del price_list, log_returns, u, var, drift, stdev, daily_returns, data
            gc.collect()

    def sim_bitcoins(self, methode='Adj Close'):
        for nom, objet in self.data._portefeuille._titres_bitcoins.items():
            print('Simulation Monte Carlo', nom)
            # methode = 'Adj Close'
            data = objet._donnees._panel[methode]

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
            # plt.title('Méthode de Monte-Carlo')
            plt.title(
                'Méthode de Monte-Carlo (calculs d\'aléas sur les 250 jours de marché à venir) pour {}'.format(nom))
            plt.plot(price_list);
            plt.savefig('OutputFiles/monaco_' + methode + '_' + nom + '.png')
            plt.clf()
            plt.close()
            del price_list, log_returns, u, var, drift, stdev, daily_returns, data
            price_list = ''
            log_returns = ''
            u = ''
            var = ''
            drift = ''
            stdev = ''
            daily_returns = ''
            data = ''
            del price_list, log_returns, u, var, drift, stdev, daily_returns, data
            gc.collect()
