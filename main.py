import tkinter as tk

# Window Settings
window = tk.Tk()
window.title("BMI Calculator")
window.minsize(400, 300)

result = tk.Label(text="")


# BMI Calculator
def bmi_calculator():
    try:
        weight = float(input_one.get())
        height_in_meters = float(input_two.get()) / 100
        bmi = weight / (height_in_meters * height_in_meters)
        bmi = round(bmi, 2)
        results_printer(bmi)
    except ValueError:
        result.config(text="Please enter a valid number!")
        result.pack()


# Results
def results_printer(bmi):
    if 0 <= bmi < 18.5:
        result.config(text=f"Your BMI is {bmi}.You are underweight")
    elif 18.5 <= bmi < 25:
        result.config(text=f"Your BMI is {bmi}.You are healthy")
    elif 25 <= bmi < 30:
        result.config(text=f"Your BMI is {bmi}.You are overweight")
    elif bmi >= 30:
        result.config(text=f"Your BMI is {bmi}.You are obese")
    else:
        result.config(text="Please enter a valid number!")
    result.pack()


# Weight
label_one = tk.Label(text="Enter your Weight (kg)")
label_one.pack()
input_one = tk.Entry()
input_one.pack()

# Height
label_two = tk.Label(text="Enter your Height (m)")
label_two.pack()
input_two = tk.Entry()
input_two.pack()

# Calculate Button
button = tk.Button(text="Calculate", command=bmi_calculator)
button.pack()

window.mainloop()