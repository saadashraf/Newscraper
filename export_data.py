import pandas as pd
from datetime import datetime

def publish_dataset_csv(links , titles , authors , contents , target):
    
    #Make a dictionary from the dataset
    dataset = {"Link" : links,
                "Title" : titles,
                "Author" : authors,
                "Content" : contents}

    #Convert the dataset into pandas dataframe
    df = pd.DataFrame(dataset, columns= ['Link', 'Title' , 'Author' , 'Content'])
    #print(df)

    #Export the dataframe into a csv file
    df.to_csv(target)

def publish_count_csv(word_count , target):

    date_time = datetime.now()
    #Make a dictionary of the data
    dataset = {"Date_time" : date_time,
                "Word_count" : word_count}
    
    #Convert the dataset into pandas dataframe
    df = pd.DataFrame(dataset, columns= ['Date_time' , 'Word_count'])
    #print(df)

    #Export the dataframe into a csv file
    df.to_csv(target)