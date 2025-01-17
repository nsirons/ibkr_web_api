'''
This file is generated by the get_exchange.py script.
Data is fetched from https://www.interactivebrokers.com/webrest/exchanges/search/
Updated on 2024-11-30 09:07:33.853655
'''
from collections import namedtuple
Exchange = namedtuple("Exchange", ["id", "name", "country_set", "country_code_set", "region_set", "product_types_set"])

AEB = Exchange(id="AEB", name="Amsterdamse Effectenbeurs", country_set={'Netherlands'}, country_code_set={'NL'}, region_set={'Europe'}, product_types_set={'Indices', 'Stocks', 'Structured Products'})
AEQLIT = Exchange(id="AEQLIT", name="Aequitas Neo", country_set={'Canada'}, country_code_set={'CA'}, region_set={'Americas'}, product_types_set={'Stocks', 'Warrants'})
AMEX = Exchange(id="AMEX", name="American Stock Exchange", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Indices', 'Stocks', 'Warrants', 'Options'})
APEXEN = Exchange(id="APEXEN", name="Apex - Euronext", country_set={'France', 'Netherlands', 'Portugal', 'Belgium'}, country_code_set={'BE', 'FR', 'PT', 'NL'}, region_set={'Europe'}, product_types_set={'Stocks'})
APEXIT = Exchange(id="APEXIT", name="Apex - Italy", country_set={'Italy'}, country_code_set={'IT'}, region_set={'Europe'}, product_types_set={'Stocks'})
AQEUAT = Exchange(id="AQEUAT", name="Aquis Exchange Europe - Austria", country_set={'Austria'}, country_code_set={'AT'}, region_set={'Europe'}, product_types_set={'Stocks'})
AQEUDE = Exchange(id="AQEUDE", name="Aquis Exchange Europe - Germany", country_set={'Germany'}, country_code_set={'DE'}, region_set={'Europe'}, product_types_set={'Stocks'})
AQEUDK = Exchange(id="AQEUDK", name="Aquis Exchange Europe - Denmark", country_set={'Denmark'}, country_code_set={'DK'}, region_set={'Europe'}, product_types_set={'Stocks'})
AQEUEN = Exchange(id="AQEUEN", name="Aquis Exchange Europe - Euronext", country_set={'France', 'Netherlands', 'Portugal', 'Belgium'}, country_code_set={'BE', 'FR', 'PT', 'NL'}, region_set={'Europe'}, product_types_set={'Stocks'})
AQEUES = Exchange(id="AQEUES", name="Aquis Exchange Europe - Spain", country_set={'Spain'}, country_code_set={'ES'}, region_set={'Europe'}, product_types_set={'Stocks'})
AQEUIT = Exchange(id="AQEUIT", name="Aquis Exchange Europe - Italy", country_set={'Italy'}, country_code_set={'IT'}, region_set={'Europe'}, product_types_set={'Stocks'})
AQXECH = Exchange(id="AQXECH", name="Aquis Exchange PLC - Switzerland", country_set={'Switzerland'}, country_code_set={'CH'}, region_set={'Europe'}, product_types_set={'Stocks'})
AQXEUK = Exchange(id="AQXEUK", name="Aquis Exchange PLC - United Kingdom", country_set={'United Kingdom'}, country_code_set={'GB'}, region_set={'Europe'}, product_types_set={'Stocks'})
ARCA = Exchange(id="ARCA", name="Archipelago", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Indices', 'Stocks', 'Warrants'})
ARCAEDGE = Exchange(id="ARCAEDGE", name="ARCAEDGE", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Stocks'})
BATECH = Exchange(id="BATECH", name="Cboe Europe Ltd. - BXE Order Book - Switzerland", country_set={'Switzerland'}, country_code_set={'CH'}, region_set={'Europe'}, product_types_set={'Stocks'})
BATEDE = Exchange(id="BATEDE", name="Cboe Europe Ltd. - BXE Order Book - Germany", country_set={'Germany'}, country_code_set={'DE'}, region_set={'Europe'}, product_types_set={'Stocks'})
BATEEN = Exchange(id="BATEEN", name="Cboe Europe Ltd. - BXE Order Book - Euronext", country_set={'France', 'Netherlands', 'Portugal', 'Belgium'}, country_code_set={'BE', 'FR', 'PT', 'NL'}, region_set={'Europe'}, product_types_set={'Stocks'})
BATEES = Exchange(id="BATEES", name="Cboe Europe Ltd. - BXE Order Book - Spain", country_set={'Spain'}, country_code_set={'ES'}, region_set={'Europe'}, product_types_set={'Stocks'})
BATEIT = Exchange(id="BATEIT", name="Cboe Europe Ltd. - BXE Order Book - Italy", country_set={'Italy'}, country_code_set={'IT'}, region_set={'Europe'}, product_types_set={'Stocks'})
BATEUK = Exchange(id="BATEUK", name="Cboe Europe Ltd. - BXE Order Book - UK", country_set={'United Kingdom'}, country_code_set={'GB'}, region_set={'Europe'}, product_types_set={'Stocks'})
BATS = Exchange(id="BATS", name="BATS Trading Inc", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Indices', 'Stocks', 'Warrants', 'Options'})
BELFOX = Exchange(id="BELFOX", name="Belgian Futures & Options Exchange", country_set={'Belgium'}, country_code_set={'BE'}, region_set={'Europe'}, product_types_set={'Indices', 'Options', 'Futures'})
BEX = Exchange(id="BEX", name="NASDAQ OMX BX", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Stocks', 'Warrants'})
BM = Exchange(id="BM", name="Bolsa de Madrid", country_set={'Spain'}, country_code_set={'ES'}, region_set={'Europe'}, product_types_set={'Indices', 'Stocks'})
BOVESPA = Exchange(id="BOVESPA", name="Bolsa de Valores de San Paulo", country_set={'Brazil'}, country_code_set={'BR'}, region_set={'Americas'}, product_types_set={'CFD'})
BOX = Exchange(id="BOX", name="Boston Option Exchange", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Options'})
BUX = Exchange(id="BUX", name="Budapest Stock Exchange", country_set={'Hungary'}, country_code_set={'HU'}, region_set={'Europe'}, product_types_set={'Stocks'})
BVL = Exchange(id="BVL", name="Lisbon Stock Exchange", country_set={'Portugal'}, country_code_set={'PT'}, region_set={'Europe'}, product_types_set={'Indices', 'Stocks'})
BVME = Exchange(id="BVME", name="Borsa Valori di Milano", country_set={'Italy'}, country_code_set={'IT'}, region_set={'Europe'}, product_types_set={'Indices', 'Stocks', 'Warrants'})
BVME_ETF = Exchange(id="BVME.ETF", name="Borsa Italiana ETF", country_set={'Italy'}, country_code_set={'IT'}, region_set={'Europe'}, product_types_set={'Stocks'})
BYX = Exchange(id="BYX", name="BATS Y Exchange", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Stocks', 'Warrants'})
CBOE = Exchange(id="CBOE", name="Chicago Board Options Exchange", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Indices', 'Stocks', 'Options'})
CBOE2 = Exchange(id="CBOE2", name="Chicago Board Options Exchange 2", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Indices', 'Options'})
CBOT = Exchange(id="CBOT", name="Chicago Board of Trade", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Indices', 'Options on Futures', 'Futures'})
CDE = Exchange(id="CDE", name="Canadian Derivatives Exchange (Bourse de Montreal)", country_set={'Canada'}, country_code_set={'CA'}, region_set={'Americas'}, product_types_set={'Indices', 'Options', 'Options on Futures', 'Futures'})
CEDX = Exchange(id="CEDX", name="CBOE Europe Derivatives", country_set={'Netherlands'}, country_code_set={'NL'}, region_set={'Europe'}, product_types_set={'Indices', 'Structured Products', 'Metals'})
CFE = Exchange(id="CFE", name="CBOE Futures Exchange", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Indices', 'Options on Futures', 'Futures'})
CFETAS = Exchange(id="CFETAS", name="Chicago Futures Exchange Trading At Settlement", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Futures'})
CHIXCH = Exchange(id="CHIXCH", name="Cboe Europe Ltd. - CXE Order Book - Swiss", country_set={'Switzerland'}, country_code_set={'CH'}, region_set={'Europe'}, product_types_set={'Stocks'})
CHIXDE = Exchange(id="CHIXDE", name="Cboe Europe Ltd. - CXE Order Book - Germany", country_set={'Germany'}, country_code_set={'DE'}, region_set={'Europe'}, product_types_set={'Stocks'})
CHIXEN = Exchange(id="CHIXEN", name="Cboe Europe Ltd. - CXE Order Book - Clearnet", country_set={'France', 'Netherlands', 'Portugal', 'Belgium'}, country_code_set={'BE', 'FR', 'PT', 'NL'}, region_set={'Europe'}, product_types_set={'Stocks'})
CHIXES = Exchange(id="CHIXES", name="Cboe Europe Ltd. - CXE Order Book - Spain", country_set={'Spain'}, country_code_set={'ES'}, region_set={'Europe'}, product_types_set={'Stocks'})
CHIXIT = Exchange(id="CHIXIT", name="Cboe Europe Ltd. - CXE Order Book - Italy", country_set={'Italy'}, country_code_set={'IT'}, region_set={'Europe'}, product_types_set={'Stocks'})
CHIXUK = Exchange(id="CHIXUK", name="Cboe Europe Ltd. - CXE Order Book - UK", country_set={'United Kingdom'}, country_code_set={'GB'}, region_set={'Europe'}, product_types_set={'Stocks'})
CHX = Exchange(id="CHX", name="Chicago Stock Exchange", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Stocks', 'Warrants'})
CME = Exchange(id="CME", name="Chicago Mercantile Exchange", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Indices', 'Options on Futures', 'Futures'})
COMEX = Exchange(id="COMEX", name="Commodity Exchange", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Indices', 'Options on Futures', 'Futures'})
CPH = Exchange(id="CPH", name="Copenhagen Stock Exchange", country_set={'Denmark'}, country_code_set={'DK'}, region_set={'Europe'}, product_types_set={'Stocks'})
DRCTEDGE = Exchange(id="DRCTEDGE", name="Direct Edge ECN LLC", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Stocks', 'Warrants'})
DXEAT = Exchange(id="DXEAT", name="Cboe Europe B.V. - DXE Order Book - Austria", country_set={'Austria'}, country_code_set={'AT'}, region_set={'Europe'}, product_types_set={'Stocks'})
DXEDE = Exchange(id="DXEDE", name="Cboe Europe B.V. - DXE Order Book - Germany", country_set={'Germany'}, country_code_set={'DE'}, region_set={'Europe'}, product_types_set={'Stocks'})
DXEDK = Exchange(id="DXEDK", name="Cboe Europe B.V. - DXE Order Book - Denmark", country_set={'Denmark'}, country_code_set={'DK'}, region_set={'Europe'}, product_types_set={'Stocks'})
DXEEN = Exchange(id="DXEEN", name="Cboe Europe B.V. - DXE Order Book - Euronext", country_set={'France', 'Netherlands', 'Portugal', 'Belgium'}, country_code_set={'BE', 'FR', 'PT', 'NL'}, region_set={'Europe'}, product_types_set={'Stocks'})
DXEES = Exchange(id="DXEES", name="Cboe Europe B.V. - DXE Order Book - Spain", country_set={'Spain'}, country_code_set={'ES'}, region_set={'Europe'}, product_types_set={'Stocks'})
DXEIT = Exchange(id="DXEIT", name="Cboe Europe B.V. - DXE Order Book - Italy", country_set={'Italy'}, country_code_set={'IT'}, region_set={'Europe'}, product_types_set={'Stocks'})
EBS = Exchange(id="EBS", name="Elektronische Boerse Schweiz", country_set={'Switzerland'}, country_code_set={'CH'}, region_set={'Europe'}, product_types_set={'Warrants', 'Structured Products', 'Indices', 'Bonds', 'Stocks'})
EDGEA = Exchange(id="EDGEA", name="Direct Edge ECN EDGEA", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Stocks', 'Warrants'})
EDGX = Exchange(id="EDGX", name="BATS Trading EDGX", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Indices', 'Stocks', 'Options'})
EMERALD = Exchange(id="EMERALD", name="MIAX EMERALD Exchange", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Options'})
ENDEX = Exchange(id="ENDEX", name="ICE Endex Futures", country_set={'Netherlands'}, country_code_set={'NL'}, region_set={'Europe'}, product_types_set={'Indices', 'Futures'})
ENEXT_BE = Exchange(id="ENEXT.BE", name="Euronext Belgium", country_set={'Belgium'}, country_code_set={'BE'}, region_set={'Europe'}, product_types_set={'Stocks', 'Structured Products'})
EUREX = Exchange(id="EUREX", name="EUREX", country_set={'Germany'}, country_code_set={'DE'}, region_set={'Europe'}, product_types_set={'Indices', 'Options', 'Options on Futures', 'Futures'})
EUREXUK = Exchange(id="EUREXUK", name="EUREX British Markets for LCH-Crest Clearing", country_set={'Germany'}, country_code_set={'DE'}, region_set={'Europe'}, product_types_set={'Options'})
EURONEXT = Exchange(id="EURONEXT", name="Euronext Regulated Bond Market", country_set={'France'}, country_code_set={'FR'}, region_set={'Europe'}, product_types_set={'Mutual Funds', 'Bonds'})
FTA = Exchange(id="FTA", name="Financiele Termijnmarkt Amsterdam", country_set={'Netherlands'}, country_code_set={'NL'}, region_set={'Europe'}, product_types_set={'Indices', 'Options', 'Futures'})
FUNDSERV = Exchange(id="FUNDSERV", name="Mutual Fund Holding Venue", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Mutual Funds'})
FWB = Exchange(id="FWB", name="Frankfurter Wertpapierboerse", country_set={'Germany'}, country_code_set={'DE'}, region_set={'Europe'}, product_types_set={'Stocks', 'Warrants', 'Structured Products'})
GEMINI = Exchange(id="GEMINI", name="ISE Gemini", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Options'})
GETTEX = Exchange(id="GETTEX", name="B��rse M��nchen AG", country_set={'Germany'}, country_code_set={'DE'}, region_set={'Europe'}, product_types_set={'Stocks', 'Warrants', 'Structured Products'})
IBBOND = Exchange(id="IBBOND", name="IB BOND", country_set={'United States'}, country_code_set={'US'}, region_set={'Global'}, product_types_set={'Bonds'})
IBCMDTY = Exchange(id="IBCMDTY", name="IB COMODITY", country_set={'United States'}, country_code_set={'US'}, region_set={'Global'}, product_types_set={'Metals'})
IBDESK = Exchange(id="IBDESK", name="IB Desk", country_set={'United States'}, country_code_set={'US'}, region_set={'Global'}, product_types_set={'Bonds'})
IBEOS = Exchange(id="IBEOS", name="IBKR Overnight Exchange", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Stocks'})
IBFX = Exchange(id="IBFX", name="Interactive Brokers Dealing System Pro", country_set={'United States'}, country_code_set={'US'}, region_set={'Global'}, product_types_set={'Currencies'})
IBIS = Exchange(id="IBIS", name="Integriertes Boersenhandels- und Informations-System", country_set={'Germany'}, country_code_set={'DE'}, region_set={'Europe'}, product_types_set={'Indices', 'Stocks'})
IBKRAM = Exchange(id="IBKRAM", name="Interactive Brokers Asset Management", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Indices'})
IBKRATS = Exchange(id="IBKRATS", name="Interactive Brokers ATS US Equities", country_set={'United States'}, country_code_set={'US'}, region_set={'Global'}, product_types_set={'Bonds'})
IBUSCFD = Exchange(id="IBUSCFD", name="IB CFD Dealing US", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'CFD'})
ICEEU = Exchange(id="ICEEU", name="ICE Futures Europe", country_set={'United Kingdom'}, country_code_set={'GB'}, region_set={'Europe'}, product_types_set={'Indices', 'Options', 'Options on Futures', 'Futures'})
ICEEUSOFT = Exchange(id="ICEEUSOFT", name="ICE Europe Soft Commodities", country_set={'United Kingdom'}, country_code_set={'GB'}, region_set={'Europe'}, product_types_set={'Indices', 'Options on Futures', 'Futures'})
ICEUS = Exchange(id="ICEUS", name="Ice Futures US Inc", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Futures'})
IDEALPRO = Exchange(id="IDEALPRO", name="Interactive Brokers Dealing System Pro", country_set={'United States'}, country_code_set={'US'}, region_set={'Global'}, product_types_set={'Currencies'})
IDEM = Exchange(id="IDEM", name="Italian Derivatives Market Milano", country_set={'Italy'}, country_code_set={'IT'}, region_set={'Europe'}, product_types_set={'Indices', 'Options', 'Futures'})
IEX = Exchange(id="IEX", name="Investors Exchange", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Stocks', 'Warrants'})
IPE = Exchange(id="IPE", name="International Petroleum Exchange", country_set={'United Kingdom'}, country_code_set={'GB'}, region_set={'Europe'}, product_types_set={'Indices', 'Options on Futures', 'Futures'})
ISE = Exchange(id="ISE", name="International Securities Exchange", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Indices', 'Stocks', 'Warrants', 'Options'})
ISED = Exchange(id="ISED", name="Irish Stock Exchange", country_set={'Ireland'}, country_code_set={'IE'}, region_set={'Europe'}, product_types_set={'Stocks'})
ISLAND = Exchange(id="ISLAND", name="ISLAND", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Stocks', 'Warrants'})
JSE = Exchange(id="JSE", name="Johannesburg Stock Exchange", country_set={'South Africa'}, country_code_set={'ZA'}, region_set={'Europe'}, product_types_set={'Stocks'})
LMEOTC = Exchange(id="LMEOTC", name="London Metals Exchange Internal OTC", country_set={'United Kingdom'}, country_code_set={'GB'}, region_set={'Europe'}, product_types_set={'Futures'})
LSE = Exchange(id="LSE", name="London Stock Exchange", country_set={'United Kingdom'}, country_code_set={'GB'}, region_set={'Europe'}, product_types_set={'Indices', 'Stocks'})
LSEETF = Exchange(id="LSEETF", name="ETF segment on LSE", country_set={'United Kingdom'}, country_code_set={'GB'}, region_set={'Europe'}, product_types_set={'Stocks'})
LSEIOB1 = Exchange(id="LSEIOB1", name="LSE-IOB 1", country_set={'United Kingdom'}, country_code_set={'GB'}, region_set={'Europe'}, product_types_set={'Stocks'})
LTSE = Exchange(id="LTSE", name="Long Term Stock Exchange", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Stocks', 'Warrants'})
MATIF = Exchange(id="MATIF", name="Marche A Terme d'Instruments Financiers", country_set={'France'}, country_code_set={'FR'}, region_set={'Europe'}, product_types_set={'Indices', 'Options on Futures', 'Futures'})
MEFFRV = Exchange(id="MEFFRV", name="Mercado Espanol de Futuros Financieros Renta Variable PROXY", country_set={'Spain'}, country_code_set={'ES'}, region_set={'Europe'}, product_types_set={'Indices', 'Options', 'Futures'})
MEMX = Exchange(id="MEMX", name="Members Exchange", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Stocks', 'Warrants', 'Options'})
MERCURY = Exchange(id="MERCURY", name="ISE Mercury", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Options'})
MEXDER = Exchange(id="MEXDER", name="Mercado Mexicano de Derivados", country_set={'Mexico'}, country_code_set={'MX'}, region_set={'Americas'}, product_types_set={'Options', 'Options on Futures', 'Futures'})
MEXI = Exchange(id="MEXI", name="Mexico Stock Exchange", country_set={'Mexico'}, country_code_set={'MX'}, region_set={'Americas'}, product_types_set={'Stocks'})
MIAX = Exchange(id="MIAX", name="Miami Options Exchange", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Options'})
MONEP = Exchange(id="MONEP", name="Marche des Opts Neg. de la Bourse de Paris", country_set={'France'}, country_code_set={'FR'}, region_set={'Europe'}, product_types_set={'Indices', 'Options', 'Futures'})
N_RIGA = Exchange(id="N.RIGA", name="NASDAQ Riga", country_set={'Latvia'}, country_code_set={'LV'}, region_set={'Europe'}, product_types_set={'Stocks'})
N_TALLINN = Exchange(id="N.TALLINN", name="Nasdaq Tallinn", country_set={'Estonia'}, country_code_set={'EE'}, region_set={'Europe'}, product_types_set={'Stocks'})
N_VILNIUS = Exchange(id="N.VILNIUS", name="AB NASDAQ Vilnius", country_set={'Lithuania'}, country_code_set={'LT'}, region_set={'Europe'}, product_types_set={'Stocks'})
NASDAQ = Exchange(id="NASDAQ", name="National Association of Security Dealers", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Indices', 'Stocks', 'Warrants'})
NASDAQBX = Exchange(id="NASDAQBX", name="NASDAQ OMX BX Options Exchange", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Options'})
NASDAQOM = Exchange(id="NASDAQOM", name="National Association of Security Dealers Options Market", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Options'})
NYBOT = Exchange(id="NYBOT", name="New York Board of Trade", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Indices', 'Options on Futures', 'Futures'})
NYMEX = Exchange(id="NYMEX", name="New York Mercantile Exchange", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Indices', 'Options on Futures', 'Futures'})
NYSE = Exchange(id="NYSE", name="New York Stock Exchange", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Indices', 'Stocks', 'Warrants', 'Bonds'})
NYSEFLOOR = Exchange(id="NYSEFLOOR", name="NYSE Floor", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Stocks', 'Warrants'})
NYSELIFFE = Exchange(id="NYSELIFFE", name="NYSE Liffe US", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Indices', 'Options on Futures', 'Futures'})
NYSENAT = Exchange(id="NYSENAT", name="NYSE National", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Stocks', 'Warrants'})
OMS = Exchange(id="OMS", name="Stockholm Options Market", country_set={'Sweden'}, country_code_set={'SE'}, region_set={'Europe'}, product_types_set={'Indices', 'Options', 'Futures'})
OMXNO = Exchange(id="OMXNO", name="Norwegian shares on OMX", country_set={'Sweden'}, country_code_set={'SE'}, region_set={'Europe'}, product_types_set={'Stocks'})
OSE = Exchange(id="OSE", name="Oslo Stock Exchange", country_set={'Norway'}, country_code_set={'NO'}, region_set={'Europe'}, product_types_set={'Indices', 'Stocks'})
OTCLNKECN = Exchange(id="OTCLNKECN", name="OTC Link ECN", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Stocks', 'Warrants'})
PEARL = Exchange(id="PEARL", name="MIAX PEARL Exchange", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Stocks', 'Warrants', 'Options'})
PHLX = Exchange(id="PHLX", name="Philadelphia Stock Exchange", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Indices', 'Stocks', 'Options'})
PINK = Exchange(id="PINK", name="Pink Sheets", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Stocks', 'Warrants'})
PRA = Exchange(id="PRA", name="Prague Stock Exchange", country_set={'Czech Republic'}, country_code_set={'CZ'}, region_set={'Europe'}, product_types_set={'Stocks'})
PSE = Exchange(id="PSE", name="Pacific Stock Exchange", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Indices', 'Options'})
PSX = Exchange(id="PSX", name="Nasdaq OMX PSX", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Stocks', 'Warrants'})
SBF = Exchange(id="SBF", name="Society des Bourses Francaises", country_set={'France'}, country_code_set={'FR'}, region_set={'Europe'}, product_types_set={'Indices', 'Stocks', 'Warrants', 'Structured Products'})
SFB = Exchange(id="SFB", name="Stockholm FondBors", country_set={'Sweden'}, country_code_set={'SE'}, region_set={'Europe'}, product_types_set={'Indices', 'Stocks'})
SGXCME = Exchange(id="SGXCME", name="Singapore Exchange - CME", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Futures'})
SMFE = Exchange(id="SMFE", name="The Small Exchange", country_set={'United States'}, country_code_set={'US'}, region_set={'Americas'}, product_types_set={'Options on Futures', 'Futures'})
SWB = Exchange(id="SWB", name="Stuttgart Wertpapierboerse", country_set={'Germany'}, country_code_set={'DE'}, region_set={'Europe'}, product_types_set={'Stocks', 'Warrants', 'Structured Products'})
TADAWUL = Exchange(id="TADAWUL", name="Saudi Exchange (Tadawul)", country_set={'Saudi Arabia'}, country_code_set={'SA'}, region_set={'Europe'}, product_types_set={'Stocks'})
TASE = Exchange(id="TASE", name="Tel Aviv Stock Exchange", country_set={'Israel'}, country_code_set={'IL'}, region_set={'Europe'}, product_types_set={'Stocks'})
TGATE = Exchange(id="TGATE", name="TradeGate", country_set={'Germany'}, country_code_set={'DE'}, region_set={'Europe'}, product_types_set={'Stocks'})
TGHEAT = Exchange(id="TGHEAT", name="Turquoise Global Holdings Europe B.V. - Austria", country_set={'Austria'}, country_code_set={'AT'}, region_set={'Europe'}, product_types_set={'Stocks'})
TGHEDE = Exchange(id="TGHEDE", name="Turquoise Global Holdings Europe B.V. - Germany", country_set={'Germany'}, country_code_set={'DE'}, region_set={'Europe'}, product_types_set={'Stocks'})
TGHEDK = Exchange(id="TGHEDK", name="Turquoise Global Holdings Europe B.V. - Denmark", country_set={'Denmark'}, country_code_set={'DK'}, region_set={'Europe'}, product_types_set={'Stocks'})
TGHEEN = Exchange(id="TGHEEN", name="Turquoise Global Holdings Europe B.V. - Euronext", country_set={'France', 'Netherlands', 'Portugal', 'Belgium'}, country_code_set={'BE', 'FR', 'PT', 'NL'}, region_set={'Europe'}, product_types_set={'Stocks'})
TGHEES = Exchange(id="TGHEES", name="Turquoise Global Holdings Europe B.V. - Spain", country_set={'Spain'}, country_code_set={'ES'}, region_set={'Europe'}, product_types_set={'Stocks'})
TGHEIT = Exchange(id="TGHEIT", name="Turquoise Global Holdings B.V. - Italy", country_set={'Italy'}, country_code_set={'IT'}, region_set={'Europe'}, product_types_set={'Stocks'})
TRADEWEB = Exchange(id="TRADEWEB", name="TradeWeb Corporate", country_set={'United States'}, country_code_set={'US'}, region_set={'Global'}, product_types_set={'Bonds'})
TRQXCH = Exchange(id="TRQXCH", name="Turquoise Europe Switzerland", country_set={'Switzerland'}, country_code_set={'CH'}, region_set={'Europe'}, product_types_set={'Stocks'})
TRQXDE = Exchange(id="TRQXDE", name="Turquoise Europe Germany", country_set={'Germany'}, country_code_set={'DE'}, region_set={'Europe'}, product_types_set={'Stocks'})
TRQXEN = Exchange(id="TRQXEN", name="Turquoise Europe EN", country_set={'France', 'Netherlands', 'Portugal', 'Belgium'}, country_code_set={'BE', 'FR', 'PT', 'NL'}, region_set={'Europe'}, product_types_set={'Stocks'})
TRQXES = Exchange(id="TRQXES", name="Turquoise Europe Spain", country_set={'Spain'}, country_code_set={'ES'}, region_set={'Europe'}, product_types_set={'Stocks'})
TRQXUK = Exchange(id="TRQXUK", name="Turquoise Europe United Kingdom", country_set={'United Kingdom'}, country_code_set={'GB'}, region_set={'Europe'}, product_types_set={'Stocks'})
TSE = Exchange(id="TSE", name="Toronto Stock Exchange", country_set={'Canada'}, country_code_set={'CA'}, region_set={'Americas'}, product_types_set={'Indices', 'Stocks', 'Warrants'})
VENTURE = Exchange(id="VENTURE", name="TSX Venture Exchange", country_set={'Canada'}, country_code_set={'CA'}, region_set={'Americas'}, product_types_set={'Stocks', 'Warrants'})
VSE = Exchange(id="VSE", name="Vienna Stock Exchange", country_set={'Austria'}, country_code_set={'AT'}, region_set={'Europe'}, product_types_set={'Indices', 'Stocks'})
WSE = Exchange(id="WSE", name="Warsaw Stock Exchange", country_set={'Poland'}, country_code_set={'PL'}, region_set={'Europe'}, product_types_set={'Stocks'})
ZEROHASH = Exchange(id="ZEROHASH", name="Zero Hash", country_set={'United States'}, country_code_set={'US'}, region_set={'Global'}, product_types_set={'Cryptocurrency'})
