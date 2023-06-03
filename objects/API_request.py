#!/usr/bin/env python

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import certifi
import json
import sys

from copy import deepcopy
from typing import Dict, List, Any

import pandas as pd

from data.securities import liste_complete, liste_indices
from objects.Reader import Reader
from objects.Ticket import Ticket
from objects.db_conn import write_to_db
from objects.db_conn import connexion

class API_request:

    def __init__(self):
        self.__apikey: str = ""
        self.result: Any[List, Dict]
        self.__urlapikey: str = "apikey=YOUR_API_KEY"

        self.service_name: list = []
        self.service_url: list = []
        self.service_dict: Dict = {}
        self.data = pd.DataFrame()

        with open("data/apikey.txt", "r") as f:
            content = f.readlines()
            for line in content:
                line = line.replace("\n", "")
                test = deepcopy(line)
                if str(test.find("apikey:")).isnumeric():
                    self.__apikey = line.replace("apikey:", "")
        self.__urlapikey = self.__urlapikey.replace("YOUR_API_KEY", self.__apikey)
        self.get_url()
        self.finstatlists: list = []
        self.set_finstatlist()

    def __str__(self):
        return " API key : " + self.__apikey + "\n" + str(self.service_name)

    @property
    def apikey(self):
        return self.__apikey

    @apikey.setter
    def apikey(self, key: str):
        self.__apikey = key

    @property
    def urlapikey(self):
        return self.__urlapikey

    @urlapikey.setter
    def urlapikey(self, key: str):
        self.__urlapikey = key

    def get_url(self):
        with open("data/schema.txt", "r") as f:
            content = f.readlines()
            for it, line in enumerate(content):
                line = line.replace("\n", "")
                if it % 2 == 0:
                    if line[0] == "#":
                        self.service_name.append(line[1:])
                elif it % 2 == 1:
                    self.service_url.append(line)
                else:
                    raise ArithmeticError("La liste ne contient pas des nombres")
        token = []
        for line in self.service_url:
            if "?" in str(line):
                token.append("&")
            else:
                token.append("?")
        self.service_dict = {self.service_name[x]: self.service_url[x] + token[x] + self.__urlapikey for x in
                             range(len(self.service_name))}

    def get_financialstatementlists(self):
        name = "financialStatementLists"
        name_nb = "data/financialStatementLists"
        self.get_jsonparsed_data(self.service_dict[name])
        with open(name_nb + ".txt", "w") as f:
            for statement in self.result:
                f.writelines(statement + "\n")

    def set_finstatlist(self):
        name_nb = "data/financialStatementLists"
        with open(name_nb + ".txt", "r") as f:
            self.finstatlists = f.readlines()
            self.finstatlists = [x.replace("\n", "") for x in self.finstatlists]

    def check_statement_presence(self, statement):
        if statement in self.finstatlists:
            return True
        else:
            return False

    def get_jsonparsed_data(self, url):
        response = urlopen(url, cafile=certifi.where())
        data = response.read().decode("utf-8")
        self.result = json.loads(data)

    def to_xlsx(self, nb_schema):
        liste = {name: mnemonic for name, mnemonic in liste_complete()[1].items() if
                 (isinstance(Reader(Ticket(name)).read(), pd.DataFrame))}
        liste = {name: mnemonic for name, mnemonic in liste.items() if (len(Reader(Ticket(name)).read()) > 74)}
        self.data = pd.DataFrame()
        n = 0
        for name, mnemonic in liste.items():
            if self.check_statement_presence(mnemonic):
                self.result = []
                url = self.service_dict[self.service_name[nb_schema]].replace("AAPL", mnemonic)
                print(url)
                self.get_jsonparsed_data(url)  # load result in self.result
                if self.result:
                    self.result[0]["name"] = name
                    df_cat = pd.DataFrame(self.result).set_index("symbol")
                    self.data = pd.concat([self.data, df_cat])

            else:
                n += 1
                print("Mnemonic pas dans l’API : " + name + ", " + mnemonic)
                continue
        print(str(n) + " n’ont pas été trouvés")

        conn = connexion()
        name = self.service_name[nb_schema]
        write_to_db(self.data, name, conn)
        self.data.to_csv("reports_excel/api_doc" + str(nb_schema) + ".csv")

