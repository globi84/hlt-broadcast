Install Manual
==================

## Features

### Current features

* ✅ Verschiedene Szenen für OBS
    * ✅ 3 * Bischofschaft
    * ✅ 3 * Pfahlpräsidentschaft
    * ✅ 3 * Sprecher
    * ✅ Intro / Outro
    * ✅ Abendmahl
    * ✅ Lieder
* ✅ Remote Control von OBS Szenen (Macro Deck)
* ✅ WebGui
    * ✅ Sprecher rollen editieren
    * ✅ Lieder text generator
    * ✅ start von allen Applikationen

### planed Features

* ❌ Remote control von Kamera (damit man unten bei der Familie sitzen kann)
* ❌ Install script
* ❌ WebGui Lieder Titel suche
* ❌ Bugfix

### known issue

* ❌ Lied #200 wird nicht erstellt

## Prerequisits

Alles Installieren

| Applikation | Install über Download                         | Install über winget                   |
| ----------- | --------------------------------------------- | ------------------------------------- |
| OBS         | [Download](https://obsproject.com/de)         | `winget install OBSProject.OBSStudio` |
| Macro Deck  | [Download](https://macrodeck.org/download)    |                                       |
| Zoom        | [Download](https://zoom.us/download)          | `winget install Zoom.Zoom`            |
| Python3     | [Download](https://www.python.org/downloads/) | `winget install Python.Python.3.11`   |

## Install

### OBS

* Szenen importieren `obs\hlt-zoom.json`
* Szene auswählen und richtige Ordner auswählen
* OBS Websocket einschalten und konfigurieren (firewall nicht öffnen)

### Macro Deck

* öffnen und grund config einstellen (hier firewall öffnen)
* schliessen (auch im systray schauen)
* inhalt vom ordner `macro Deck` nach `%appdata%\Macro Deck` Kopieren
* Macrodeck öffnen einstellungen -> Netzwerk das richtige interface auswählen
* Obs plugin konfigurieren

### WebGui

* mit Terminal in den ordner `bin/Webgui` gehen
* `pip install -r requirements.txt` ausführen
* `config.json.skel` zu `config.json` umbenennen und konfigurieren

#### tools

im Projekt enthalten sind auch

* [Bootstrap](https://getbootstrap.com/docs/versions/)
* [jQuerry](https://code.jquery.com/jquery-3.6.1.min.js)
* [chosen](https://github.com/harvesthq/chosen/releases)

## Run

Jetzt muss man einfach `start.cmd` ausführen und alles sollte richtig starten.
