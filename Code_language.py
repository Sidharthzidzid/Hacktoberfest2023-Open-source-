import tkinter as tk

# Define the code language
code_language = {
    'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
    'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
    'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
    'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
    'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A'
}

# Encode a message
def encode_message():
    message = message_entry.get().upper()
    encoded_message = ''.join([code_language.get(char, char) for char in message])
    result_label.config(text=f"Encoded Message: {encoded_message}")

# Decode a message
def decode_message():
    message = message_entry.get().upper()
    decoded_message = ''.join([code_language.get(char, char) for char in message])
    result_label.config(text=f"Decoded Message: {decoded_message}")

# Create the main window
window = tk.Tk()
window.title("Code Language Program")

# Create and configure widgets
message_label = tk.Label(window, text="Enter a message:")
message_entry = tk.Entry(window, width=50)
encode_button = tk.Button(window, text="Encode", command=encode_message)
decode_button = tk.Button(window, text="Decode", command=decode_message)
result_label = tk.Label(window, text="Result will be displayed here", font=("Arial", 12), wraplength=300)
copyright_label = tk.Label(window, text="\u00A9 2023 Sidharth v nair. All rights reserved", font=("Arial", 10), fg="#888")

# Place widgets on the window
message_label.pack()
message_entry.pack()
encode_button.pack()
decode_button.pack()
result_label.pack()
copyright_label.pack()

window.mainloop()
