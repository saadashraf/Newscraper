import pandas as pd

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