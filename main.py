# Importing tkinter
from tkinter import *
from tkinter import ttk

# Basic tkinter setup
window = Tk()
window.geometry("600x300")
window.title("BMI Calculator")

# Creating welcome heading
welcome_heading = ttk.Label(window, text="Welcome to BMI Calculator", font="lucida 20 bold")
welcome_heading.grid(row=0, columnspan=3, padx=110, pady=5)

# Creating height label and entry
height_label = ttk.Label(window, text="Enter your height in cm", font="lucida 13")
height_label.grid(row=1, columnspan=1, pady=20, padx=45)

height_value = IntVar()
height_entry = ttk.Entry(window, textvariable=height_value)
height_entry.grid(row=1, column=1)

# Creating weight label and entry
weight_label = ttk.Label(window, text="Enter your weight in kg", font="lucida 13")
weight_label.grid(row=2, column=0)

weight_value = IntVar()
weight_entry = ttk.Entry(window, textvariable=weight_value)
weight_entry.grid(row=2, column=1)

# Creating age label and entry
age_label = ttk.Label(window, text="Enter your age", font="lucida 13")
age_label.grid(row=3, column=0, pady=20)

age_entry = ttk.Entry(window)
age_entry.grid(row=3, column=1, pady=20)

# Function for calculating bmi
def calculate():
    height = float(height_value.get())
    weight = float(weight_value.get())

    bmi = weight/((height*0.01)**2)
    output_result = Label(window, text=f"Your BMI is {round(bmi,2)}.", font="lucida 13")
    output_result.grid(row=5, columnspan=3)

    return bmi, output_result



# Create calculate button
calculate_button = ttk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=4, columnspan=3, pady=10)


window.mainloop()