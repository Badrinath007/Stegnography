import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from encryption import Encryptor
from decryption import Decryptor

class SteganographyApp(ctk.CTk):
    def __init__(self):
        ctk.set_appearance_mode("Dark")  # Set default theme first
        ctk.CTk.__init__(self)
        self.title("Secure Data Hiding")
        self.geometry("750x650")
        self.resizable(False, False)
        
        # Encryption & Decryption Classes
        self.encryptor = Encryptor()
        self.decryptor = Decryptor()
        
        # Variables
        self.secret_message = ctk.StringVar()
        self.input_image_path = None
        self.encoded_image_path = None
        self.displayed_image = None  # Store image reference to prevent garbage collection
        
        # Create a grid layout
        self.columnconfigure(0, weight=1)  # Center content
        
        # Reset Button (Top Left)
        self.reset_btn = ctk.CTkButton(self, text="Reset", command=self.reset_app, width=100)
        self.reset_btn.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        
        # Exit Button (Top Right)
        self.exit_btn = ctk.CTkButton(self, text="Exit", command=self.quit, width=100)
        self.exit_btn.grid(row=0, column=1, padx=20, pady=10, sticky="e")
        
        # Center Frame for All UI Elements
        self.center_frame = ctk.CTkFrame(self)
        self.center_frame.grid(row=1, column=0, columnspan=2, pady=10, padx=10)
        self.center_frame.columnconfigure(0, weight=1)  # Center content
        
        # UI Elements inside Center Frame
        self.label = ctk.CTkLabel(self.center_frame, text="Enter Message:")
        self.label.grid(row=0, column=0, pady=5)
        
        self.entry = ctk.CTkEntry(self.center_frame, textvariable=self.secret_message, width=400)
        self.entry.grid(row=1, column=0, pady=5)
        
        self.upload_btn = ctk.CTkButton(self.center_frame, text="Upload Image", command=self.upload_image)
        self.upload_btn.grid(row=2, column=0, pady=10)
        
        self.image_label = ctk.CTkLabel(self.center_frame, text="No Image Selected", width=200, height=200)
        self.image_label.grid(row=3, column=0, pady=10)
        
        self.encrypt_btn = ctk.CTkButton(self.center_frame, text="Encrypt & Hide", command=self.encrypt_data)
        self.encrypt_btn.grid(row=4, column=0, pady=5)
        
        self.decrypt_btn = ctk.CTkButton(self.center_frame, text="Extract & Decrypt", command=self.decrypt_data)
        self.decrypt_btn.grid(row=5, column=0, pady=5)
        
        # Light/Dark Mode Toggle (Below Main Frame)
        self.toggle_frame = ctk.CTkFrame(self)
        self.toggle_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.toggle_label = ctk.CTkLabel(self.toggle_frame, text="Theme Mode:")
        self.toggle_label.grid(row=0, column=0, padx=10)
        
        self.theme_mode = ctk.StringVar(value="Dark")
        self.toggle_btn = ctk.CTkSwitch(self.toggle_frame, text="Light Mode", command=self.toggle_theme, variable=self.theme_mode, onvalue="Light", offvalue="Dark")
        self.toggle_btn.grid(row=0, column=1)
    
    def upload_image(self):
        """Upload an image and display it."""
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        self.load_image(file_path)
    
    def load_image(self, file_path):
        if file_path:
            self.input_image_path = file_path
            img = Image.open(file_path).resize((200, 200))
            self.displayed_image = ImageTk.PhotoImage(img)
            self.image_label.configure(image=self.displayed_image, text="")
            self.image_label.image = self.displayed_image  # Store reference to avoid garbage collection
    
    def encrypt_data(self):
        """Encrypt message and hide in image."""
        if not self.input_image_path or not self.secret_message.get():
            messagebox.showerror("Error", "Image and message required!")
            return
        
        encrypted_message = self.encryptor.encrypt_message(self.secret_message.get())
        message, encoded_image_path = self.encryptor.encode_image(self.input_image_path, encrypted_message)
        
        if encoded_image_path:
            self.encoded_image_path = encoded_image_path
            messagebox.showinfo("Success", "Encryption Successful! Encoded image saved.")
    
    def decrypt_data(self):
        """Extract and decrypt message from image."""
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            encrypted_data = self.decryptor.decode_image(file_path)
            if encrypted_data:
                decrypted_message = self.decryptor.decrypt_message(encrypted_data)
                messagebox.showinfo("Decoded Message", f"🔓 Decoded Message: {decrypted_message}")
    
    def reset_app(self):
        """Reset message input and image preview."""
        self.secret_message.set("")
        self.input_image_path = None
        self.encoded_image_path = None
        self.displayed_image = None  # Store image reference to prevent garbage collection

        # Remove the image reference safely
        self.image_label.configure(image="", text="No Image Selected")
        # self.image_label.image = None  # Important: Reset image reference
        
        # # Check and delete displayed image if it exists
        if hasattr(self, "displayed_image"):
            del self.displayed_image  # Remove stored image reference
        
    
    def toggle_theme(self):
        """Switch between light and dark mode."""
        mode = self.theme_mode.get()
        ctk.set_appearance_mode(mode)
        self.toggle_btn.configure(text="Dark Mode" if mode == "Light" else "Light Mode")

if __name__ == "__main__":
    app = SteganographyApp()
    app.mainloop()