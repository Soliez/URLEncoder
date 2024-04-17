import tkinter as tk
import pyperclip
from urllib.parse import quote, unquote




def main() -> None:
    '''
    The UI's main logic
    '''

    def encode_text() -> None:
        '''
        Encodes the text from the input textbox
        '''
        text = textbox.get("1.0", tk.END).strip()  
        encoded_text = quote(text)           
        result_box.config(state=tk.NORMAL)         
        result_box.delete("1.0", tk.END)           
        result_box.insert(tk.END, encoded_text)    
        result_box.config(state=tk.DISABLED)       


    def decode_text() -> None:
        '''
        Decodes the text from the input textbox
        '''
        text = textbox.get("1.0", tk.END).strip()  
        decoded_text = unquote(text)           
        result_box.config(state=tk.NORMAL)         
        result_box.delete("1.0", tk.END)           
        result_box.insert(tk.END, decoded_text)    
        result_box.config(state=tk.DISABLED)       


    def copy_to_clipboard() -> None:
        '''
        Copies the text from the results textbox to the user's clipboard
        '''
        result_box_text = result_box.get("1.0", tk.END).strip()
        pyperclip.copy(result_box_text)


    def clear_result() -> None:
        '''
        Clears the text in the results textbox
        '''
        result_box.config(state=tk.NORMAL)
        result_box.delete("1.0", tk.END)
        result_box.config(state=tk.DISABLED)

    
    def clear_input() -> None:
        '''
        Clears the text in the input textbox
        '''
        textbox.delete("1.0", tk.END)

    
    def paste_input() -> None:
        '''
        Updates the input textbox with the content of the user's clipboard
        '''
        textbox.delete("1.0", tk.END)
        textbox.insert(tk.END, pyperclip.paste())


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
    encode_button.pack(side=tk.LEFT, padx=10)

    decode_button = tk.Button(button_container, text="Decode", font=("Calibri", 18), command=decode_text)
    decode_button.pack(side=tk.LEFT, padx=10)

    paste_button = tk.Button(button_container, text="Paste", font=("Calibri", 18), command=paste_input)
    paste_button.pack(side=tk.LEFT, padx=10)

    clear_input_button = tk.Button(button_container, text="Clear", font=("Calibri", 18), command=clear_input)
    clear_input_button.pack(side=tk.LEFT, padx=10)

    result_box = tk.Text(root, height=5, font=("Calibri", 16), state=tk.DISABLED)
    result_box.pack()

    cc_button_container = tk.Frame(root)
    cc_button_container.pack(pady=10)

    copy_button = tk.Button(cc_button_container, text="Copy", font=("Calibri", 18), command=copy_to_clipboard)
    copy_button.pack(side=tk.LEFT, padx=10)

    clear_button = tk.Button(cc_button_container, text="Clear", font=("Calibri", 18), command=clear_result)
    clear_button.pack(side=tk.LEFT, padx=10)

    root.mainloop()

if __name__ == "__main__":
    main()