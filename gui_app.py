#GUI app
import tkinter as tk
from tkinter import ttk
from defaults import DefaultsUI as dui
from defaults import DefaultsFileManagent as dfm
from PIL import Image, ImageTk

class QRCodeGeneratorGUI:

    root: tk.Tk = tk.Tk()
    frame_general: tk.LabelFrame = tk.LabelFrame(
        master=root, text="General", padx=10, pady=10
    )
    frame_advanced: tk.LabelFrame = tk.LabelFrame(
        master=root, text="Advanced", padx=10, pady=10
    )
    frame_image: tk.LabelFrame = tk.LabelFrame(
        master=root, text="QR Code Image", padx=10, pady=10
        )

    url_var: tk.StringVar = tk.StringVar()
    title_var: tk.StringVar = tk.StringVar()
    output_dir_var: tk.StringVar = tk.StringVar(value=dfm.OUTPUT_DIR_PATH)
    print_title_var: tk.BooleanVar = tk.BooleanVar(value=True)
    file_prefix_var: tk.StringVar = tk.StringVar(value=dfm.FILE_PREFIX)

    def build_layout(self):

        self.frame_general.pack(padx=10, pady=10, fill="both", expand=True)
        self.frame_advanced.pack(padx=10, pady=10, fill="both", expand=True)
        self.frame_image.pack(padx=10, pady=10, fill="both", expand=True)

    def launch(self):

        self.root.title("QR code generator")
        self.build_layout()

        # Top frame
        self.build_url_widget()
        self.build_title_widget()
        self.build_print_title_widget()

        # Bottom frame
        self.build_output_dir_widget()
        self.build_file_prefix_widget()

        # Right frame
        self.build_image_widget()

        # Main buttons
        self.build_save_widget()

        self.root.mainloop()

    def build_title_widget(self):
        # Title Label
        label_title: ttk.Label = ttk.Label(
            master=self.frame_general, text="QR code title (optional):"
        )
        label_title.pack(padx=dui.PADX, pady=dui.PADY, anchor="w")

        # Title entry box
        title_entry: ttk.Entry = ttk.Entry(
            master=self.frame_general, textvariable=self.title_var, width=dui.WIDTH
        )
        title_entry.pack(padx=dui.PADX, pady=dui.PADY, anchor="w")

    def build_url_widget(self):
        # URL label
        label_url: ttk.Label = ttk.Label(master=self.frame_general, text="URL:")
        label_url.pack(padx=dui.PADX, pady=dui.PADY, anchor="w")

        # URL Entry
        url_entry: ttk.Entry = ttk.Entry(
            master=self.frame_general, textvariable=self.url_var, width=dui.WIDTH
        )
        url_entry.pack(padx=dui.PADX, pady=dui.PADY, anchor="w")

    def build_output_dir_widget(self):
        # Output directory label
        label_output_dir: ttk.Label = ttk.Label(
            master=self.frame_advanced, text="Output directory:"
        )
        label_output_dir.pack(padx=dui.PADX, pady=dui.PADY, anchor="w")

        # Output directory Entry
        output_dir_entry: ttk.Entry = ttk.Entry(
            master=self.frame_advanced,
            textvariable=self.output_dir_var,
            width=dui.WIDTH,
        )
        output_dir_entry.pack(padx=dui.PADX, pady=dui.PADY, anchor="w")

    def build_print_title_widget(self):
        # Print title checkbox
        print_title_check: ttk.Checkbutton = ttk.Checkbutton(
            master=self.frame_general, text="Print title", variable=self.print_title_var
        )
        print_title_check.pack(padx=dui.PADX, pady=dui.PADY, anchor="w")

    def build_file_prefix_widget(self):
        # File prefix label
        label_file_prefix: ttk.Label = ttk.Label(
            master=self.frame_advanced, text="File prefix:"
        )
        label_file_prefix.pack(padx=dui.PADX, pady=dui.PADY, anchor="w")

        # File prefix entry
        file_prefix_entry: ttk.Entry = ttk.Entry(
            master=self.frame_advanced,
            textvariable=self.file_prefix_var,
            width=dui.WIDTH,
        )
        file_prefix_entry.pack(padx=dui.PADX, pady=dui.PADY, anchor="w")

    def build_save_widget(self):
        save_button: ttk.Button = ttk.Button(
            master=self.root, text="Save Image", command=self.save_widget_on_click
        )
        save_button.pack(padx=dui.PADX, pady=dui.PADY, anchor="w")

    def save_widget_on_click(self):
        print("clicked boby")

    def build_image_widget(self):
        pass
        #image: ttk.
