import pandas as pd

data = pd.read_csv('co.csv')

def fips(row):
    if row['county']=='Adams':
        return 8001
    elif row['county']=='Alamosa':
        return 8003
    elif row['county']=='Arapahoe':
        return 8005
    elif row['county']=='Archuleta':
        return 8007
    elif row['county']=='Baca':
        return 8009
    elif row['county']=='Bent':
        return 8011
    elif row['county']=='Boulder':
        return 8013
    elif row['county']=='Broomfield':
        return 8014
    elif row['county']=='Chaffee':
        return 8015
    elif row['county']=='Cheyenne':
        return 8017
    elif row['county']=='Clear':
        return 8019
    elif row['county']=='Conejos':
        return 8021
    elif row['county']=='Costilla':
        return 8023
    elif row['county']=='Crowley':
        return 8025
    elif row['county']=='Custer':
        return 8027
    elif row['county']=='Delta':
        return 8029
    elif row['county']=='Denver':
        return 8031
    elif row['county']=='Dolores':
        return 8033
    elif row['county']=='Douglas':
        return 8035
    elif row['county']=='Eagle':
        return 8037
    elif row['county']=='Elbert':
        return 8039
    elif row['county']=='El Paso':
        return 8041
    elif row['county']=='Fremont':
        return 8043
    elif row['county']=='Garfield':
        return 8045
    elif row['county']=='Gilpin':
        return 8047
    elif row['county']=='Grand':
        return 8049
    elif row['county']=='Gunnison':
        return 8051
    elif row['county']=='Hinsdale':
        return 8053
    elif row['county']=='Huerfano':
        return 8055
    elif row['county']=='Jackson':
        return 8057
    elif row['county']=='Jefferson':
        return 8059
    elif row['county']=='Kiowa':
        return 8061
    elif row['county']=='Kit Carson':
        return 8063
    elif row['county']=='Lake County':
        return 8065
    elif row['county']=='La Plata':
        return 8067
    elif row['county']=='Larimer':
        return 8069
    elif row['county']=='Las Animas':
        return 8071
    elif row['county']=='Lincoln':
        return 8073
    elif row['county']=='Logan':
        return 8075
    elif row['county']=='Mesa':
        return 8077
    elif row['county']=='Mineral':
        return 8079
    elif row['county']=='Moffat':
        return 8081
    elif row['county']=='Montezuma':
        return 8083
    elif row['county']=='Montrose':
        return 8085
    elif row['county']=='Morgan':
        return 8087
    elif row['county']=='Otero':
        return 8089
    elif row['county']=='Ouray':
        return 8091
    elif row['county']=='Park':
        return 8093
    elif row['county']=='Phillips':
        return 8095
    elif row['county']=='Pitkin':
        return 8097
    elif row['county']=='Prowers':
        return 8099
    elif row['county']=='Pueblo':
        return 8101
    elif row['county']=='Rio Blanco':
        return 8103
    elif row['county']=='Rio Grande':
        return 8105
    elif row['county']=='Routt':
        return 8107
    elif row['county']=='Saguache':
        return 8109
    elif row['county']=='San Juan':
        return 8111
    elif row['county']=='San Miguel':
        return 8113
    elif row['county']=='Sedgwick':
        return 8115
    elif row['county']=='Summit':
        return 8117
    elif row['county']=='Teller':
        return 8119
    elif row['county']=='Washington':
        return 8121
    elif row['county']=='Weld':
        return 8123
    elif row['county']=='Yuma':
        return 8125
    return fips

data['fips'] = data.apply(fips, axis=1)

data.to_csv('co.csv')