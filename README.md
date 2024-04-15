# QR-Code Generator

Basierend auf deinen aktualisierten Informationen habe ich das README angepasst, um die Details zur `requirements.txt` und den spezifischen Inhalt der `build.bat` Datei zu reflektieren. Hier ist das überarbeitete README für deinen QR Code Generator:

```markdown
# QR Code Generator

Dieses Projekt implementiert einen QR Code Generator mit einer grafischen Benutzeroberfläche, erstellt mit Python und tkinter. Nutzer können Text oder URLs eingeben, um QR-Codes zu generieren und diese als PNG-Datei zu speichern.

## Voraussetzungen

Um dieses Projekt auszuführen, müssen Sie Python und Pip installiert haben. Python kann von [python.org](https://www.python.org/downloads/) heruntergeladen und installiert werden.

## Installation

Laden Sie das Projekt herunter und navigieren Sie im Terminal oder in der Kommandozeile in das Projektverzeichnis.

### Abhängigkeiten installieren

Das Projekt verwendet eine `requirements.txt`, die alle benötigten Pakete auflistet:

- `Pillow`
- `qrcode`
- `pyinstaller`

Um die Abhängigkeiten zu installieren, führen Sie:

```bash
pip install -r requirements.txt
```

## Build

Das Projekt verwendet eine `build.bat` Batch-Datei für den Build-Prozess. Führen Sie die folgenden Schritte aus, um die Anwendung zu bauen:

1. Öffnen Sie ein Terminal oder eine Kommandozeile.
2. Navigieren Sie zum Verzeichnis des Projekts.
3. Führen Sie die `build.bat` Datei aus, die die folgenden Befehle enthält:

```cmd
pip install -r requirements.txt
pyinstaller --onefile --windowed qr_code_generator.py
```

Dies kompiliert die Python-Datei in eine ausführbare `.exe`-Datei unter Verwendung von PyInstaller, die einfach verteilt und ausgeführt werden kann.

## Nutzung

Nach dem Build-Prozess finden Sie die ausführbare Datei im `dist` Verzeichnis. Starten Sie die Anwendung, indem Sie die `.exe` Datei ausführen. Die GUI erlaubt die Eingabe von Text oder URLs, woraus dann QR-Codes generiert und angezeigt werden können.

## Features

- Eingabe von Text oder URLs zur Generierung von QR-Codes.
- Anzeige des generierten QR-Codes in der GUI.
- Möglichkeit, den generierten QR-Code als PNG-Datei zu speichern.

## Support

Bei Fragen oder Problemen mit der Installation oder Nutzung der Anwendung können Sie ein Issue im GitHub-Repo dieses Projekts erstellen.

## Beitrag

Beiträge zu diesem Projekt sind willkommen. Sie können das Projekt forken, Änderungen vornehmen und einen Pull Request einreichen.

## Lizenz

Dieses Projekt ist unter der MIT Lizenz lizenziert. Details finden Sie in der `LICENSE` Datei.
