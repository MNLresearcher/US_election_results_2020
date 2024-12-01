import pandas as pd

data = pd.read_csv('id.csv')

def fips(row):
    if row['county']=='Ada':
        return 16001
    elif row['county']=='Adams':
        return 16003
    elif row['county']=='Bannock':
        return 16005
    elif row['county']=='Bear Lake':
        return 16007
    elif row['county']=='Benewah':
        return 16009
    elif row['county']=='Bingham':
        return 16011
    elif row['county']=='Blaine':
        return 16013
    elif row['county']=='Boise':
        return 16015
    elif row['county']=='Bonner':
        return 16017
    elif row['county']=='Bonneville':
        return 16019
    elif row['county']=='Boundary':
        return 16021
    elif row['county']=='Butte':
        return 16023
    elif row['county']=='Camas':
        return 16025
    elif row['county']=='Canyon':
        return 16027
    elif row['county']=='Caribou':
        return 16029
    elif row['county']=='Cassia':
        return 16031
    elif row['county']=='Clark':
        return 16033
    elif row['county']=='Clearwater':
        return 16035
    elif row['county']=='Custer':
        return 16037
    elif row['county']=='Elmore':
        return 16039
    elif row['county']=='Franklin':
        return 16041
    elif row['county']=='Fremont':
        return 16043
    elif row['county']=='Gem':
        return 16045
    elif row['county']=='Gooding':
        return 16047
    elif row['county']=='Idaho':
        return 16049
    elif row['county']=='Jefferson':
        return 16051
    elif row['county']=='Jerome':
        return 16053
    elif row['county']=='Kootenai':
        return 16055
    elif row['county']=='Latah':
        return 16057
    elif row['county']=='Lemhi':
        return 16059
    elif row['county']=='Lewis':
        return 16061
    elif row['county']=='Lincoln':
        return 16063
    elif row['county']=='Madison':
        return 16065
    elif row['county']=='Minidoka':
        return 16067
    elif row['county']=='Nez Perce':
        return 16069
    elif row['county']=='Oneida':
        return 16071
    elif row['county']=='Owyhee':
        return 16073
    elif row['county']=='Payette':
        return 16075
    elif row['county']=='Power':
        return 16077
    elif row['county']=='Shoshone':
        return 16079
    elif row['county']=='Teton':
        return 16081
    elif row['county']=='Twin Falls':
        return 16083
    elif row['county']=='Valley':
        return 16085
    elif row['county']=='Washington':
        return 16087
    return fips

data['fips'] = data.apply(fips, axis=1)

data.to_csv('id.csv')