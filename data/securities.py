def liste_indices():
    indices = ['Indices', {
        'CAC 40': '^FCHI',
        'DAX': '^GDAXI',
        'Sbf 120': "^SBF120",
        'NASDAQ': '^IXIC',
        'Europe Developed Real Estate': 'IFEU',
        'MSCI WORLD INDEX FUTURES': 'MWL=F'
    }]
    return indices


def print_indices(indices):
    if indices[0] == 'Indices':
        str_describe = "Liste d'indices\n"
        for key, value in indices[1].items():
            str_describe += key + '\n'
    else:
        return "Ne sont pas des indices !"
    return str_describe


def liste_actions_pme():
    actions = ['Actions_pme', {
        'ABC ARBITRAGE': 'ABCA.PA',
        'AB SCIENCE': 'AB.PA'
    }]
    return actions


def print_actions_pme(actions_pme):
    if actions_pme[0] == 'Actions_pme':
        str_describe = "Liste d'actions pme\n"
        for key, value in actions_pme[1].items():
            str_describe += key + '\n'
    else:
        return "Ne sont pas des actions pme !"
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


def liste_complete():
    dict_complete = {}
    dict_complete.update(liste_indices()[1])
    dict_complete.update(liste_actions_pme()[1])
    dict_complete.update(liste_actions_usa()[1])
    return ['Liste_complete', dict_complete]