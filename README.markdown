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

* Szenen importieren: *Szenensammlung -> Importieren* `obs\hlt-zoom.json`
  [[!img doku/img/02.png size="500x"]]
* Szene auswählen und richtige Ordner auswählen: *Szenensammlung -> HLT-ZOOM*
  [[!img doku/img/03.png size="500x"]]
* OBS Websocket einschalten und konfigurieren (firewall nicht öffnen): *Werkzeuge -> OBS-websocket-Einstellungen*
  [[!img doku/img/04.png size="500x"]]


### Macro Deck

* Macro Deck sollte geschlossen sein auch im systray schauen
* Den ordner `Macro Deck` nach `%appdata%\` Kopieren. Fals schon ein ordner vorhanden ist. einfach löschen
  [[!img doku/img/08.png size="500x"]]
* Macro Deck öffnen und Firewall regel zulassen
* einstellungen (unten links) -> Verbindung -> bei Netzwerkadapter: das richtige interface auswählen
* Plugin einstellen (Puzzle Teil) -> OBS-WebSocket Plugin -> konfigurieren
  [[!img doku/img/05.png size="500x"]]
  [[!img doku/img/06.png size="500x"]]
  [[!img doku/img/07.png size="500x"]]

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
