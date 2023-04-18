import tkinter as tk
import math

window = tk.Tk()
window.title('BMI Calculator')
window.minsize(200,300)
window.config(pady=30,padx=30)

FONT = ('Arial',10,'italic')

weight_label = tk.Label(text='Enter Your Weight (kg)',font=FONT)
weight_label.pack()
weight_label.config(padx=15,pady=15)

weight_entry = tk.Entry(width=15)
weight_entry.pack()

height_label = tk.Label(text='Enter Your Height (cm)',font=FONT)
height_label.pack()
height_label.config(padx= 15, pady=15)

height_entry = tk.Entry(width=15)
height_entry.pack()

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())

    global result_label
    if weight == "" or height == "":
        result_label.config(text='Please enter weight and height values!')
    else:
        try:
            bmi_result = weight / (math.pow((height / 100), 2))
            result_text = f'Your BMI is: {round(bmi_result, 2)}. You are'
            if bmi_result < 18.5:
                result_label.config(text=f'{result_text} under weight.')

            elif 18.5 < bmi_result < 24.9:
                result_label.config(text=f'{result_text} normal weight.')

            elif 25 < bmi_result < 29.9:
                result_label.config(text=f'{result_text} over weight.')

            elif 30 < bmi_result < 34.9:
                result_label.config(text=f'{result_text} obesity (Class 1).')

            elif 35 < bmi_result < 39.9:
                result_label.config(text=f'{result_text} obesity (Class 2).')

            else:
                result_label = tk.Label(text=f'{result_text} extreme obesity.')

        except:
            result_label.config(text='Enter a valid number')


calculate_button = tk.Button(text='Calculate', command=calculate_bmi)
calculate_button.pack()

result_label = tk.Label()
result_label.pack()

window.mainloop()