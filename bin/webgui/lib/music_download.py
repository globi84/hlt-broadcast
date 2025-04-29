import subprocess
import re
import os
from lib.Quote2Image import convert
import json

def generate_songText(config, songNRs):
    """generate song text images from lds hyms with song nr"""

    scriptRoot = os.path.dirname(os.path.realpath(__file__)) + "\\"

    deletFotos = "del /F /S /Q " + scriptRoot + "\\..\\"+ config["destination"] + "\*"
    os.system(deletFotos)

    songs = {}
    titles = get_songTitles(config)

    for index, songNR in enumerate(songNRs):

        #songNR = 122
        # Inhaltsverzeichniss öffnen
        toc = open(scriptRoot + config["source"]["toc"], "r", encoding="utf-8")

        # Urls auslesen
        x = re.search('(?s).+href="(?P<songuri>.+?)".+?songNumber.+?>'+str(songNR), toc.read())

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
                'id="[^"]+">(?:<span class="verse-number">[^<]+<\/span>)?(.*?)<\/p>', songHtml[i])
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
                        if songPhrase:
                            songText.append(songPhrase)
                        break
                    i += 1
            i += 1
        
        songs[songNR]= {
            "Text": songText,
            "Title": titles[str(songNR)]
        }

        # Bild erstellen
        #for nr, strophe in enumerate(songText):    
#
        #    img = convert(
        #        quote        = strophe,
        #        author       = ("#" + str(songNR)),
        #        fg           = "white",
        #        image        = scriptRoot + config["source"]["background"],
        #        font_size    = 32,
        #        font_file    = scriptRoot + config["source"]["font"],
        #        width        = 530,
        #        height       = 1000,
        #        border_color = "black"
        #    )
#
        #    img.save(scriptRoot + "\\..\\" + config["destination"]+"\\" +
        #            str(index+1) + "_" + str(nr+1) + ".png")
    songs
    with open("new_songs.json", "w", encoding="utf-8") as fp:
        json.dump(songs, fp, ensure_ascii=False)



def get_songTitles(config):
    """get a list of dict with songnr as key and title as value"""
    scriptRoot = os.path.dirname(os.path.realpath(__file__)) + "\\"
    # Inhaltsverzeichniss öffnen
    toc = open(scriptRoot + config["source"]["toc"], "r", encoding="utf8")
    toc_read = toc.read()
    # Urls auslesen
    a = re.findall('songNumber.+?>(?P<songnr>\d+)<.+?<span>(?P<songtext>(.|\n)+?)</span>', toc_read)
    #lieder = []
    lieder = {}
    for b in a:
        tempnr = b[0]
        temptext = b[1].replace("\n","")
        temptext = ' '.join(temptext.split())
        #lieder.append({"nr":tempnr,"title":temptext})
        lieder[tempnr] = temptext

    return lieder
