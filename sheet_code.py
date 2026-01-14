import pandas as pd

hobby_sheet = pd.read_csv("Hobby_Sheet.csv")
print(hobby_sheet.head()) # print for testing

# get input from users
def getInput():
    intensity_input = input("Enter desired intensity of activity (Low, Med, High)\n").lower().capitalize()
    time_input = int(input("Enter amount of time in minutes\n"))
    type_input = input("Enter desired activity type (Music, Art, TV/Movie/YouTube, Work, Reading, Shopping)\n").lower().capitalize()
    return intensity_input, time_input, type_input

# get dataframe output from users
def getOutput(intensity, time, type):
    results_df = hobby_sheet[(hobby_sheet['Type'] == type) &
                  (hobby_sheet['Intensity'] == intensity) &
                  (hobby_sheet['Time (min)'] <= time)]
    return results_df

