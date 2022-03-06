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


def liste_actions_pea():
    actions = ['Actions_pea', {
        'ACCOR': 'AC.PA',
        'ADOCIA': 'ADOC.PA',
        'AEROPORTS PARIS': 'ADP.PA',
        'AIRBUS SE': 'AIR.PA',
        'AIR FRANCE KLM': 'AF.PA',
        'AIR LIQUIDE': 'AI.PA',  #
        'AKKA TECHNOLOGIES': 'AKA.PA',
        'AKWEL': 'AKW.PA',
        'ALSTOM': 'ALO.PA',
        'ALTAMIR': 'LTA.PA',
        'AMUNDI': 'AMUN.PA',
        'ALTAREA': 'ALTA.PA',
        'ALTEN': 'ATE.PA',
        'ARGAN': 'ARG.PA',
        'ARKEMA': 'AKE.PA',
        # 'ARTMARKET':'PRC.PA',
        # 'ASML':'ASME.F',
        'ATOS': 'ATO.PA',
        'AUBAY': 'AUB.PA',
        'AUDIOVALLEY RG': 'ALAVY.PA',  #
        'AXA': 'CS.PA',
        'AXWAY SOFTWARE': 'AXW.PA',  #
        'BENETEAU': 'BEN.PA',
        'BIC': 'BB.PA',
        'BIOMERIEUX': 'BIM.PA',
        # 'BLOCKCHAIN GROUP':'ALTBG.PA',
        # 'BLUESOLUTIONS':'BLUE.PA',
        'BNP PARIBAS': 'BNP.PA',
        # 'BOIRON':'BOI.PA',
        # 'BOLLORE':'BOL.PA',
        'BONDUELLE': 'BON.PA',
        'BOUYGUES': 'EN.PA',
        'BUREAU VERITAS': 'BVI.PA',
        'CAPGEMINI': 'CAP.PA',
        'CAPELLI': 'CAPLI.PA',
        'CARMILA': 'CARM.PA',
        'CARREFOUR': 'CA.PA',
        'CASINO GUICHARD': 'CO.PA',
        'CEGEDIM': 'CGM.PA',
        'CGG': 'CGG.PA',
        'CHRISTIAN DIOR': 'CDI.PA',
        'CIE ALPES': 'CDA.PA',
        'CNIM GROUPE SA': 'COM.PA',
        # 'CNP ASSURANCES':'CNP.PA',
        # 'COFACE':'COFA.PA',
        'COLAS': 'RE.PA',
        'COVIVIO': 'COV.PA',
        'CREDIT AGRICOLE': 'ACA.PA',
        'GROUPE CRIT': 'CEN.PA',
        'DANONE': 'BN.PA',
        'DASSAULT AVIATION': 'AM.PA',
        'DASSAULT SYSTEMES': 'DSY.PA',
        'DELTA PLUS GROUP': 'DLTA.PA',
        'DERICHEBOURG': 'DBG.PA',
        # 'DONTNOD':'ALDNE.PA',
        'EDENRED': 'EDEN.PA',
        'EDF': 'EDF.PA',
        'EIFFAGE': 'FGR.PA',
        'ELIOR GROUP': 'ELIOR.PA',
        'ENGIE': 'ENGI.PA',
        'ERAMET': 'ERA.PA',
        'ESSILORLUXOTTICA': 'EL.PA',
        'ESSO': 'ES.PA',
        'EURAZEO': 'RF.PA',
        'EUROFINS SCIENTIF': 'ERF.PA',
        'EURONEXT': 'ENX.PA',
        'EUROPACORP': 'ECP.PA',
        'EUROPCAR MOBILITY': 'EUCAR.PA',
        'EURO RESSOURCES': 'EUR.PA',
        'EUTELSAT COMMUNICA': 'ETL.PA',
        'FAURECIA': 'EO.PA',
        # 'FDJ':'FDJ.PA',
        #'FFP': 'FFP.PA',
        'FINANCIERE ODET': 'ODET.PA',
        'FNAC DARTY': 'FNAC.PA',
        'GAZTRANSPORT TECHN': 'GTT.PA',
        'GECINA': 'GFC.PA',
        # 'GENKYOTEX': 'GKTX.PA',
        'GLOBAL BIOENERGIES': 'ALGBE.PA',
        'GRAINES VOLTZ': 'GRVO.PA',
        'HERMES INTL': 'RMS.PA',
        'ICADE': 'ICAD.PA',
        'ID LOGISTICS': 'IDL.PA',
        'ILIAD': 'ILD.PA',
        'IMERYS': 'NK.PA',
        #'INGENICO GROUP': 'ING.PA',
        'IPSEN': 'IPN.PA',
        'IPSOS': 'IPS.PA',
        'JC DECAUX': 'DEC.PA',
        'KERING': 'KER.PA',
        'KLEPIERRE': 'LI.PA',
        'KORIAN': 'KORI.PA',
        #'LAFARGEHOLCIM LTD': 'LHN.PA',
        'LAGARDERE': 'MMB.PA',
        'LEGRAND': 'LR.PA',
        # 'LEXIBOOKLINGUIST':'ALLEX.PA',
        'LISI': 'FII.PA',
        "LOREAL": 'OR.PA',
        'LVMH': 'MC.PA',
        'MANITOU BF': 'MTU.PA',  #
        # 'MAURELPROM':'MAU.PA',
        'MERCIALYS': 'MERY.PA',
        'MERSEN': 'MRN.PA',
        'M6': 'MMT.PA',
        'MICHELIN': 'ML.PA',
        'NATIXIS': 'KN.PA',
        'NEOEN': 'NEOEN.PA',
        'NEXANS': 'NEX.PA',
        'NEXITY': 'NXI.PA',
        'NOKIA': 'NOKIA.PA',
        'OENEO': 'SBT.PA',
        #'ONXEO': 'ONXEO.PA',
        'ORANGE': 'ORA.PA',
        'ORPEA': 'ORP.PA',
        'PERNOD RICARD': 'RI.PA',
        #'PEUGEOT': 'UG.PA',
        "PIERRE VACANCES": 'VAC.PA',
        'PROLOGUEREGROUPE': 'PROL.PA',
        'PUBLICIS GROUPE': 'PUB.PA',
        'QUADIENT SA': 'QDT.PA',
        'RALLYE': 'RAL.PA',
        'RAMSAY GEN SANTE': 'GDS.PA',
        'REMY COINTREAU': 'RCO.PA',
        'RENAULT': 'RNO.PA',
        'REXEL': 'RXL.PA',
        'ROTHSCHILD CO': 'ROTH.PA',
        'RHI MAGNESITA': 'RHF.F',
        'RUBIS': 'RUI.PA',
        'SAFRAN': 'SAF.PA',
        'SAINT GOBAIN': 'SGO.PA',
        'SANOFI': 'SAN.PA',
        'SARTORIUS STEDIM': 'DIM.PA',
        'SAVENCIA': 'SAVE.PA',
        'SCHLUMBERGER': 'SLB.PA',
        'SCHNEIDER ELECTRIC': 'SU.PA',
        'SEB': 'SK.PA',
        'SOCIETE GENERALE': 'GLE.PA',
        'SODEXO': 'SW.PA',
        'SPIE': 'SPIE.PA',
        'STEF': 'STF.PA',
        'STMICROELECTRONICS': 'STM.PA',
        'SUEZ': 'SEV.PA',
        'SYNERGIE': 'SDG.PA',
        'TECHNIPFMC': 'FTI.PA',
        'TELEPERFORMANCE': 'TEP.PA',
        'TF1': 'TFI.PA',
        'THALES': 'HO.PA',
        'TOUR EIFFEL': 'EIFF.PA',
        'TRANSGENE': 'TNG.PA',
        'UBISOFT ENTERTAIN': 'UBI.PA',
        'VALEO': 'FR.PA',
        'VALLOUREC': 'VK.PA',
        'VEOLIA ENVIRONNEMENT': 'VIE.PA',
        'VETOQUINOL': 'VETO.PA',
        'VICAT': 'VCT.PA',
        'VILMORIN CIE': 'RIN.PA',
        'VINCI': 'DG.PA',
        'VIVENDI': 'VIV.PA',
        'WEDIA': 'ALWED.PA',
        'WENDEL': 'MF.PA',
        'WORLDLINE': 'WLN.PA',
        #'XPO LOGISTICS EURO': 'XPO.PA',
        'X-FAB SILICON FOUN': 'XFAB.PA'
    }]
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
    actions = ['Actions_pme', {
        'ABC ARBITRAGE': 'ABCA.PA',
        'AB SCIENCE': 'AB.PA',
        'ACTIA GROUP': 'ATI.PA',
        'ALBIOMA': 'ABIO.PA',
        #'ARCHOS': 'JXR.PA',
        'ARTMARKET-COM-SA': 'PRC.PA',
        'BIGBEN INTERACTIVE': 'BIG.PA',
        'CHARGEURS': 'CRI.PA',
        'CLARANOVA': 'CLA.PA',
        'DBV TECHNOLOGIES': 'DBV.PA',
        'EKINOPS': 'EKI.PA',
        #'EOS IMAGING': 'EOSI.PA',
        'ERYTECH PHARMA': 'ERYP.PA',
        'EXEL INDUSTRIES': 'EXE.PA',
        #'GECI INTERNATIONAL': 'GECP.PA',
        'GENFIT': 'GNFT.PA',
        'GETLINK SE': 'GET.PA',
        'GL EVENTS': 'GLO.PA',
        'GROUPE GORGE': 'GOE.PA',
        'HAULOTTE GROUP': 'PIG.PA',
        'HEXAOM': 'HEXA.PA',
        'INNATE PHARMA': 'IPH.PA',
        'INTERPARFUMS': 'ITP.PA',
        'JACQUET METALS': 'JCQ.PA',
        'LATECOERE': 'LAT.PA',
        'LAURENT PERRIER': 'LPE.PA',
        #'LE BELIER': 'BELI.PA',
        'LECTRA': 'LSS.PA',
        'LEXIBOOK': 'ALLEX.PA',
        'LNA SANTE': 'LNA.PA',
        'LUMIBIRD': 'LBIRD.PA',
        'MANUTAN INTL': 'MAN.PA',
        'MARIE BRIZARD WINE': 'MBWS.PA',
        'MAUNA KEA TECHN': 'MKEA.PA',
        'MAUREL PROM': 'MAU.PA',
        'METABOLIC EXPLORER': 'METEX.PA',
        'NANOBIOTIX': 'NANO.PA',
        'NICOX': 'COX.PA',
        'PHARMAGEST INTERAC': 'PHA.PA',
        'POXEL': 'POXEL.PA',
        'PLASTIC OMNIUM': 'POM.PA',
        'MAISONS MONDE': 'MDM.PA',
        'KAUFMAN BROAD': 'KOF.PA',
        'DEVOTEAM': 'DVT.PA',
        'COFACE': 'COFA.PA',
        'CELLECTIS': 'ALCLS.PA',
        'ALD': 'ALD.PA',
        'PSB INDUSTRIES': 'PSB.PA',
        'SECHE ENVIRONNEMEN': 'SCHP.PA',
        'SES IMAGOTAG SA': 'SESL.PA',
        'SOITEC': 'SOI.PA',
        'SOPRA STERIA GROUP': 'SOP.PA',
        'SQLI': 'SQI.PA',
        'SWORD GROUP': 'SWP.PA',
        'TFF GROUP': 'TFF.PA',
        'TRIGANO': 'TRI.PA',
        'VALNEVA SE': 'VLA.PA',
        'VERIMATRIX': 'VMX.PA',
        'VIRBAC SA': 'VIRP.PA',
        'VRANKEN POMMERY': 'VRAP.PA',
        'WAVESTONE': 'WAVE.PA'
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


def liste_actions_cic():
    actions = ['Actions_cic', {
        'CM-CIC DYNAMIQUE EUROPE (C)': '0P00000UNH.F',
        'CM-CIC DYNAMIQUE INTERNATIONAL (C)': '0P00000FMT.F',
        'CM-CIC ENTREPRENEURS EUROPE (C)': '0P00000Q4Z.F',
        'CM-CIC EQUILIBRE EUROPE (D)': '0P00000Q4D.F',
        'CM-CIC EQUILIBRE EUROPE (C)': '0P00001NLK.F',
        'CM-CIC EQUILIBRE INTERNATIONAL (RC)': '0P00000FOV.F',
        'CM-CIC EURO EQUITIES (C)': '0P00001PDS.F',
        'CM-CIC EURO MID CAP (C)': '0P00000FET.F',
        'CM-CIC EUROPE GROWTH (C)': '0P00001PDT.F',
        'CM-CIC EUROPE RENDEMENT (RC)': '0P0000Z816.F',
        'CM-CIC EUROPE RENDEMENT (RD)': '0P0000Z817.F',
        'CM-CIC EUROPE VALUE (C)': '0P00000FEJ.F',
        'CM-CIC FRANCE EQUITIES (C)': '0P00001PDW.F',
        'CM-CIC GLOBAL EMERGING MARKETS (RC)': '0P00000LT0.F',
        'CM-CIC GLOBAL LEADERS (RC)': '0P000152US.F',
        # 'CM-CIC HIGH YIELD 2021 (C)': '0P000163YV.F',
        'CM-CIC HIGH YIELD SHORT DURATION (C)': '0P00013MDM.F',
        'CM-CIC INDICIEL AMERIQUE 500 (C)': '0P00001NLH.F',
        'CM-CIC INDICIEL JAPON 225 (C)': '0P00008IB9.F',
        'CM-CIC MONE ISR (RC)': 'PRC.PA',
        'CM-CIC OBJECTIF ENVIRONNEMENT (C)': '0P00000FS2.F',
        'CM-CIC OBLI PAYS EMERGENTS (C)': '0P00001PDY.F',
        'CM-CIC PIERRE (C)': '0P00008Y84.F', 'CM-CIC PME-ETI ACTIONS (C)': '0P000125M7.F',
        'CM-CIC SILVER ECONOMIE (C)': '0P000175VV.F',
        'CM-CIC TEMPERE EUROPE (C)': '0P000123DC.F',
        'CM-CIC TEMPERE INTERNATIONAL (RC)': '0P00001NLL.F',
        'FLEXIGESTION 20-70 (C)': '0P00000Q7R.F',
        'FLEXIGESTION 50-100 (C)': '0P00000Q5G.F',
        'FLEXIGESTION PATRIMOINE (C)': '0P00005W9T.F',
        # Fonds responsable
        'CM-CIC OBJECTIF ENVIRONNEMENT': '0P00000FS2.F',
        'CM-CIC OBLI ISR': '0P0000Q1L3.F',
        'SOCIAL ACTIVE ACTIONS': '0P00016NIH.F',
        'SOCIAL ACTIVE OBLIGATIONS': '0P00016NIN.F',
        'SOCIAL ACTIVE MONETAIRE': '0P00016NIL.F',
        'SOCIAL ACTIVE DIVERSIFIE': '0P00016NII.F',
        'SOCIAL ACTIVE TEMPERE SOLIDAIRE': '0P00016NIO.F',
        'SOCIAL ACTIVE EQUILIBRE SOLIDAIRE': '0P00016NIK.F',
        'SOCIAL ACTIVE DYNAMIQUE SOLIDAIRE': '0P00016NIJ.F',
        'SOCIAL ACTIVE OBLI SOLIDAIRE': '0P00016NIM.F',
        # Fonds impact social
        'CM-CIC FRANCE EMPLOI': '0P00000FRO.F',
        # Épargne salariale
        'CM-CIC PERSPECTIVE ACTIONS EUROPE A': '0P0000U0J7.F',
        'CM-CIC PERSPECTIVE CONVICTION MONDE A': '0P0000U0ZP.F',
        'CM-CIC PERSPECTIVE OR ET MAT': '0P0000U0JA.F',
        'CM-CIC PERSPECTIVE PAYS EMERGENTS': '0P00016NKY.F',
        'CM-CIC PERSPECTIVE CONVICTION EUROPE A': '0P00016NKX.F',
        'CM-CIC PERSPECTIVE IMMO': '0P0000U0J9.F',
        'CM-CIC PERSPECTIVE CERTITUDE': '0P00016NKU.F',
        'CM-CIC PERSPECTIVE MONETAIRE B': '0P0000U0FQ.F',
        'CM-CIC PERSPECTIVE OBLI CT A': '0P0000U0FR.F',
        'CM-CIC PERSPECTIVE OBLI LT A': '0P0000U0FU.F',
        'CM-CIC PERSPECTIVE OBLI MT A': '0P0000U0FT.F',
        'CM-CIC STRATEGIE TRESO P': '0P00016NKV.F'
    }]
    return actions


def print_actions_cic(actions_cic):
    if actions_cic[0] == 'Actions_cic':
        str_describe = "Liste d'actions cic\n"
        for key, value in actions_cic[1].items():
            str_describe += key + '\n'
    else:
        return "Ne sont pas des actions cic !"
    return str_describe


def liste_complete():
    dict_complete = {}
    dict_complete.update(liste_indices()[1])
    dict_complete.update(liste_actions_pme()[1])
    dict_complete.update(liste_actions_pea()[1])
    dict_complete.update(liste_actions_cic()[1])
    dict_complete.update(liste_actions_usa()[1])
    dict_complete.update(liste_cryptomonnaies()[1])
    return ['Liste_complete', dict_complete]
