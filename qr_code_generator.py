import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox
from PIL import Image, ImageTk
import qrcode
from qrcode.image.svg import SvgImage, SvgFillImage

class QRCodeGenerator(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title('QR Code Generator')
		self.geometry('400x530')

		self.label = tk.Label(self, text="Gib deinen Text oder URL ein:")
		self.label.pack(pady=10)

		self.text_entry = tk.Entry(self)
		self.text_entry.pack(pady=5)

		self.color_button = tk.Button(self, text="Vordergrundfarbe wählen", command=self.choose_foreground_color)
		self.color_button.pack(pady=5)

		self.bg_color_button = tk.Button(self, text="Hintergrundfarbe wählen", command=self.choose_background_color)
		self.bg_color_button.pack(pady=5)

		self.generate_button = tk.Button(self, text="QR-Code generieren", command=self.generate_qr_code)
		self.generate_button.pack(pady=15)

		self.qr_image_label = tk.Label(self)
		self.qr_image_label.pack(pady=15)

		self.save_button = tk.Button(self, text="QR-Code speichern", command=self.save_qr_code)
		self.save_button.pack(pady=5)
		self.save_button['state'] = tk.DISABLED

		self.foreground_color = 'black'  # Standardfarbe für den Vordergrund
		self.background_color = 'white'  # Standardfarbe für den Hintergrund

	def choose_foreground_color(self):
		color_code = colorchooser.askcolor(title="Wähle eine Vordergrundfarbe")[1]
		if color_code:
			self.foreground_color = color_code

	def choose_background_color(self):
		color_code = colorchooser.askcolor(title="Wähle eine Hintergrundfarbe")[1]
		if color_code:
			self.background_color = color_code

	def generate_qr_code(self):
		data = self.text_entry.get()
		if not data:
			messagebox.showerror("Fehler", "Bitte gib einen Text oder URL ein.")
			return

		qr = qrcode.QRCode(
			version=1,
			error_correction=qrcode.constants.ERROR_CORRECT_H,
			box_size=10,
			border=4,
		)
		qr.add_data(data)
		qr.make(fit=True)
		self.qr_code = qr  # Speichere das QRCode-Objekt zur späteren Verwendung

		# Erzeuge ein Bild für die Anzeige in der GUI
		img = qr.make_image(fill_color=self.foreground_color, back_color=self.background_color).convert('RGB')
		img_path = "temp_qr_code.png"
		img.save(img_path)

		self.show_qr_code(img_path)
		self.save_button['state'] = tk.NORMAL

	def show_qr_code(self, filepath):
		if filepath.endswith('.png'):
			img = Image.open(filepath)
			img = img.resize((250, 250), Image.Resampling.LANCZOS)
			tk_img = ImageTk.PhotoImage(img)
			self.qr_image_label.configure(image=tk_img)
			self.qr_image_label.image = tk_img
		else:
			# Update UI to reflect SVG is loaded, but cannot be displayed in a Tkinter label directly.
			self.qr_image_label.configure(text="SVG QR-Code generiert. Bitte zum Anzeigen die SVG-Datei öffnen.")


	def save_qr_code(self):
		if self.qr_code is None:
			messagebox.showerror("Fehler", "Kein QR-Code zum Speichern vorhanden.")
			return

		file_path = filedialog.asksaveasfilename(defaultextension='.png',
												filetypes=[("PNG-Dateien", "*.png"), ("SVG-Dateien", "*.svg"), ("Alle Dateien", "*.*")])
		if file_path:
			if file_path.endswith('.svg'):
				# SVG speichern, öffne die Datei im binären Schreibmodus
				with open(file_path, "wb") as f:
					img = self.qr_code.make_image(fill_color=self.foreground_color, back_color=self.background_color, image_factory=SvgFillImage)
					img.save(f)
			else:
				# PNG speichern
				img = self.qr_code.make_image(fill_color=self.foreground_color, back_color=self.background_color).convert('RGB')
				img.save(file_path)
			messagebox.showinfo("Erfolg", "QR-Code erfolgreich gespeichert.")


if __name__ == "__main__":
	app = QRCodeGenerator()
	app.mainloop()
