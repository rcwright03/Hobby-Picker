import pandas as pd
import numpy as np

hobby_sheet = pd.read_csv("Hobby_Sheet.csv", index_col=False)
#print(hobby_sheet.head()) # print for testing

# get input from users
def getInput():
    intensity_input = input("Enter desired intensity of activity (Low, Med, High)\n").lower().capitalize()
    time_input = int(input("Enter amount of time in minutes\n"))

    return intensity_input, time_input

# get dataframe output from users
def getOutput(intensity, time):
    results_df = hobby_sheet[(hobby_sheet['Intensity'] == intensity) &
                  (hobby_sheet['Time (min)'] <= time)]
    return results_df

def selectRandomActivities(df):
    random_rows = df.sample(n=3)
    print(random_rows['Activity'])