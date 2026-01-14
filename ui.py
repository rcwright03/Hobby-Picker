import tkinter as tk

# start ui portion of the code, using tkinter GUI b/c it's pretty simple
window = tk.Tk()
window.title("Hobby Picker")
window.geometry('500x700')

# add labels and input line for time input and intensity input
intensity_label = tk.Label(window, text="Select desired level of intensity:")

string_var = tk.StringVar(value="nothin?")
low_rb = tk.Radiobutton(window, text="Low", variable = string_var, value="Low")
med_rb = tk.Radiobutton(window, text="Med", variable = string_var, value="Med")
high_rb = tk.Radiobutton(window, text="High", variable = string_var, value="High")

intensity_label.pack(pady=10, anchor='w')
low_rb.pack(anchor='w')
med_rb.pack(anchor='w')
high_rb.pack(anchor='w')

# function to ensure that the entered value is a number
def validate_num(p):
    if p.isdigit():
        return True
    else:
        return False

# register validation fcn as a command
vcmd = (window.register(validate_num), '%p')

time_label = tk.Label(window, text="Enter amount of time in minutes:")
time_entry = tk.Entry(window, validate='key', vcmd=vcmd)

time_label.pack(pady=10, anchor='w')
time_entry.pack(anchor='w')

# add labels and checkboxes for type input
type_label = tk.Label(window, text="Select which types of activities you would want to do:")
type_label.pack(pady=10, anchor='w')

music_var, art_var, watching_var, reading_var, work_var, shopping_var = tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()

music_cb = tk.Checkbutton(window, text="Music", variable=music_var, onvalue=1, offvalue=0)
art_cb = tk.Checkbutton(window, text="Art", variable=art_var, onvalue=1, offvalue=0)
watching_cb = tk.Checkbutton(window, text="Watching", variable=watching_var, onvalue=1, offvalue=0)
reading_cb = tk.Checkbutton(window, text="Reading", variable=reading_var, onvalue=1, offvalue=0)
work_cb = tk.Checkbutton(window, text="Work", variable=work_var, onvalue=1, offvalue=0)
shopping_cb = tk.Checkbutton(window, text="Shopping", variable=shopping_var, onvalue=1, offvalue=0)

music_cb.pack(anchor='w')
art_cb.pack(anchor='w')
watching_cb.pack(anchor='w')
reading_cb.pack(anchor='w')
work_cb.pack(anchor='w')
shopping_cb.pack(anchor='w')

def get_values():
    try:
        time_val = time_entry.get()
        if time_val:
            mins = int(time_val)
            print(f"Test if this worked, number: {mins}")
        else:
            print("Did this work?")
    except ValueError:
        print("Invalid number input")

submit_b = tk.Button(window, text='Enter', command=get_values)
submit_b.pack(pady=10, anchor='w')

window.mainloop()