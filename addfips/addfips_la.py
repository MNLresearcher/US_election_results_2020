import pandas as pd

data = pd.read_csv('la.csv')

def fips(row):
    if row['county']=='Acadia':
        return 22001
    elif row['county']=='Allen':
        return 22003
    elif row['county']=='Ascension':
        return 22005
    elif row['county']=='Assumption':
        return 22007
    elif row['county']=='Avoyelles':
        return 22009
    elif row['county']=='Beauregard':
        return 22011
    elif row['county']=='Bienville':
        return 22013
    elif row['county']=='Bossier':
        return 22015
    elif row['county']=='Caddo':
        return 22017
    elif row['county']=='Calcasieu':
        return 22019
    elif row['county']=='Caldwell':
        return 22021
    elif row['county']=='Cameron':
        return 22023
    elif row['county']=='Catahoula':
        return 22025
    elif row['county']=='Claiborne':
        return 22027
    elif row['county']=='Concordia':
        return 22029
    elif row['county']=='De Soto':
        return 22031
    elif row['county']=='East Baton Rouge':
        return 22033
    elif row['county']=='East Carroll':
        return 22035
    elif row['county']=='East Feliciana':
        return 22037
    elif row['county']=='Evangeline':
        return 22039
    elif row['county']=='Franklin':
        return 22041
    elif row['county']=='Grant':
        return 22043
    elif row['county']=='Iberia':
        return 22045
    elif row['county']=='Iberville':
        return 22047
    elif row['county']=='Jackson':
        return 22049
    elif row['county']=='Jefferson':
        return 22051
    elif row['county']=='Jefferson Davis':
        return 22053
    elif row['county']=='Lafayette':
        return 22055
    elif row['county']=='Lafourche':
        return 22057
    elif row['county']=='LaSalle':
        return 22059
    elif row['county']=='Lincoln':
        return 22061
    elif row['county']=='Livingston':
        return 22063
    elif row['county']=='Madison':
        return 22065
    elif row['county']=='Morehouse':
        return 22067
    elif row['county']=='Natchitoches':
        return 22069
    elif row['county']=='Orleans':
        return 22071
    elif row['county']=='Ouachita':
        return 22073
    elif row['county']=='Plaquemines':
        return 22075
    elif row['county']=='Pointe Coupee':
        return 22077
    elif row['county']=='Rapides':
        return 22079
    elif row['county']=='Red River':
        return 22081
    elif row['county']=='Richland':
        return 22083
    elif row['county']=='Sabine':
        return 22085
    elif row['county']=='St. Bernard':
        return 22087
    elif row['county']=='St. Charles':
        return 22089
    elif row['county']=='St. Helena':
        return 22091
    elif row['county']=='St. James':
        return 22093
    elif row['county']=='St. John the Baptist':
        return 22095
    elif row['county']=='St. Landry':
        return 22097
    elif row['county']=='St. Martin':
        return 22099
    elif row['county']=='St. Mary':
        return 22101
    elif row['county']=='St. Tammany':
        return 22103
    elif row['county']=='Tangipahoa':
        return 22105
    elif row['county']=='Tensas':
        return 22107
    elif row['county']=='Terrebonne':
        return 22109
    elif row['county']=='Union':
        return 22111
    elif row['county']=='Vermilion':
        return 22113
    elif row['county']=='Vernon':
        return 22115
    elif row['county']=='Washington':
        return 22117
    elif row['county']=='Webster':
        return 22119
    elif row['county']=='West Baton Rouge':
        return 22121
    elif row['county']=='West Carroll':
        return 22123
    elif row['county']=='West Feliciana':
        return 22125
    elif row['county']=='Winn':
        return 22127
    return fips

data['fips'] = data.apply(fips, axis=1)

data.to_csv('la.csv')