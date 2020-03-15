import scraping
import pandas as pd

#Get the informations from scraping function
links , titles , authors , contents = scraping.scraping_output()

#Make a dictionary from the dataset
dataset = {"Link" : links,
            "Title" : titles,
            "Author" : authors,
            "Content" : contents}

#Convert the dataset into pandas dataframe
df = pd.DataFrame(dataset, columns= ['Link', 'Title' , 'Author' , 'Content'])
#print(df)

#Export the dataframe into a csv file
df.to_csv("Output_dataset.csv")