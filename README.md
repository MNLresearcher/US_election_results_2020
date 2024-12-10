# US_election_results_2020
The 2020 election results for each county in each state (except oklahoma)

The data folder contains the total votes of each candidate in every county for 49 states (excluding oklahoma). 
Since each state publishes their election results in their own style and format (pdf,xls,csv), we have to apply the codes from the folder 'parsing_codes' to transform the data into the required form and assign the fips codes afterwards (see the folder addfips).
In most cases their data has the county as index and the candidates as column names, for this you only need to apply the 'python Columnchange.py'. 
If there are any unwanted columns, delete them using 'python deletecolumn.py'. Sometimes the votes are displayed on a precinct-level so that they have to be sumed up using 'python sumrows.py'.
'python filterrows.py' is used when the data also contains the votes for other political positions (e.g. senator), which we sort out.
In order for all python codes to work, the data has to be managed into a csv. For xls and xlms it is quite easy, but in pdf-format it has to be copy pasted. We recommend to use notepad++ for the data framing.
Run 'python "election data by region".py' to sort the votes into their respective regions (using the region.h5 file from 'https://github.com/djsutherland/pummeler/tree/master')
