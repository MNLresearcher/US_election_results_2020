import pandas as pd

data = pd.read_csv('mn.csv')

def fips(row):
    if row['county']=='Aitkin':
        return 27001
    elif row['county']=='Anoka':
        return 27003
    elif row['county']=='Becker':
        return 27005
    elif row['county']=='Beltrami':
        return 27007
    elif row['county']=='Benton':
        return 27009
    elif row['county']=='Big Stone':
        return 27011
    elif row['county']=='Blue Earth':
        return 27013
    elif row['county']=='Brown':
        return 27015
    elif row['county']=='Carlton':
        return 27017
    elif row['county']=='Carver':
        return 27019
    elif row['county']=='Cass':
        return 27021
    elif row['county']=='Chippewa':
        return 27023
    elif row['county']=='Chisago':
        return 27025
    elif row['county']=='Clay':
        return 27027
    elif row['county']=='Clearwater':
        return 27029
    elif row['county']=='Cook':
        return 27031
    elif row['county']=='Cottonwood':
        return 27033
    elif row['county']=='Crow Wing':
        return 27035
    elif row['county']=='Dakota':
        return 27037
    elif row['county']=='Dodge':
        return 27039
    elif row['county']=='Douglas':
        return 27041
    elif row['county']=='Faribault':
        return 27043
    elif row['county']=='Fillmore':
        return 27045
    elif row['county']=='Freeborn':
        return 27047
    elif row['county']=='Goodhue':
        return 27049
    elif row['county']=='Grant':
        return 27051
    elif row['county']=='Hennepin':
        return 27053
    elif row['county']=='Houston':
        return 27055
    elif row['county']=='Hubbard':
        return 27057
    elif row['county']=='Isanti':
        return 27059
    elif row['county']=='Itasca':
        return 27061
    elif row['county']=='Jackson':
        return 27063
    elif row['county']=='Kanabec':
        return 27065
    elif row['county']=='Kandiyohi':
        return 27067
    elif row['county']=='Kittson':
        return 27069
    elif row['county']=='Koochiching':
        return 27071
    elif row['county']=='Lac Qui Parle':
        return 27073
    elif row['county']=='Lake':
        return 27075
    elif row['county']=='Lake Of The Woods':
        return 27077
    elif row['county']=='Le Sueur':
        return 27079
    elif row['county']=='Lincoln':
        return 27081
    elif row['county']=='Lyon':
        return 27083
    elif row['county']=='McLeod':
        return 27085
    elif row['county']=='Mahnomen':
        return 27087
    elif row['county']=='Marshall':
        return 27089
    elif row['county']=='Martin':
        return 27091
    elif row['county']=='Meeker':
        return 27093
    elif row['county']=='Mille Lacs':
        return 27095
    elif row['county']=='Morrison':
        return 27097
    elif row['county']=='Mower':
        return 27099
    elif row['county']=='Murray':
        return 27101
    elif row['county']=='Nicollet':
        return 27103
    elif row['county']=='Nobles':
        return 27105
    elif row['county']=='Norman':
        return 27107
    elif row['county']=='Olmsted':
        return 27109
    elif row['county']=='Otter Tail':
        return 27111
    elif row['county']=='Pennington':
        return 27113
    elif row['county']=='Pine':
        return 27115
    elif row['county']=='Pipestone':
        return 27117
    elif row['county']=='Polk':
        return 27119
    elif row['county']=='Pope':
        return 27121
    elif row['county']=='Ramsey':
        return 27123
    elif row['county']=='Red Lake':
        return 27125
    elif row['county']=='Redwood':
        return 27127
    elif row['county']=='Renville':
        return 27129
    elif row['county']=='Rice':
        return 27131
    elif row['county']=='Rock':
        return 27133
    elif row['county']=='Roseau':
        return 27135
    elif row['county']=='St. Louis':
        return 27137
    elif row['county']=='Scott':
        return 27139
    elif row['county']=='Sherburne':
        return 27141
    elif row['county']=='Sibley':
        return 27143
    elif row['county']=='Stearns':
        return 27145
    elif row['county']=='Steele':
        return 27147
    elif row['county']=='Stevens':
        return 27149
    elif row['county']=='Swift':
        return 27151
    elif row['county']=='Todd':
        return 27153
    elif row['county']=='Traverse':
        return 27155
    elif row['county']=='Wabasha':
        return 27157
    elif row['county']=='Wadena':
        return 27159
    elif row['county']=='Waseca':
        return 27161
    elif row['county']=='Washington':
        return 27163
    elif row['county']=='Watonwan':
        return 27165
    elif row['county']=='Wilkin':
        return 27167
    elif row['county']=='Winona':
        return 27169
    elif row['county']=='Wright':
        return 27171
    elif row['county']=='Yellow Medicine':
        return 27173
    return fips

data['fips'] = data.apply(fips, axis=1)

data.to_csv('mn.csv')