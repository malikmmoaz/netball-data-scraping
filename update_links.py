# read csv file and update each row with the new link

#https://engage.englandnetball.co.uk/Dashboard/Organisation/{placeholder}

import pandas as pd

df = pd.read_csv('raw_links.csv', header=None)

for index, row in df.iterrows():
    df.iloc[index, 0] = 'https://engage.englandnetball.co.uk/Dashboard/Organisation/' + str(row[0])
    #print(df.iloc[index, 0])

# add dataframe as a new column in links.csv
# delete contents of links.csv

df.to_csv('links.csv', header=False, index=False)
