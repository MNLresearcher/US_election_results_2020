import pandas as pd

data = pd.read_csv('va.csv')

def fips(row):
    if row['county']=='Accomack':
        return 51001
    elif row['county']=='Albermarle':
        return 51003
    elif row['county']=='Alleghany':
        return 51005
    elif row['county']=='Amelia':
        return 51007
    elif row['county']=='Amherst':
        return 51009
    elif row['county']=='Appomattox':
        return 51011
    elif row['county']=='Arlington':
        return 51013
    elif row['county']=='Augusta':
        return 51015
    elif row['county']=='Bath':
        return 51017
    elif row['county']=='Bedford':
        return 51019
    elif row['county']=='Bland':
        return 51021
    elif row['county']=='Botetourt':
        return 51023
    elif row['county']=='Brunswick':
        return 51025
    elif row['county']=='Buchanan':
        return 51027
    elif row['county']=='Buckingham':
        return 51029
    elif row['county']=='Campbell':
        return 51031
    elif row['county']=='Caroline':
        return 51033
    elif row['county']=='Carroll':
        return 51035
    elif row['county']=='Charles':
        return 51036
    elif row['county']=='Charlotte':
        return 51037
    elif row['county']=='Chesterfield':
        return 51041
    elif row['county']=='Clarke':
        return 51043
    elif row['county']=='Craig':
        return 51045
    elif row['county']=='Culpeper':
        return 51047
    elif row['county']=='Cumberland':
        return 51049
    elif row['county']=='Dickenson':
        return 51051
    elif row['county']=='Dinwiddie':
        return 51053
    elif row['county']=='Essex':
        return 51057
    elif row['county']=='Fairfax':
        return 51059
    elif row['county']=='Fauquier':
        return 51061
    elif row['county']=='Floyd':
        return 51063
    elif row['county']=='Fluvanna':
        return 51065
    elif row['county']=='Franklin':
        return 51067
    elif row['county']=='Frederick':
        return 51069
    elif row['county']=='Giles':
        return 51071
    elif row['county']=='Gloucester':
        return 51073
    elif row['county']=='Goochland':
        return 51075
    elif row['county']=='Grayson':
        return 51077
    elif row['county']=='Greene':
        return 51079
    elif row['county']=='Greensville':
        return 51081
    elif row['county']=='Halifax':
        return 51083
    elif row['county']=='Hanover':
        return 51085
    elif row['county']=='Henrico':
        return 51087
    elif row['county']=='Henry':
        return 51089
    elif row['county']=='Highland':
        return 51091
    elif row['county']=='Isle of Wight':
        return 51093
    elif row['county']=='James City':
        return 51095
    elif row['county']=='King and Queen':
        return 51097
    elif row['county']=='King George':
        return 51099
    elif row['county']=='King William':
        return 51101
    elif row['county']=='Lancaster':
        return 51103
    elif row['county']=='Lee':
        return 51105
    elif row['county']=='Loudoun':
        return 51107
    elif row['county']=='Louisa':
        return 51109
    elif row['county']=='Lunenburg':
        return 51111
    elif row['county']=='Madison':
        return 51113
    elif row['county']=='Mathews':
        return 51115
    elif row['county']=='Mecklenburg':
        return 51117
    elif row['county']=='Middlesex':
        return 51119
    elif row['county']=='Montgomery':
        return 51121
    elif row['county']=='Nelson':
        return 51125
    elif row['county']=='New Kent':
        return 51127
    elif row['county']=='Northampton':
        return 51131
    elif row['county']=='Northumberland':
        return 51133
    elif row['county']=='Nottoway':
        return 51135
    elif row['county']=='Orange':
        return 51137
    elif row['county']=='Page':
        return 51139
    elif row['county']=='Patrick':
        return 51141
    elif row['county']=='Pittsylvania':
        return 51143
    elif row['county']=='Powhatan':
        return 51145
    elif row['county']=='Prince Edward':
        return 51147
    elif row['county']=='Prince George':
        return 51149
    elif row['county']=='Prince William':
        return 51153
    elif row['county']=='Pulaski':
        return 51155
    elif row['county']=='Rappahannock':
        return 51157
    elif row['county']=='Richmond':
        return 51159
    elif row['county']=='Roanoke':
        return 51161
    elif row['county']=='Rockbridge':
        return 51163
    elif row['county']=='Rockingham':
        return 51165
    elif row['county']=='Russell':
        return 51167
    elif row['county']=='Scott':
        return 51169
    elif row['county']=='Shenandoah':
        return 51171
    elif row['county']=='Smyth':
        return 51173
    elif row['county']=='Southampton':
        return 51175
    elif row['county']=='Spotsylvania':
        return 51177
    elif row['county']=='Stafford':
        return 51179
    elif row['county']=='Surry':
        return 51181
    elif row['county']=='Sussex':
        return 51183
    elif row['county']=='Tazewell':
        return 51185
    elif row['county']=='Warren':
        return 51187
    elif row['county']=='Washington':
        return 51191
    elif row['county']== 'Westmoreland':
        return 51193
    elif row['county']== 'Wise':
        return 51195
    elif row['county']== 'Wythe':
        return 51197
    elif row['county']== 'York':
        return 51199
    elif row['county']== 'Alexandria City':
        return 51510
    elif row['county']== 'Bristol City':
        return 51520
    elif row['county']== 'Buena Vista City':
        return 51530
    elif row['county']== 'Charlottesville City':
        return 51540
    elif row['county']== 'Chesapeake City':
        return 51550
    elif row['county']== 'Colonial Heights City':
        return 51570
    elif row['county']== 'Covington City':
        return 51580
    elif row['county']== 'Danville City':
        return 51590
    elif row['county']== 'Emporia City':
        return 51595
    elif row['county']== 'Fairfax City':
        return 51600
    elif row['county']== 'Falls Church City':
        return 51610
    elif row['county']== 'Franklin City':
        return 51620
    elif row['county']== 'Fredericksburg City':
        return 51630
    elif row['county']== 'Galax City':
        return 51640
    elif row['county']== 'Hampton City':
        return 51650
    elif row['county']== 'Harrisonburg City':
        return 51660
    elif row['county']== 'Hopewell City':
        return 51670
    elif row['county']== 'Lexington City':
        return 51678
    elif row['county']== 'Lynchburg City':
        return 51680
    elif row['county']== 'Manassas City':
        return 51683
    elif row['county']== 'Manassas Park City':
        return 51685
    elif row['county']== 'Martinsville City':
        return 51690
    elif row['county']== 'Newport News City':
        return 51700
    elif row['county']== 'Norfolk City':
        return 51710
    elif row['county']== 'Norton City':
        return 51720
    elif row['county']== 'Petersburg City':
        return 51730
    elif row['county']== 'Poquoson City':
        return 51735
    elif row['county']== 'Portsmouth City':
        return 51740
    elif row['county']== 'Radford City':
        return 51750
    elif row['county']== 'Richmond City':
        return 51760
    elif row['county']== 'Roanoke City':
        return 51770
    elif row['county']== 'Salem City':
        return 51775
    elif row['county']== 'Staunton City':
        return 51790
    elif row['county']== 'Suffolk City':
        return 51800
    elif row['county']== 'Virginia Beach City':
        return 51810
    elif row['county']== 'Waynesboro City':
        return 51820
    elif row['county']== 'Williamsburg City':
        return 51830
    elif row['county']== 'Winchester City':
        return 51840
    return fips

data['fips'] = data.apply(fips, axis=1)

data.to_csv('va.csv')