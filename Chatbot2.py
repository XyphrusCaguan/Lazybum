import re
#import long_responses as long
import pandas as pd
import numpy as np
import random
# Import writer class from csv module
from csv import writer

def chat_exam():
    print("What is your last name?")
    user_lastName = input("User: ")
    print("What is your first name?")
    user_firstName = input("User: ")
    print("Your gender?")
    user_gender = input("User: ")
    print("How old are you?")
    user_age = input("User: ")
    print("Where do you live?")
    user_address = input("User: ")
    print("Question 1")
    user_q1 = input("User: ")
    print("Question 2")
    user_q2 = input("User: ")
    print("Question 3")
    user_q3 = input("User: ")
    print("Question 4")
    user_q4 = input("User: ")
    print("Question 5")
    user_q5 = input("User: ")

    user_fullName = user_firstName + " " + user_lastName
    df2 = pd.DataFrame([[user_lastName, user_firstName, user_fullName, user_gender, user_age, user_address, user_q1, user_q2, user_q3,  user_q4, user_q5]],
                   columns=['LastName', 'FirstName', 'FullName', 'Gender', 'Age', 'Address', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5'])

    # List
    #List = [user_lastName, user_firstName, fullName, user_gender, user_age, user_address, user_q1, user_q2, user_q3,  user_q4, user_q5]

    # list of column names
    field_names = ['LastName', 'FirstName', 'FullName',
               'Gender', 'Age', 'Address', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5']

    # Dictionary
    dict = {'LastName': user_lastName, 'FirstName': user_firstName, 'FullName': user_fullName,
               'Gender': user_gender, 'Age': user_age, 'Address': user_address, 'Q1': user_q1, 'Q2': user_q2, 'Q3': user_q3, 'Q4': user_q4, 'Q5': user_q5}

        # Open our existing CSV file in append mode
        # Create a file object for this file
    with open('Chatbot_Responses.csv', 'a') as f_object:
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)

        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(dict)

        # Close the file object
        f_object.close()

    print(dict)