import copy
import numpy as np
import pandas as pd
import requests
import re

from bs4 import BeautifulSoup
from data.securities import liste_complete, liste_indices
from decimal import Decimal
from objects.Clock import Clock
from objects.Reader import Reader
from objects.Ticket import Ticket
from joblib import Parallel, delayed
COLUMNS = ['Nom', 'Prix', 'Achat', 'Vente', 'Perf', 'Cac 40', '5 ans', '3 ans', '1er janv', 'Moy/ans', 'Mois',
               'Semaine', 'Séance', 'Avis', 'Prix 3 mois', 'Gain 3 mois', 'Rôle', 'Secteur', 'Activité']


class Analyse:

    def __init__(self, list_of_stocks=liste_complete()[1]):
        self.date_last_day = Clock()
        self.list_of_stocks = list_of_stocks
        self.avg = {str(): Decimal()}
        self.avg_d_log = {str(): Decimal()}
        self.avg_a_log = {str(): Decimal()}
        self.avg_d_dis = {str(): Decimal()}
        self.avg_a_dis = {str(): Decimal()}
        self.avg1 = {str(): Decimal()}
        self.avg3 = {str(): Decimal()}
        self.avg5 = {str(): Decimal()}
        self.avg10 = {str(): Decimal()}
        self.avg25j = {str(): Decimal()}
        self.avg5j = {str(): Decimal()}
        self.perf_shot = {str(): Decimal()}
        self.price = {str(): Decimal()}
        self.avg_cac40 = {str(): Decimal()}
        self.beta = {}
        self.risk = {}
        self.dictionnaire_beta = {}
        self.trans = {}
        self.df = pd.read_excel('tex/Strategie_PME.xlsx')
        
        self.synoptique = pd.DataFrame(columns=COLUMNS)

    def perf_du_dernier_jour(self, data, name):
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
        if data['close'].count() >= 250:
            self.avg1.update({name: round(((data['close'][-1] /
                                            data['close'][-250]) - 1) * 100, 2)})
        else:
            self.avg1.update({name: None})
        if data['close'].count() >= 750:
            self.avg3.update({name: round(((data['close'][-1] /
                                            data['close'][-750]) - 1) * 100, 2)})
        else:
            self.avg3.update({name: None})
        if data['close'].count() >= 1250:
            self.avg5.update({name: round(((data['close'][-1] /
                                            data['close'][-1250]) - 1) * 100, 2)})
        else:
            self.avg5.update({name: None})
        self.avg5j.update({name: round(((data['close'][-1] /
                                         data['close'][-5]) - 1) * 100, 2)})
        self.avg25j.update({name: round(((data['close'][-1] /
                                          data['close'][-25]) - 1) * 100, 2)})
        data_cac40 = Reader(Ticket('CAC 40')).read()
        try:
            self.avg_cac40.update({name: round(((data_cac40.at[data.index[-1], 'close'] /
                                                 data_cac40.at[data.index[0], 'close']) - 1) * 100, 2)})
        except Exception:
            self.avg_cac40.update({name: 0})
        self.risk.update({name: round((data['Log_ror'].std() * 250 ** 0.5) * 10, 1)})
        if data['Log_ror'].count() < 250:
            self.risk.update({name: 0})
        return data

    def beta_calc(self, nom):

        r = {}
        for nom_indice, objet in liste_indices()[1].items():
            data_stock = Reader(Ticket(nom)).read()
            data_indice = Reader(Ticket(nom_indice)).read()
            data_ac = pd.DataFrame({'stock': data_stock['close'],
                                    nom_indice: data_indice['close']})

            sec_returns_ac = np.log(data_ac / data_ac.shift(1))
            cov_ac = sec_returns_ac.cov() * 250

            cov_with_market_ac = cov_ac.loc['stock', nom_indice]

            market_var_ac = sec_returns_ac[nom_indice].var() * 250

            beta_temp_ac = cov_with_market_ac / market_var_ac
            r.update({nom_indice: beta_temp_ac})

        self.dictionnaire_beta.update({nom: r})

    def to_txt(self):
        fichier = open("reports_txt/performance_du_jour.txt", "w")
        Parallel(n_jobs=-1)(delayed(self.make_txt)(name, fichier) for name, mnemonic in self.list_of_stocks.items())

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

    def search_objectifs(self, page):
        predict_price = ''
        predict_gain = ''
        for line in page.find_all('p'):
            # Seeking Objectif paragraph
            search = re.search('Objectif de cours \d+ mois :', line.text)
            if search != None:
                res = line.text.replace('\n', '').split(' ')
                scores = [x for x in res if (x != '')]
                print(scores)
                predict_price = scores[6]
                predict_gain = scores[-1][:-1] if str.isnumeric(scores[-1][:-1].replace('.', '1')) else 0
        prediction = page.find('div', "c-median-gauge__tooltip")
        if prediction != None:
            return float(prediction.text), float(predict_price), float(predict_gain) / 100
        else:
            return '', '', ''

    def make_prediction(self, nom):
        """Search in a web page to follow objectives for a stock"""
        print(nom)
        url = self.df.loc[self.df['Nom'] == nom]['Boursorama'].iloc[
            0] if len(self.df.loc[self.df['Nom'] == nom][
                          'Boursorama'].values) > 0 else ''
        print(str(url)+'\n')
        url_exists = (str(url) != '') & (url != None) & (str(url) != 'nan')
        if url_exists:
            result = requests.get(url)
            page = BeautifulSoup(result.text, 'html.parser')

            # Searching for html paragraphs in webpage
            prediction, predict_price, predict_gain = self.search_objectifs(page)
            return prediction, predict_price, predict_gain
        else:
            return '', '', ''

    def to_xlsx(self):
        num = Parallel(n_jobs=-1)(
            delayed(self.make_xlsx)(name) for name, mnemonic in liste_complete()[1].items())
        for r in num:
            prediction, predict_price, predict_gain = self.make_prediction(r[0])
            self.synoptique = self.synoptique.append({COLUMNS[0]: r[0],  # Nom
                                                      COLUMNS[1]: r[1],  # Prix
                                                      COLUMNS[2]: r[2],  # Achat
                                                      COLUMNS[3]: r[3],  # Vente
                                                      COLUMNS[4]: r[4],  # Perf
                                                      COLUMNS[5]: r[13],  # Cac 40
                                                      COLUMNS[6]: r[5] if r[5] != None else 'N/A',  # 5 ans
                                                      COLUMNS[7]: r[6] if r[6] != None else 'N/A',  # 3 ans 
                                                      COLUMNS[8]: r[7] if r[7] != None else 'N/A',  # 1er janv 
                                                      COLUMNS[9]: r[8],  # Moy/ans
                                                      COLUMNS[10]: r[9],  # Mois
                                                      COLUMNS[11]: r[10],  # Semaine
                                                      COLUMNS[12]: r[11],  # Séance
                                                      COLUMNS[16]: 'Offensif' if r[12] > 0.75 else 'Défensif',  # Rôle
                                                      COLUMNS[17]: self.df.loc[self.df['Nom'] == r[0]]['Secteur'].iloc[
                                                          0] if len(self.df.loc[self.df['Nom'] == r[0]][
                                                                        'Secteur'].values) > 0 else '',  # Secteur
                                                      COLUMNS[18]:  
                                                          self.df.loc[self.df['Nom'] == r[0]]['Activité'].iloc[
                                                              0] if len(self.df.loc[self.df['Nom'] == r[0]][
                                                                            'Activité'].values) > 0 else '',  # Activité
                                                      
                                                      COLUMNS[13]: prediction,  # Avis
                                                      COLUMNS[14]: predict_price,  # Prix 3 mois
                                                      COLUMNS[15]: predict_gain  # Gain 3 mois
                                                      }, ignore_index=True)

        self.synoptique[COLUMNS[0]] = self.synoptique[COLUMNS[0]].astype('str')
        self.synoptique[COLUMNS[1]] = self.synoptique[COLUMNS[1]].astype('float')
        self.synoptique[COLUMNS[2]] = self.synoptique[COLUMNS[2]].astype('str')
        self.synoptique[COLUMNS[3]] = self.synoptique[COLUMNS[3]].astype('str')
        self.synoptique[COLUMNS[4]] = self.synoptique[COLUMNS[4]].astype('float')
        self.synoptique[COLUMNS[5]] = self.synoptique[COLUMNS[5]].astype('float')
        self.synoptique[COLUMNS[12]] = self.synoptique[COLUMNS[12]].astype('float')
        self.synoptique[COLUMNS[16]] = self.synoptique[COLUMNS[16]].astype('str')
        # Set Pandas engine to xlsxwriter
        writer = pd.ExcelWriter('reports_excel/' + str(Clock().date.date()) + '_synoptique.xlsx',
                                engine='xlsxwriter')

        # Convert the dataframe to an XlsxWriter Excel object.
        self.synoptique.to_excel(writer, sheet_name='Sheet1', index=True)

        # Get the xsxwriter objects from the dataframe writer object.
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']

        # Conditional formatting
        format0 = workbook.add_format({'align': 'center'})
        format1 = workbook.add_format({'num_format': '##,###.##€', 'align': 'center'})
        format2 = workbook.add_format({'num_format': '##,###.##%', 'align': 'center'})
        format3 = workbook.add_format({'font_color': 'green', 'align': 'center'})
        format4 = workbook.add_format({'font_color': 'red', 'align': 'center'})
        worksheet.set_column('A:A', 10, format0)
        # Nom
        worksheet.set_column('B:B', 37, format0)
        # Prix actuel
        worksheet.set_column('C:C', 9, format1)
        # Achat
        worksheet.set_column('D:D', 9, format0)
        # Vente
        worksheet.set_column('E:E', 9, format0)
        # Perf
        worksheet.set_column('F:F', 9, format2)
        # Cac 40
        worksheet.set_column('G:G', 12, format2)  # , format2)
        # 5 ans
        worksheet.set_column('H:H', 9, format2)
        # 3 ans
        worksheet.set_column('I:I', 9, format2)
        # 1er janv
        worksheet.set_column('J:J', 9, format2)
        # Moy
        worksheet.set_column('K:K', 9, format2)
        # Mois
        worksheet.set_column('L:L', 9, format2)
        # Semaine
        worksheet.set_column('M:M', 9, format2)
        # Perf du Jour
        worksheet.set_column('N:N', 9, format2)
        # Avis
        worksheet.set_column('O:O', 9)
        # Prix 3 mois
        worksheet.set_column('P:P', 9, format1)
        # Gain 3 mois
        worksheet.set_column('Q:Q', 9, format2)
        # Rôle
        worksheet.set_column('R:R', 9, format0)
        # Secteur
        worksheet.set_column('S:S', 9)
        # Activité
        worksheet.set_column('T:T', 19)
        worksheet.conditional_format('C2:C600', {'type': '3_color_scale'})
        worksheet.conditional_format('E2:E600', {'type': 'data_bar'})
        worksheet.conditional_format('F2:F600', {'type': 'data_bar'})
        worksheet.conditional_format('G2:G600', {'type': 'data_bar'})
        worksheet.conditional_format('H2:H600', {'type': 'data_bar'})
        worksheet.conditional_format('I2:I600', {'type': 'data_bar'})
        worksheet.conditional_format('J2:J600', {'type': 'data_bar'})
        worksheet.conditional_format('K2:K600', {'type': 'data_bar'})
        worksheet.conditional_format('L2:L600', {'type': 'data_bar'})
        worksheet.conditional_format('M2:M600', {'type': 'data_bar'})

        worksheet.conditional_format('N2:N600', {'type': 'data_bar'})
        worksheet.conditional_format('O2:O600', {'type': 'data_bar'})
        worksheet.conditional_format('P2:P600', {'type': 'data_bar'})
        worksheet.conditional_format('Q2:Q600', {'type': 'data_bar'})

        worksheet.conditional_format('R2:R600',
                                     {'type': 'text', 'criteria': 'containing', 'value': 'Offensif', 'format': format3})
        worksheet.conditional_format('R2:R600',
                                     {'type': 'text', 'criteria': 'containing', 'value': 'Défensif', 'format': format4})
        c = Clock()
        worksheet.write(0, 0, c.date)

        # Close worksheet
        workbook.close()

    def make_xlsx(self, name):
        data = Reader(Ticket(name)).read()
        data = self.perf_du_dernier_jour(data, name)
        self.beta_calc(name)
        r = [name,
             float(self.price[name]),
             pd.to_datetime(data.index[0]).date(),
             pd.to_datetime(data.index[-1]).date(),
             float(self.avg[name] / 100),
             float(self.avg5[name] / 100) if self.avg5[
                                                 name] is not None else 'N/A',
             float(self.avg3[name] / 100) if self.avg3[
                                                 name] is not None else 'N/A',
             float(self.avg1[name] / 100) if self.avg1[
                                                 name] is not None else 'N/A',
             float(self.avg_a_log[name] / 100),
             float(self.avg25j[name] / 100),
             float(self.avg5j[name] / 100),
             float(self.perf_shot[name] / 100),
             float(
                 self.dictionnaire_beta[name]['CAC 40']),
             float(self.avg_cac40[name] / 100)]

        return r
