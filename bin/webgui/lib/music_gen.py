import subprocess
import re
import os
from lib.Quote2Image import convert

def generate_songText(config, songNRs):
    """generate song text images from lds hyms with song nr"""

    scriptRoot = os.path.dirname(os.path.realpath(__file__)) + "\\"

    deletFotos = "del /F /S /Q " + config["destination"] + "\*"
    os.system(deletFotos)

    for index, songNR in enumerate(songNRs):

        #songNR = 122
        # Inhaltsverzeichniss öffnen
        toc = open(scriptRoot + config["source"]["toc"], "r")

        # Urls auslesen
        x = re.search('href="(?P<songuri>.+)"\s+id=li'+str(songNR), toc.read())

        # Lied Holen
        r = subprocess.run(
            ["curl", (config["baseURI"] + x['songuri'])], stdout=subprocess.PIPE)

        # Text raus Holen
        songHtml = r.stdout.decode('utf-8').split("\n")
        songText = []
        i = 0
        while i < len(songHtml):
            songPhrase = ""
            regStrophe = re.search(
                '<p class="line" data-aid.+">\d\. </span>', songHtml[i])
            if regStrophe:
                while i < len(songHtml):
                    regSong = re.search(
                        '<p class="line" data-aid.+">(.+?)</p>', songHtml[i])
                    regEndStanza = re.search(
                        '(<div class="stanza">)|(<div class="citation-info">)', songHtml[i])
                    regNL = re.search('<div class="chorus">', songHtml[i])
                    if regNL:
                        songPhrase += "\n\n"
                    elif regSong:
                        songPhrase += regSong[1].replace('</span>', '') + " "
                    elif regEndStanza:
                        songText.append(songPhrase)
                        break
                    i += 1
            i += 1

        # Bild erstellen
        for nr, strophe in enumerate(songText):
            img = convert(
                quote        = strophe,
                author       = ("#" + str(songNR)),
                fg           = "white",
                image        = scriptRoot + config["source"]["background"],
                font_size    = 32,
                font_file    = scriptRoot + config["source"]["font"],
                width        = 530,
                height       = 1000,
                border_color = "black"
            )

            img.save(config["destination"]+"\\" +
                    str(index+1) + "_" + str(nr+1) + ".png")
