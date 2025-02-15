# Secure Data Hiding in Images using Steganography

## 📌 Project Overview
This project implements **Least Significant Bit (LSB) steganography** with **encryption and decryption**, ensuring **secure data concealment** within images. It allows users to **hide confidential information** inside an image while maintaining its visual integrity. The data is first **encrypted**, embedded into the image, and later extracted and decrypted for enhanced security.

## 🚀 Features
- **🔐 Dual-Layer Security** – Data is **encrypted before embedding** for additional protection.
- **🎨 User-Friendly GUI** – Built with **`customtkinter`** for a modern and interactive interface.
- **🖼️ Image Integrity** – Uses **LSB steganography**, ensuring **zero visible distortion**.
- **⚡ Fast & Optimized** – Utilizes **NumPy and Pillow** for efficient pixel manipulation.
- **🔄 Cross-Platform Compatibility** – Works on **Windows and Linux**.
- **📂 Multi-Format Support** – Supports **PNG, JPEG, BMP** image formats.

## 📚 Technologies Used
### **Programming Language:**
- **Python 3.12**

### **Libraries:**
- **Pillow** – Image processing
- **cryptography** – Data encryption & decryption
- **customtkinter** – GUI development
- **numpy** – Optimized pixel manipulation

### **Platforms:**
- **Windows** – Compatible operating systems
- **VS Code** – IDEs for development

## 🔧 Installation & Setup
### **Prerequisites**
Ensure you have **Python 3.12** installed. Then, install the required dependencies:
```bash
pip install pillow cryptography customtkinter numpy
```

### **Running the Application**
```bash
python app.py
```

## 📌 How It Works
1. **Encryption & Embedding:**
   - User inputs **text data**.
   - The data is **encrypted** and embedded into an image using LSB steganography.
   - The modified image is saved as output.

2. **Extraction & Decryption:**
   - The program extracts hidden **encrypted data** from the image.
   - It then **decrypts** the data and displays the original message.

## 🎯 End Users
- **🔐 Cybersecurity Experts** – Securely transmit sensitive data.
- **🕵️‍♂️ Journalists & Whistleblowers** – Protect confidential communications.
- **📂 Digital Forensics Analysts** – Research data concealment techniques.
- **🎓 Students & Researchers** – Learn cryptography and steganography.
- **💼 Businesses** – Protect sensitive business information.

## 🔮 Future Scope
- **🔑 Password-Protected Steganography** – Add **password-based access** to extract hidden data.
- **🧠 AI-Powered Steganalysis Resistance** – Use **machine learning** to evade detection.
- **📱 Mobile & Web Integration** – Extend support to **web and mobile applications**.
- **🖼️ Adaptive Steganography** – Implement **dynamic pixel selection** for improved security.
- **📡 Cloud Storage & Remote Access** – Enable **secure cloud-based storage** of steganographic images.

## 📜 License
This project is licensed under the **MIT License**.

## 🙌 Acknowledgments
Thanks to the **open-source community** for providing valuable resources that made this project possible! 🎉
