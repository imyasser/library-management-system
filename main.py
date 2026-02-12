from operator import truediv

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
from matplotlib.backend_tools import cursors

df = pd.read_csv('books.csv__100lines.csv')

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

cursor = connection.cursor()
"""

df['Book_num'] = np.random.randint(1,15,len(df))
for _,row in df.iterrows():
    count = UPDATE books SET book_num =  %s WHERE title = %s
    val = (int(row['Book_num']),row['title'])
    cursor.execute(count,val)
connection.commit()
"""

def user_exist(username):
    search = "SELECT * FROM users WHERE username = %s"
    cursor.execute(search,(username,))
    found = cursor.fetchone()

    if found:
        print(f"Welcome '{username}' ------ \n")
        return True
    else:
        return False
def create_user():
    while True:
        username = str(input("Enter a valid username"))
        if user_exist(username)==True:
            print("User name already exist")
        else:
            gender = str(input("Enter your gender"))
            gender.upper()
            break
    insert_user = """INSERT INTO users(username,gender) VALUES (%s,%s)"""
    cursor.execute(insert_user,(username,gender))
    connection.commit()
    print("----Account created----- \n")

def Add_book():
    print("--------Add a Book to The library-----------")
    name = str(input("Enter your username"))


def main():
    while True:
        print("-----WELCOME TO THE LIBRARY-----")
        print("1) Connect")
        print("2) Create account")
        print("3) Exit")
        print("--------------------------------")

        choice = input("Choose one from the list:")
        if choice == '1':
            user_name = input("Enter your username:")
            if user_exist(user_name)==True:
                break
            else:
                print("User not found with this username, create one \n")
                continue
        elif choice == '2':
            create_user()
            continue
        elif choice =='3':
            exit()
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



df.drop(columns=['isbn'], inplace=True)
df.drop(columns=['isbn13'],inplace=True)
df.drop(columns=['ratings_count'],inplace=True)
df.drop(columns=['text_reviews_count'],inplace=True)
df.drop(columns=['publication_date'],inplace=True)
df.drop(columns=['publisher'],inplace=True)

df['men'] = np.random.randint(10,300,size=len(df))
df['women'] = np.random.randint(10,300,size=len(df))

print("Inserting data")

for _,row in df.iterrows():
    insert_book =  INSERT INTO books
                    (title,authors,average_rating,women,languagecode)
                    VALUES (%s, %s, %s, %s, %s, %s)
    values = (row['title'],row['authors'],row['average_rating'],row['men'], row['women'], row['language_code'])
    cursor.execute(insert_sql,values)
connection.commit()

"""
