import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate the password
def generate_password():
    # Get the answers from the user input
    answer1 = entry_name.get()
    answer2 = entry_birthdate.get()
    answer3 = entry_petname.get()

    # Check if all answers are filled in
    if not answer1 or not answer2 or not answer3:
        messagebox.showwarning("Input Error", "Please fill in all the fields.")
        return

    # Get the selected password length
    try:
        password_length = int(password_length_var.get())
    except ValueError:
        messagebox.showwarning("Input Error", "Please select a valid password length.")
        return

    # Combine the answers to form a structured base string
    base_string = f"{answer1}#{answer2}#{answer3}"

    # Ensure the base string is not too short
    if len(base_string) > password_length:
        base_string = base_string[:password_length]  # Trim the base string if it's too long

    # Calculate how many random characters are needed to meet the password length
    random_characters_needed = password_length - len(base_string)
    
    # Generate the random characters to fill the rest
    random_characters = random.choices(string.ascii_letters + string.digits + string.punctuation, k=random_characters_needed)

    # Combine the base string with random characters
    combined = list(base_string + ''.join(random_characters))
    
    # Shuffle the combined string to make the password more secure
    random.shuffle(combined)

    # Create the final password
    final_password = ''.join(combined)[:password_length]  # Ensure password is the correct length
    label_password.config(text=f"Your Password: {final_password}")

# Function to toggle light/dark mode
def toggle_theme():
    if is_dark_mode.get():
        # Dark Mode
        root.config(bg='#2E2E2E')
        frame.config(bg='#2E2E2E')
        label_name.config(bg='#2E2E2E', fg='#FFFFFF')
        label_birthdate.config(bg='#2E2E2E', fg='#FFFFFF')
        label_petname.config(bg='#2E2E2E', fg='#FFFFFF')
        label_length.config(bg='#2E2E2E', fg='#FFFFFF')
        label_password.config(bg='#2E2E2E', fg='#FFFFFF')
        button_generate.config(bg='#4B4B4B', fg='#FFFFFF', activebackground='#5A5A5A', relief="solid")
        password_length_menu.config(bg='#4B4B4B', fg='#FFFFFF')
    else:
        # Light Mode
        root.config(bg='#F0F0F0')
        frame.config(bg='#F0F0F0')
        label_name.config(bg='#F0F0F0', fg='#000000')
        label_birthdate.config(bg='#F0F0F0', fg='#000000')
        label_petname.config(bg='#F0F0F0', fg='#000000')
        label_length.config(bg='#F0F0F0', fg='#000000')
        label_password.config(bg='#F0F0F0', fg='#000000')
        button_generate.config(bg='#D1D1D1', fg='#000000', activebackground='#C0C0C0', relief="solid")
        password_length_menu.config(bg='#D1D1D1', fg='#000000')

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x450")  # Set window size
root.resizable(True, True)  # Allow resizing the window

# Boolean variable for dark mode using a Checkbutton (switch)
is_dark_mode = tk.BooleanVar(value=False)

# Create a frame to contain all widgets (for better layout)
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Create labels and entry fields for personal questions
label_name = tk.Label(frame, text="What is your full name?")
label_name.pack(pady=5)
entry_name = tk.Entry(frame)
entry_name.pack(pady=5)

label_birthdate = tk.Label(frame, text="What is your birthdate? (e.g., 01-01-1990)")
label_birthdate.pack(pady=5)
entry_birthdate = tk.Entry(frame)
entry_birthdate.pack(pady=5)

label_petname = tk.Label(frame, text="What is your pet's name?")
label_petname.pack(pady=5)
entry_petname = tk.Entry(frame)
entry_petname.pack(pady=5)

# Create label and option menu for password length
label_length = tk.Label(frame, text="Select password length:")
label_length.pack(pady=5)

password_length_var = tk.StringVar(value='4')  # Default value
password_length_menu = tk.OptionMenu(frame, password_length_var, '4', '6', '8')
password_length_menu.pack(pady=5)

# Button to generate the password
button_generate = tk.Button(frame, text="Generate Password", command=generate_password, relief="solid")
button_generate.pack(pady=20)

# Label to display the generated password
label_password = tk.Label(frame, text="Your Password: ")
label_password.pack(pady=5)

# Switch to toggle between light and dark modes
mode_switch = tk.Checkbutton(root, text="Dark Mode", variable=is_dark_mode, onvalue=True, offvalue=False, command=toggle_theme)
mode_switch.pack(pady=10)

# Run the main loop
root.mainloop()
