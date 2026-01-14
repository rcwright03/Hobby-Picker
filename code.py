import pandas as pd

hobby_sheet = pd.read_csv("Hobby_Sheet.csv")

print(hobby_sheet.head())

# get input from users
intensity_input = input("Enter desired intensity of activity (Low, Med, High)\n").lower().capitalize()
# print(f"{intensity_input}") # testing input

time_input = int(input("Enter amount of time in minutes\n"))

type_input = input("Enter you desired activity type (Music, Art, TV/Movie/YouTube, Work, Shopping)\n").lower().capitalize()

# get output
'''returned_df = hobby_sheet[(hobby_sheet['Type'] == type_input) &
                          (hobby_sheet['Intensity'] == intensity_input) &
                          (hobby_sheet['Time (min)'] <= time_input)]
print(returned_df.head())'''

results = hobby_sheet[(hobby_sheet['Type'] == type_input) &
                  (hobby_sheet['Intensity'] == intensity_input) &
                  (hobby_sheet['Time (min)'] <= time_input)]
print(results)