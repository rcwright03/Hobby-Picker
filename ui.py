import tkinter as tk
from sheet_code import hobby_sheet, selectRandomActivities

# start ui portion of the code, using tkinter GUI b/c it's pretty simple
window = tk.Tk()
window.title("Hobby Picker")
window.geometry('500x700')

# add labels and input line for time input and intensity input
intensity_label = tk.Label(window, text="Select desired level of intensity:").pack(pady=10, anchor='w')

string_var = tk.StringVar(value="nothin?")
low_rb = tk.Radiobutton(window, text="Low", variable = string_var, value="Low").pack(anchor='w')
med_rb = tk.Radiobutton(window, text="Med", variable = string_var, value="Med").pack(anchor='w')
high_rb = tk.Radiobutton(window, text="High", variable = string_var, value="High").pack(anchor='w')

# function to ensure that the entered value is a number
def validateNum(string):
    return string.isdigit() or string == ""
# register validation fcn as a command
validation = window.register(validateNum)

time_label = tk.Label(window, text="Enter amount of time in minutes:").pack(pady=10, anchor='w')
time_entry = tk.Entry(window, validate='key', validatecommand=(validation, '%S'))
time_entry.pack(anchor='w')

# add labels and checkboxes for type input
type_label = tk.Label(window, text="Select which types of activities you would want to do:").pack(pady=10, anchor='w')

type_var_dict = {
    "Music": tk.IntVar(),
    "Art": tk.IntVar(),
    "Watching": tk.IntVar(),
    "Reading": tk.IntVar(),
    "Work": tk.IntVar(),
    "Shopping": tk.IntVar()
}
for text, var in type_var_dict.items():
    cb = tk.Checkbutton(
        window,
        text=text,
        variable=var,
        onvalue=1,
        offvalue=0
    )
    cb.pack(anchor='w')

def submitFunction():
    # get values from entries and filter them in the dataframe
    # validate that entered values are okay
    intensity = string_var.get()
    results_df = hobby_sheet[hobby_sheet['Intensity'] == intensity]
    # print(results_df) # testing printing

    mins = int(time_entry.get())
    results_df = results_df[results_df['Time (min)'] <= mins]
    
    for text, var in type_var_dict.items():
        if var.get() == 0:
            results_df = results_df[results_df['Type'] != text]

    print(results_df)
    
    # show output (label + random activities) when button is clicked
    output_label.pack(pady=10, anchor='w')

'''def resetOptions():
    # reset each option
    string_var.set("nothin?")
    time_entry.delete(0, tk.END)'''

submit_button = tk.Button(window, text='Enter', command=submitFunction).pack(pady=10, anchor='w')

# will finish reset button when the rest is complete
# reset_button = tk.Button(window, text="Reset Options", command=resetOptions).pack(pady=10, anchor='w')

output_label = tk.Label(window, text="Activities:")

window.mainloop()