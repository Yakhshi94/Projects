import tkinter as tk

FONT = ("monospace", 20, 'bold')


def convert_to_km():
    mile = float(get_mile.get())
    kms = round(mile * 1.6)
    result['text'] = kms

window = tk.Tk()
window.config(padx=10, pady=10)
window.title("Mile To Km Converter")
# window.minsize(width=500, height=300)

get_mile = tk.Entry()
get_mile.grid(column=1, row=0)

label_miles = tk.Label(text="Miles", font=FONT)
label_miles.grid(column=2, row=0)

result_label = tk.Label(text="is equal to", font=FONT)
result_label.grid(column=0, row=1)

result = tk.Label(text="0", font=FONT)
result.grid(column=1, row=1)

km = tk.Label(text="Km", font=FONT)
km.grid(column=2, row=1)

button = tk.Button(text='Calculate', command=convert_to_km, font=FONT)
button.grid(column=1, row=2)















window.mainloop()
