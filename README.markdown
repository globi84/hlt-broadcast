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
* ✅ Remote control von Kamera (damit man unten bei der Familie sitzen kann)
* ✅ Install script

### planed Features

* ❌ WebGui Lieder Titel suche
* ❌ Bugfix

### known issue

* ❌ Lied #200 wird nicht erstellt


## Install

### auto install

* run `setup.cmd` as admin

Danach muss folgendes noch gemacht werden:

* config.json Anpassen
  * IP vom ATEM Switcher
  * IP von beiden Kameras
  * zoom einladungslink
  * Kameras so konfigurieren wie du glücklich bist. 😊
* obs öffnen und Pfade zu den Medien setzen
* OBS Websocket passwort ändern: *Werkzeuge -> OBS-websocket-Einstellungen*
* check path in macrodeck macros
* Password für obs-plugin in macrodeck setzen

### manual install

#### Prerequisites

Alles Installieren

| Applikation | Install über Download                         | Install über winget                   |
| ----------- | --------------------------------------------- | ------------------------------------- |
| OBS         | [Download](https://obsproject.com/de)         | `winget install OBSProject.OBSStudio` |
| Macro Deck  | [Download](https://macrodeck.org/download)    |                                       |
| Zoom        | [Download](https://zoom.us/download)          | `winget install Zoom.Zoom`            |
| Python3.10  | [Download](https://www.python.org/downloads/) | `winget install Python.Python.3.10`   |

#### OBS

* obs sollte zu sein.
* Den Ordner `obs-studio` nach `%appdata%\` kopieren.
* obs öffnen und Pfade zu den Medien setzen
* OBS Websocket konfigurieren (firewall nicht öffnen): *Werkzeuge -> OBS-websocket-Einstellungen*
  * Standard Password: `1234.qwer`

  ![image size="500x"](/doku/img/04.png)


#### Macro Deck

* Macro Deck sollte geschlossen sein auch im systray schauen
* Den ordner `Macro Deck` nach `%appdata%\` Kopieren. Fals schon ein ordner vorhanden ist. einfach löschen

  ![image size="500x"](/doku/img/08.png)

* Macro Deck öffnen und Firewall regel zulassen
* einstellungen (unten links) -> Verbindung -> bei Netzwerkadapter: das richtige interface auswählen
* Plugin einstellen (Puzzle Teil) -> OBS-WebSocket Plugin -> konfigurieren

  ![image size="500x"](/doku/img/05.png)

  ![image size="500x"](/doku/img/06.png)

  ![image size="500x"](/doku/img/07.png)

#### WebGui

* mit Terminal in den ordner `bin/Webgui` gehen
* `pip install -r requirements.txt` ausführen

#### tools

im Projekt enthalten sind auch

* [Bootstrap](https://getbootstrap.com/docs/versions/)
* [jQuerry](https://code.jquery.com/jquery-3.6.1.min.js)
* [chosen](https://github.com/harvesthq/chosen/releases)

## Run

Jetzt muss man einfach `start.cmd` ausführen und alles sollte richtig starten.
