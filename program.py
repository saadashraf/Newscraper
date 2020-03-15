import scraping
import export_data
import analytics

#Get the informations from scraping function
links , titles , authors , contents = scraping.scraping_output()

#Export the data into a csv file
export_data.publish_dataset_csv(links , titles , authors , contents , "Output_dataset.csv")

#Get the word count for the news contents
word_count = analytics.word_count(contents)
