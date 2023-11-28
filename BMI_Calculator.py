from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("BMI CALCULATOR")
root.geometry("600x500")
root.config(bg='DodgerBlue')


def calculate_BMI(weight, height):
    weight = float(weight)
    height = float(height)

    BMI = weight/(height/100)**2 
    return BMI
def classify_BMI(BMI):
    if BMI < 18.5:
        messagebox.showinfo("Result",f"Body Mass Index = {BMI:.2f}\n \nYou are Underweight")
    elif BMI >= 18.5 and BMI <= 24.9:
        messagebox.showinfo("Result",f"Body Mass Index = {BMI:.2f}\n \nYou are Healthy")
    elif BMI >= 24.9 and BMI <= 29.9:
        messagebox.showinfo("Result",f"Body Mass Index = {BMI:.2f}\n \nYou are Overweight.")
    elif BMI >= 29.9:
        messagebox.showinfo("Result",f"Body Mass Index = {BMI:.2f}\n \nYou are Obesity.")
    else:
        messagebox.showerror("Result","Invalid!")


    
def on_calculate():
    Name = name_entry.get()
    Age = age_entry.get()
    Weight =weight_entry.get()
    Height = height_entry.get()
    BMI = calculate_BMI(Weight, Height)
    if isinstance(BMI, str):
        messagebox.showerror("Error")
    else:
        calculate = classify_BMI(BMI)
        

def reset_entry():
    name_entry.delete(0, 'end')
    age_entry.delete(0, 'end')
    weight_entry.delete(0, 'end')
    height_entry.delete(0, 'end')
    

var = IntVar()

name_label = Label(root, text="Name :", font=('Arial', 15), background='DodgerBlue')
name_entry = Entry(root, width=30, font=('Arial', 15), background='DodgerBlue')

age_label = Label(root, text="Age :", font=('Arial', 15), background='DodgerBlue')
age_entry = Entry(root, width=20,font=('Arial', 15), background='DodgerBlue')

gender_label = Label(root, text="Gender",font=('Arial', 15), background='DodgerBlue')
male_rb = Radiobutton(root, text="Male", value = 1, variable = var,font=('Arial', 15), background='DodgerBlue')
female_rb = Radiobutton(root, text="Female", value = 2, variable=var,font=('Arial', 15), background='DodgerBlue')

weight_label = Label(root, text="Weight (KG) :", font=('Arial', 15), background='DodgerBlue')
weight_entry = Entry(root, width=30,font=('Arial', 15), background='DodgerBlue')

height_label = Label(root, text="Height (M) :", font=('Arial', 15), background='DodgerBlue')
height_entry = Entry(root, width=30,font=('Arial', 15), background='DodgerBlue')

calculate_button = Button(root, text="CALCULATE",font=('Arial', 15), background='#49A109', command=on_calculate)
reset_button = Button(root, text="RESET",font=('Arial', 15), background='grey', command=reset_entry)
exit_button = Button(root, text="EXIT",font=('Arial', 15), background='red', command=lambda:root.destroy())

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1, pady=20, padx=20)
age_label.grid(row=1, column=0)
age_entry.grid(row=1, column=1, pady=20, padx=20)
gender_label.grid(row=2, column=0)
male_rb.grid(row=2, column=1, pady=20, padx=20)
female_rb.grid(row=3, column=1, pady=20, padx=20)
weight_label.grid(row=4, column=0)
weight_entry.grid(row=4, column=1, pady=20, padx=20)
height_label.grid(row=5, column=0)
height_entry.grid(row=5,column=1, pady=20, padx=20)
calculate_button.grid(row=6, column=0, pady=10, padx=10)
reset_button.grid(row=6, column=1)
exit_button.grid(row=6, column=2)




root.mainloop()
