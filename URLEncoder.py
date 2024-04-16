import tkinter as tk
from urllib.parse import quote, unquote


def encode_text() -> None:
    '''
    Function to encode the text from the textbox
    '''
    text = textbox.get("1.0", tk.END).strip()  
    encoded_text = quote(text)           
    result_box.config(state=tk.NORMAL)         
    result_box.delete("1.0", tk.END)           
    result_box.insert(tk.END, encoded_text)    
    result_box.config(state=tk.DISABLED)       


def decode_text() -> None:
    '''
    Function to decode the text from the textbox
    '''
    text = textbox.get("1.0", tk.END).strip()  
    decoded_text = unquote(text)           
    result_box.config(state=tk.NORMAL)         
    result_box.delete("1.0", tk.END)           
    result_box.insert(tk.END, decoded_text)    
    result_box.config(state=tk.DISABLED)       

root = tk.Tk()

root.geometry("500x500")
root.title("URL Encoder")

label = tk.Label(root, text="URL Encoder", font=("Calibri",18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=5, font=("Calibri", 16))
textbox.pack()

button_container = tk.Frame(root)
button_container.pack(pady=10)

encode_button = tk.Button(button_container, text="Encode", font=("Calibri",18), command=encode_text)
encode_button.grid(row=0, column=0, padx=10)

decode_button = tk.Button(button_container, text="Decode", font=("Calibri", 18), command=decode_text)
decode_button.grid(row=0, column=1, padx=10)

result_box = tk.Text(root, height=5, font=("Calibri", 16), state=tk.DISABLED)
result_box.pack()

root.mainloop()
