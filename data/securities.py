import json
def liste_indices():
    with open("data/indices.json", "r") as file:
        indices_dict = json.load(file)
    indices = ['Indices', indices_dict]
    return indices


def print_indices(indices):
    if indices[0] == 'Indices':
        str_describe = "Liste d'indices\n"
        for key, value in indices[1].items():
            str_describe += key + '\n'
    else:
        return "Ne sont pas des indices !"
    return str_describe


def liste_actions_pea():
    with open("data/pea.json", "r") as file:
        pea_dict = json.load(file)
    actions = ['Actions_pea', pea_dict]
    return actions


def print_actions_pea(actions_pea):
    if actions_pea[0] == 'Actions_pea':
        str_describe = "Liste d'actions pea\n"
        for key, value in actions_pea[1].items():
            str_describe += key + '\n'
    else:
        return "Ne sont pas des actions pea !"
    return str_describe


def liste_actions_pme():
    with open("data/pme.json") as file:
        pme = json.load(file)
    actions = ['Actions_pme', pme]
    return actions


def print_actions_pme(actions_pme):
    if actions_pme[0] == 'Actions_pme':
        str_describe = "Liste d'actions pme\n"
        for key, value in actions_pme[1].items():
            str_describe += key + '\n'
    else:
        return "Ne sont pas des actions pme !"
    return str_describe


def liste_cryptomonnaies():
    actions = ['Cryptomonnaies', {
        'Bitcoin EUR': 'BTC-EUR',
        'Ethereum EUR': 'ETH-EUR'
    }]
    return actions


def print_cryptomonnaies(cryptomonnaies):
    if cryptomonnaies[0] == 'Crypto_assets':
        str_describe = "Liste de cryptomonnaies\n"
        for key, value in cryptomonnaies[1].items():
            str_describe += key + '\n'
    else:
        return "Ne sont pas des cryptomonnaies !"
    return str_describe


def liste_actions_usa():
    actions = ['Actions_usa', {
        'Microsoft': 'MSFT'
    }]
    return actions


def print_actions_usa(actions_usa):
    if actions_usa[0] == 'Actions_usa':
        str_describe = "Liste d'actions usa\n"
        for key, value in actions_usa[1].items():
            str_describe += key + '\n'
    else:
        return "Ne sont pas des actions usa !"
    return str_describe


def liste_mutual_funds():
    with open("data/mutual_funds.json", "r") as file:
        mutual_funds_dict = json.load(file)
    actions = ['Mutual_funds', mutual_funds_dict]
    return actions


def print_mutual_funds(mutual_funds):
    if mutual_funds[0] == 'Mutual_funds':
        str_describe = "Liste fonds\n"
        for key, value in mutual_funds[1].items():
            str_describe += key + '\n'
    else:
        return "Ne sont pas des fonds !"
    return str_describe

def liste_assets():
    with open("data/assets.json", "r") as file:
        assets = json.load(file)
    assets = ["Assets", assets]
    return assets


def print_assets(mutual_funds):
    if mutual_funds[0] == 'Assets':
        str_describe = "Liste assets\n"
        for key, value in mutual_funds[1].items():
            str_describe += key + '\n'
    else:
        return "Ne sont pas des assets !"
    return str_describe


def liste_complete():
    dict_complete = {}
    dict_complete.update(liste_indices()[1])
    #dict_complete.update(liste_actions_pme()[1])
    #dict_complete.update(liste_actions_pea()[1])
    dict_complete.update(liste_mutual_funds()[1])
    #dict_complete.update(liste_actions_usa()[1])
    dict_complete.update(liste_assets()[1])
    dict_complete.update(liste_cryptomonnaies()[1])
    # Debug
    #dict_complete = {x: dict_complete[x] for it, x in enumerate(dict_complete.keys()) if it < 7}
    # Work with a selection of stocks
    with open("data/selection.txt", "r") as file:
        select_list = file.readlines()
        select_option = True if len(select_list) > 1 else False
        select_list = [name.replace("\n", "") for name in select_list]
    if select_option:
        select_complete = {str(name): dict_complete[str(name)] for name in select_list}
        select_complete.update(liste_indices()[1])
        del dict_complete
        dict_complete = select_complete

    return ['Liste_complete', dict_complete]
