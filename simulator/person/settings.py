# Calculated from PORDATA
# Óbitos de residentes em Portugal: total e por grupo etário
# Fontes de Dados: INE - Estatísticas de Óbitos
# Fonte: PORDATA
# Última actualização: 2022-08-11
PROBABILITY_AGE_DEAD = [0.009343999093649446,
                        0.002401098036385132,
                        0.0016018740990457509,
                        0.00621562783163168,
                        0.012624266302603677,
                        0.018019199190862853,
                        0.035019210840025704,
                        0.07012567619393069,
                        0.13534568433920807,
                        0.2616945603206215,
                        0.32945614170133053,
                        0.11385046632055708,
                        0.00423618380734386]
DEAD_AGES = [1, 2.5, 7.0, 14.5, 24.5, 34.5, 44.5, 54.5, 64.5, 74.5, 84.5, 94.5, 100]

# Probability sex
#População residente, média anual: total e por sexo
#Fontes de Dados: INE - Estimativas Anuais da População Residente
#Fonte: PORDATA
#Última actualização: 2022-08-22
PROBABILITY_SEX = [0.47887189157584076, 0.5211286008672906]
SEXS_TYPE = ['M', 'F']

# Probability of investing
#https://eco.sapo.pt/2021/05/25/portugueses-tem-mais-capacidade-de-poupar-mas-um-terco-teme-o-risco-da-bolsa/
PROBABILITY_INVEST = [0.3, 0.7]

# Probability of save money
#https://eco.sapo.pt/2021/05/25/portugueses-tem-mais-capacidade-de-poupar-mas-um-terco-teme-o-risco-da-bolsa/
PROBABILITY_SAVE = [0.62, 0.38]

# Fonte: ine.pt
#População residente (N.º) por Local de residência, Sexo e Níveis de ensino; Decenal - INE, Recenseamento da população e habitação - Censos 2021
# Última atualização destes dados: 12 de novembro de 2021
SCHOOL_LEVELS = ['Nenhum', 'Ensino básico',
                 'Ensino secundário e pós secundário', 'Ensino superior']

PROBABILITY_SCHOOL_LEVELS_MAN = [0.13108671, 0.50060697,
                                 0.22186797, 0.14643835]
PROBABILITY_SCHOOL_LEVELS_WOMAN = [0.14263173, 0.45415987,
                                   0.2041807 , 0.1990277 ]
# fonte: ine.pt
#Núcleos familiares (N.º) por Local de residência (à data dos Censos 2001) e Filhos; Decenal - INE, Recenseamento da população e habitação - Censos 2001
#Última atualização destes dados: 31 de maio de 2007
NUMBER_CHILDS = [0,1,2,3]
PROBABILITY_NUMBER_CHILDS = [0.31769804983801586,
                             0.36521046536438695,
                             0.2477616218936752,
                             0.06932986290392198]

# Fonte: https://www.dinheirovivo.pt/economia/40-da-populacao-ativa-preve-recorrer-ao-credito-12806316.html
PROBABILITY_CREDIT = [0.4,0.6]

#Fontes/Entidades: INE, PORDATA
#Última actualização: 2022-09-26
#População residente segundo os Censos: total e por estado civil
PROBABILITY_MARRIED = [0.460296, 0.539704]

#Ganho médio mensal dos trabalhadores por conta de outrem: total e por nível de escolaridade
#Fontes de Dados: GEP/MTSSS (até 2009) | GEE/MEc (2010 a 2012) | GEP/MSESS, MTSSS (a partir de 2013) - Quadros de Pessoal
#Fonte: PORDATA
#Última actualização: 2021-07-30
SALARY_BY_EDUCATION = {
    'Nenhum': 9671.8,
    'Ensino básico': 9671.8,
    'Ensino secundário e pós secundário': 12245.6,
    'Ensino superior': 18412.4
}

# linear regression from data from
#https://www.numbeo.com/cost-of-living/country_result.jsp?country=Portugal
LIVING_COST_PARAMETER_M = 470.40
LIVING_COST_PARAMETER_B = 90.7
RENT_T1_HOUSE_MEAN = 637.2
#Instituto Nacional de Estatística - Estatísticas da Saúde : 2020.
#Lisboa : INE, 2022.
#Disponível na www: <url:https://www.ine.pt/xurl/pub/436989156>.
#ISSN 2183-1637. ISBN 978-989-25-0599-2
# data for 2020
HEALTH_COST_PER_CAPITA_PUBLIC = 1345.6
HEALTH_COST_PER_CAPITA_PRIVATE = 6626.2

#Fontes/Entidades: INE, PORDATA
#Última actualização: 2022-08-22
#https://www.pordata.pt/portugal/despesa+corrente+em+cuidados+de+saude+per+capita-609
COST_OF_UNIVERSAL_HEALTH_SYSTEM_PER_CAPITA = 2285.9


