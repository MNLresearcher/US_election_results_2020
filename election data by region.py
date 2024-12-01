from __future__ import division, print_function
#get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
import pandas as pd
import re
import six

from IPython.display import display

import sys
sys.path.append('..')

from geocode_data import geocode_data

county_to_region = geocode_data('county_region_10').region.to_dict()

from glob import glob

bits = []
for f in glob('data/??.csv'):
    # Two ?? instead of * do the trick too
    piece = pd.read_csv(f, dtype={'fips': str})
    #The election results from all counties are called (with fips called as string)
    piece['state'] = f[-6:-4]
    bits.append(piece)
election = pd.concat(bits)

cand_votes = election.groupby(election.candidate).votes.agg(lambda x: pd.to_numeric(x, errors='coerce').sum()).sort_values(ascending=False)
print(cand_votes)
#Here we want to sum the overall votes for all candidates but since this list has some elements with the 'string' or 'integer' type it cannot sum or concatenate them. Instead it gives the error message 'can only concatenate str (not "int") to str'

election['party'] = 'oth'
election.loc[election.candidate == 'Joseph R. Biden', 'party'] = 'D'
election.loc[election.candidate == 'Donald J. Trump', 'party'] = 'R'
#assigning each candidate to their respective party

print(election.groupby(election.party).votes.agg(lambda x: pd.to_numeric(x, errors='coerce').sum()).sort_values(ascending=False))
#sorting each votes according to their party and summing them up

set(election.fips) - set(county_to_region)
#turning the fips codes from the 'election' dataframe as well as 'county_to_region' fips into a sequence and filtering out the fips codes from the first list, which are not in the second list

election[pd.isnull(election.fips)]
# checking if there is any 'Not a Number' (aka NaN) values in the fips column

{fips for fips in set(county_to_region) - set(election.fips)
 if not fips.startswith('02')}
#checking which 'county_to_region' fips are not in the 'election' fips list, except Alaska (whose fips code starts with '02')

county_to_region['15005'] == county_to_region['15009']

df=election.groupby(election.fips.map(county_to_region))
#transforming the fips in the election data into their respective region (according to the county_to_region), and grouping them

election_region = df.apply(lambda x: x.votes.groupby(x.party).sum()).unstack()

# summing the votes for each party in each region and then using the each party as a seperate column (through unstack)

election_region.index.name = 'region'
# the regions are now the index and get the name 'region'
election_region.columns = ['votes_{}'.format(p) for p in election_region.columns]
# we add a 'votes_' to every column name

election_region.fillna(0, inplace=True)
#each uknown value gets a zero assigned
election_region = election_region.astype('int')
#translating each number into an integer
print(election_region.head())

election_region.to_csv('2020-by-region.csv.gz', compression='gzip')

