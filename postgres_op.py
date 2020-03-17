import psycopg2
from datetime import datetime

def enter_word_count(word_count):
    try:
        connection = psycopg2.connect(user = "eciuvvjjmawypq",
                                    password = "f742d9624cca75affce31a69bf8d86a93a1f39cf233ff1a4e6c1cf163b328cd0",
                                    host = "ec2-3-229-210-93.compute-1.amazonaws.com",
                                    port = "5432",
                                    database = "d3bpa14p78p94e")

        cursor = connection.cursor()
        date = datetime.date(datetime.now())
        time = datetime.time(datetime.now())

        insert_query = """INSERT INTO analytics (Date , Time , Word_count) VALUES (%s , %s , %s)"""
        record = (date , time , word_count)

        cursor.execute(insert_query , record)

        connection.commit()


    except (Exception, psycopg2.Error) as error :
        print ("Error while inserting to PostgreSQL", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")