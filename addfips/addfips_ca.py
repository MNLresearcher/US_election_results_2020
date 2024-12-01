import pandas as pd

data = pd.read_csv('ca.csv')

def fips(row):
    if row['county']=='Alameda':
        return 6001
    elif row['county']=='Alpine':
        return 6003
    elif row['county']=='Amador':
        return 6005
    elif row['county']=='Butte':
        return 6007
    elif row['county']=='Calaveras':
        return 6009
    elif row['county']=='Colusa':
        return 6011
    elif row['county']=='Contra Costa':
        return 6013
    elif row['county']=='Del Norte':
        return 6015
    elif row['county']=='El Dorado':
        return 6017
    elif row['county']=='Fresno':
        return 6019
    elif row['county']=='Glenn':
        return 6021
    elif row['county']=='Humboldt':
        return 6023
    elif row['county']=='Imperial':
        return 6025
    elif row['county']=='Inyo':
        return 6027
    elif row['county']=='Kern':
        return 6029
    elif row['county']=='Kings':
        return 6031
    elif row['county']=='Lake':
        return 6033
    elif row['county']=='Lassen':
        return 6035
    elif row['county']=='Los Angeles':
        return 6037
    elif row['county']=='Madera':
        return 6039
    elif row['county']=='Marin':
        return 6041
    elif row['county']=='Mariposa':
        return 6043
    elif row['county']=='Mendocino':
        return 6045
    elif row['county']=='Merced':
        return 6047
    elif row['county']=='Modoc':
        return 6049
    elif row['county']=='Mono':
        return 6051
    elif row['county']=='Monterey':
        return 6053
    elif row['county']=='Napa':
        return 6055
    elif row['county']=='Nevada':
        return 6057
    elif row['county']=='Orange':
        return 6059
    elif row['county']=='Placer':
        return 6061
    elif row['county']=='Plumas':
        return 6063
    elif row['county']=='Riverside':
        return 6065
    elif row['county']=='Sacramento':
        return 6067
    elif row['county']=='San Benito':
        return 6069
    elif row['county']=='San Bernardino':
        return 6071
    elif row['county']=='San Diego':
        return 6073
    elif row['county']=='San Francisco':
        return 6075
    elif row['county']=='San Joaquin':
        return 6077
    elif row['county']=='San Luis Obispo':
        return 6079
    elif row['county']=='San Mateo':
        return 6081
    elif row['county']=='Santa Barbara':
        return 6083
    elif row['county']=='Santa Clara':
        return 6085
    elif row['county']=='Santa Cruz':
        return 6087
    elif row['county']=='Shasta':
        return 6089
    elif row['county']=='Sierra':
        return 6091
    elif row['county']=='Siskiyou':
        return 6093
    elif row['county']=='Solano':
        return 6095
    elif row['county']=='Sonoma':
        return 6097
    elif row['county']=='Stanislaus':
        return 6099
    elif row['county']=='Sutter':
        return 6101
    elif row['county']=='Tehama':
        return 6103
    elif row['county']=='Trinity':
        return 6105
    elif row['county']=='Tulare':
        return 6107
    elif row['county']=='Tuolumne':
        return 6109
    elif row['county']=='Ventura':
        return 6111
    elif row['county']=='Yolo':
        return 6113
    elif row['county']=='Yuba':
        return 6115
    return fips

data['fips'] = data.apply(fips, axis=1)

data.to_csv('ca.csv')