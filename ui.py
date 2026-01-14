import tkinter as tk

# start ui portion of the code, using tkinter GUI b/c it's pretty simple
window = tk.Tk()
window.title("Hobby Picker")
window.geometry('400x400')

# add labels and checkboxes and whatnot
type_label = tk.Label(window, text="Select which types of activities you would want to do:")
type_label.pack()

music_var, art_var, watching_var, reading_var, work_var, shopping_var = tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()

music_cb = tk.Checkbutton(window, text="Music", variable=music_var, onvalue=1, offvalue=0)
art_cb = tk.Checkbutton(window, text="Art", variable=art_var, onvalue=1, offvalue=0)
watching_cb = tk.Checkbutton(window, text="Watching", variable=watching_var, onvalue=1, offvalue=0)
reading_cb = tk.Checkbutton(window, text="Reading", variable=reading_var, onvalue=1, offvalue=0)
work_cb = tk.Checkbutton(window, text="Work", variable=work_var, onvalue=1, offvalue=0)
shopping_cb = tk.Checkbutton(window, text="Shopping", variable=shopping_var, onvalue=1, offvalue=0)

music_cb.pack()
art_cb.pack()
watching_cb.pack()
reading_cb.pack()
work_cb.pack()
shopping_cb.pack()

window.mainloop()