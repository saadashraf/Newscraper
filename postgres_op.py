import psycopg2

#uploading the data into postgres database
def enter_word_count(word_count):
    try:
        #making the connection using credentials
        connection = psycopg2.connect(user = "eciuvvjjmawypq",
                                    password = "f742d9624cca75affce31a69bf8d86a93a1f39cf233ff1a4e6c1cf163b328cd0",
                                    host = "ec2-3-229-210-93.compute-1.amazonaws.com",
                                    port = "5432",
                                    database = "d3bpa14p78p94e")

        #getting a cursor object to perform postgres command
        cursor = connection.cursor()
        
        #performing insertion operation for each of the tuples
        for word , count in word_count:
            
            insert_query = """INSERT INTO analytics (word , count) VALUES (%s , %s)""" 
            record = (str(word) , count)

            cursor.execute(insert_query , record)

        print("Successfully added data")
        connection.commit()


    except (Exception, psycopg2.Error) as error :
        print ("Error while inserting to PostgreSQL", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")