import tkinter as tk
from tkinter import ttk
from defaults import DefaultsUI as dui
from defaults import DefaultsFileManagent as dfm

# UI Stuff

class QRCodeGeneratorGUI():

    root: tk.Tk = tk.Tk()
    
    url_var: tk.StringVar = tk.StringVar()
    title_var: tk.StringVar = tk.StringVar()
    output_dir_var: tk.StringVar = tk.StringVar(value=dfm.OUTPUT_DIR_PATH)
    print_title_var: tk.BooleanVar = tk.BooleanVar(value=True)

    def launch(self):

        self.root.title("QR code generator")

        self.build_url_widget()
        self.build_title_widget()
        self.build_print_title_widget()
        self.build_output_dir_widget()
        
        self.root.mainloop()

    def build_title_widget(self):
        # Title Label
        label_title: ttk.Label = ttk.Label(master=self.root, text="QR code title (optional):")
        label_title.pack(padx=dui.PADX, pady=dui.PADY, anchor="w")

        # Title entry box
        title_entry: ttk.Entry = ttk.Entry(master=self.root, textvariable=self.title_var, width=dui.WIDTH)
        title_entry.pack(padx=dui.PADX, pady=dui.PADY, anchor="w")

        
    def build_url_widget(self):
        # URL label
        label_url: ttk.Label = ttk.Label(master=self.root, text="URL:")
        label_url.pack(padx=dui.PADX, pady=dui.PADY, anchor="w")

        # URL Entry
        url_entry: ttk.Entry = ttk.Entry(master=self.root, textvariable=self.url_var, width=dui.WIDTH)
        url_entry.pack(padx=dui.PADX, pady=dui.PADY, anchor="w")

    def build_output_dir_widget(self):
        # Output directory label
        label_output_dir: ttk.Label = ttk.Label(master=self.root, text="Output directory:")
        label_output_dir.pack(padx=dui.PADX, pady=dui.PADY, anchor="w")

        # Output directory Entry
        output_dir_entry: ttk.Entry = ttk.Entry(master=self.root, textvariable=self.output_dir_var, width=dui.WIDTH)
        output_dir_entry.pack(padx=dui.PADX, pady=dui.PADY, anchor="w")

    def build_print_title_widget(self):
        # Print title checkbox
        print_title_check: ttk.Checkbutton = ttk.Checkbutton(master=self.root, text="Print title", variable=self.print_title_var)
        print_title_check.pack(padx=dui.PADX, pady=dui.PADY, anchor="w")
