import pandas as pd

#A function that returns a DataFrame of the cleaned data
def cleanDF():

    df = pd.read_csv('helium-hotspot_2020-5-19_2021-9-5.csv')
    df = df.drop(['Market Cap','Volume'], axis = 1)

    return df