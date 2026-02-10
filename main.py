import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

#connect to a database
try:
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",      # Default for phpMyAdmin/XAMPP
        password="",      # XAMPP default is an empty string
        port=3307,
        database  = "library"
    )
    print("Connected to MySQL via phpMyAdmin/XAMPP!")
except mysql.connector.Error as err:
    print(f"Error: {err}")


def main():
    while True:
        print("-----WELCOME TO THE LIBRARY-----")
        print("1) Borrow a book")
        print("2) Add a BoOK to the library")
        print("3) Exit")
        print("--------------------------------")

        choice = input("Choose one from the list:")

if __name__ == "__main__":
    main()

"""
 ---------- Hadi hia bach zedt hadok les elements dial dataset f database----

cursor = connection.cursor()
df = pd.read_csv('books.csv__100lines.csv')
df.drop(columns=['isbn'], inplace=True)
df.drop(columns=['isbn13'],inplace=True)
df.drop(columns=['ratings_count'],inplace=True)
df.drop(columns=['text_reviews_count'],inplace=True)
df.drop(columns=['publication_date'],inplace=True)
df.drop(columns=['publisher'],inplace=True)

df['men_borrowers'] = np.random.randint(10,300,size=len(df))
df['women_borrowers'] = np.random.randint(10,300,size=len(df))

print("Inserting data")

for _,row in df.iterrows():
    insert_sql =  INSERT INTO books
                    (title,authors,average_rating,men_borrowers,women_borrowers,languagecode)
                    VALUES (%s, %s, %s, %s, %s, %s)
    values = (row['title'],row['authors'],row['average_rating'],row['men_borrowers'], row['women_borrowers'], row['language_code'])
    cursor.execute(insert_sql,values)
connection.commit()
print(f"Data succefully added to database with numbers of books: {len(df)}")

"""
