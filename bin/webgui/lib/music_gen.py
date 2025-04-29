import re
import os
from lib.Quote2Image import convert
import json

def generate_songText(config, songNRs):
    """generate song text images from lds hyms with song nr"""

    scriptRoot = os.path.dirname(os.path.realpath(__file__)) + "\\"

    deletFotos = "del /F /S /Q " + scriptRoot + "\\..\\"+ config["destination"] + "\*"
    os.system(deletFotos)

    with open(scriptRoot + config["source"]["songs"], "r", encoding="utf-8") as f:
        songs = json.load(f)

    for index, songNR in enumerate(songNRs):

        songText = songs[str(songNR)]["Text"]

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

            img.save(scriptRoot + "\\..\\" + config["destination"]+"\\" +
                    str(index+1) + "_" + str(nr+1) + ".png")

def get_songTitles(config):
    """get a list of dict with songnr as key and title as value"""
    scriptRoot = os.path.dirname(os.path.realpath(__file__)) + "\\"
    # Song Json öffnen
    with open(scriptRoot + config["source"]["songs"], "r", encoding="utf-8") as f:
        songs = json.load(f)
    lieder = []
    for b in songs.keys():
        tempnr = b
        temptext = songs[b]["Title"]
        lieder.append({"nr": tempnr, "title": temptext})

    return lieder
