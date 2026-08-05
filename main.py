import tkinter as tk
from tkinter import messagebox
# Function to Calculate BMI
def calculate_bmi():
    try:
        # Get User Input
        name = name_entry.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        # Check if values are valid
        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Weight and Height must be greater than 0.")
            return
        # Calculate BMI
        bmi = weight / (height ** 2)
        # Find BMI Category
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal Weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        # Display Result
        result = f"Name : {name}\nBMI : {bmi:.2f}\nCategory : {category}"
        result_label.config(text=result)
        # Save Result to output.txt
        with open("output.txt", "w") as file:
            file.write(result)
        messagebox.showinfo("Success", "BMI calculated and saved to output.txt")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for weight and height.")
# Create Window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x500")
# Heading
title = tk.Label(root, text="BMI Calculator", font=("Arial", 20, "bold"))
title.pack(pady=20)
# Name
name_label = tk.Label(root, text="Name")
name_label.pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)
# Weight
weight_label = tk.Label(root, text="Weight (kg)")
weight_label.pack()
weight_entry = tk.Entry(root, width=30)
weight_entry.pack(pady=5)
# Height
height_label = tk.Label(root, text="Height (m)")
height_label.pack()
height_entry = tk.Entry(root, width=30)
height_entry.pack(pady=5)
# Calculate Button
calculate_button = tk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi,
    font=("Arial", 12)
)
calculate_button.pack(pady=20)
# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()
# Run Window
root.mainloop()