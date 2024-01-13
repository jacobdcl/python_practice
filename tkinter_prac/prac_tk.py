import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


class App:
    def __init__(self, master):
        
        # top of the window
        self.master = master
        master.title("Text-to-Speech Converter") 
        # 'label' text
        self.label = tk.Label(master, text="Enter text to convert:") 
        self.label.pack()
        # text box
        self.textbox = tk.Text(master, height=5) 
        self.textbox.pack()
        # text
        self.language_label = tk.Label(master, text="Select language:") 
        self.language_label.pack()
        # cover of menu
        self.language_var = tk.StringVar() #
        self.language_var.set("en")
        # # drop down menu, set options, tk.OptionMenu()
        self.language_menu = tk.OptionMenu(master, self.language_var, "en", "es", "fr", "de")
        self.language_menu.pack()

        self.convert_button = tk.Button(master, text="Convert", command=self.convert)
        self.convert_button.pack()

    def convert(self):
        text = self.textbox.get("1.0", tk.END)
        language = self.language_var.get()
        try:
            output = gTTS(text=text, lang=language, slow=False)
            file_path = filedialog.asksaveasfilename(defaultextension=".mp3")
            output.save(file_path)

            # Play the MP3 file using the appropriate command for the platform
            if platform.system() == 'Darwin':  # macOS
                command = ['afplay', file_path]
            elif platform.system() == 'Windows':  # Windows
                command = ['start', file_path, '/B', '/MIN']
            else:  # Linux and other Unix-like systems
                command = ['xdg-open', file_path]

            if subprocess.call(command) == 0:
                messagebox.showinfo("Conversion Complete", "The audio file was successfully saved and played.")
            else:
                messagebox.showerror("Playback Error", "There was an error playing the audio file.")
                
        except:
            messagebox.showerror("Conversion Error", "There was an error converting the text to speech.")



root = tk.Tk()
app = App(root)
root.mainloop()