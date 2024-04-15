import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import qrcode

class QRCodeGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('QR Code Generator')
        self.geometry('400x500')

        self.label = tk.Label(self, text="Gib deinen Text oder URL ein:")
        self.label.pack(pady=10)

        self.text_entry = tk.Entry(self)
        self.text_entry.pack(pady=5)

        self.generate_button = tk.Button(self, text="QR-Code generieren", command=self.generate_qr_code)
        self.generate_button.pack(pady=15)

        # Initialer Platzhalter als Label
        self.placeholder_label = tk.Label(self, text="Simon Marcel Linden", justify=tk.CENTER)
        self.placeholder_label.pack(pady=15)

        self.qr_image_label = tk.Label(self)
        self.qr_image_label.pack(pady=15)

        self.save_button = tk.Button(self, text="QR-Code speichern", command=self.save_qr_code)
        self.save_button.pack(pady=5)
        self.save_button['state'] = tk.DISABLED  # Disabled bis ein QR-Code generiert wurde

        self.qr_image = None  # Hält das PIL Image Objekt des QR-Codes

    def generate_qr_code(self):
        data = self.text_entry.get()
        if data.strip() == "":
            tk.messagebox.showerror("Fehler", "Bitte gib einen Text oder URL ein.")
            return

        self.create_qr_code(data)
        self.placeholder_label.pack_forget()  # Entferne den Platzhalter-Text
        self.save_button['state'] = tk.NORMAL  # Aktiviere den Speichern-Button

    def create_qr_code(self, data):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        self.qr_image = qr.make_image(fill='black', back_color='white').convert('RGB')

        img_path = "temp_qr_code.png"
        self.qr_image.save(img_path)
        self.show_qr_code(img_path)

    def show_qr_code(self, filepath):
        img = Image.open(filepath)
        img = img.resize((250, 250), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
        self.qr_image_label.configure(image=img)
        self.qr_image_label.image = img

    def save_qr_code(self):
        if self.qr_image is None:
            tk.messagebox.showerror("Fehler", "Kein QR-Code zum Speichern vorhanden.")
            return
        file_path = filedialog.asksaveasfilename(defaultextension='.png',
                                                 filetypes=[("PNG-Dateien", "*.png"), ("Alle Dateien", "*.*")])
        if file_path:
            self.qr_image.save(file_path)
            tk.messagebox.showinfo("Erfolg", "QR-Code erfolgreich gespeichert.")

if __name__ == "__main__":
    app = QRCodeGenerator()
    app.mainloop()
