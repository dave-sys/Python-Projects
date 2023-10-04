import pandas as pd

earthquake_df = pd.read_csv('Eartquakes-1990-2023.csv')

#split date into date and time
earthquake_df[['date', 'hour']] = earthquake_df['date'].str.split(" ",expand = True)

#drop time column 
earthquake_df = earthquake_df.drop(columns= ['time'])

#rename magnitudo to magnitude
earthquake_df = earthquake_df.rename(columns={"magnitudo":"magnitude"})

#rename state into country 
earthquake_df = earthquake_df.rename(columns= {"state":'country'})

#store all of indonesia earth quakes into a new dataframe
indo_earthquake_filter = earthquake_df["country"] == " Indonesia"

indo_earthquake_df = earthquake_df[indo_earthquake_filter]

#extract the name of the cities and apply it to a new column
def extract_city_name(city_description):
    
    # Split the city description by commas and get the part after "of "
    parts = city_description.split(',')
    if len(parts) > 1:
        city_part = parts[0].split('of ')[-1].strip()
        return city_part
    else:
        return None

#applies the function into the dataframe and makes a new column
indo_earthquake_df['closes city'] = indo_earthquake_df['place'].apply(extract_city_name)

#turns the dataframe into a csv
indo_earthquake_df.to_csv("Earthquakes in Indonesia 1990 to 2023.csv")


