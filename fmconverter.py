import tkinter as tk
from tkinter.font import Font

# Function to center the fixed-size frame
def center_frame(root, frame):
    root.update_idletasks()
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    frame_width = frame.winfo_width()
    frame_height = frame.winfo_height()
    x = (window_width // 2) - (frame_width // 2)
    y = (window_height // 2) - (frame_height // 2)
    frame.place(x=x, y=y)

# Create the main window
window = tk.Tk()
window.title("Feet to meter conversion app")
window.configure(background="#FF10F0")
window.geometry("800x600")  # Starting size, but it can be resized
window.resizable(width=True, height=True)

# other functions to convert units
def convert():
    try:
        if ft_entry.get():
            value = float(ft_entry.get())
            meter = value * 0.3048
            mt_value.set(f"{meter:.2f}")
        elif mt_entry.get():
            value = float(mt_entry.get())
            feet = value * 3.280839895
            ft_value.set(f"{feet:.2f}")
    except ValueError:
        mt_value.set("Invalid input")
        ft_value.set("Invalid input")

def clear():
    ft_value.set("")
    mt_value.set("")

# Create a fixed-size mint green frame
frame = tk.Frame(window, bg="#98FF98", width=620, height=520)
frame.place(x=0, y=0)  # Initial placement; will be updated

# Update the frame position whenever the window size changes
window.bind('<Configure>', lambda event: center_frame(window, frame))

# Define the font with size and weight
font_style = Font(family="Helvetica", size=12, weight="bold")

# Place the label inside the frame with specified styles
ft_lbl = tk.Label(frame, text="Feet", bg="white", fg="black", width=14, font=font_style,
                  borderwidth=1, relief="solid")
ft_lbl.place(x=30, y=30, width=125, height=20)

# Create a DoubleVar instance for the entry field
ft_value = tk.DoubleVar()
# Create an Entry widget bound to the DoubleVar and place it inside the frame
ft_entry = tk.Entry(frame, textvariable=ft_value, width=14)
# Position it below the label with some padding
ft_entry.place(x=185, y=30, width=125, height=20)
 # Clear any default text
ft_entry.delete(0, 'end')

# Create and place the Meter label as shown in the picture
mt_lbl = tk.Label(frame, text="Meter", bg="white", fg="black", width=14, font=font_style,
                  borderwidth=1, relief="solid")
mt_lbl.place(x=30, y=80, width=125, height=20)  # Corrected y-coordinate

# Create a DoubleVar instance for the meter entry field
mt_value = tk.DoubleVar()

# Create an Entry widget bound to the DoubleVar and place it inside the frame
mt_entry = tk.Entry(frame, textvariable=mt_value, width=14)
mt_entry.place(x=185, y=80, width=125, height=20)  # Corrected y-coordinate
mt_entry.delete(0, 'end')  # Clear any default text

# Create and place the Convert button
convert_btn = tk.Button(frame, text="Convert", bg="#98FF98", fg="#FF10F0", width=14, height=30, activebackground="#98FF98", activeforeground="#FF10F0", highlightbackground="white", highlightcolor="#FF10F0", state="active", font=font_style, command=convert)
convert_btn.place(x=30, y=130, width=250, height=30)  # Positioned below the entries

# Create the clear button
clear_btn = tk.Button(frame, text="Clear", bg="#98FF98", fg="#FF10F0", width=14, height=30, activebackground="#98FF98", activeforeground="#FF10F0", highlightbackground="white", highlightcolor="#FF10F0", state="active", font=font_style, command=clear)
clear_btn.place(x=320, y=130, width=250, height=30)  # Positioned below the entries


# Run the application
window.mainloop()
