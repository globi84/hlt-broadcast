from os import  path,system
from os.path import exists
import json

from lib.music_download import generate_songText,get_songTitles

rootPath = path.dirname(path.realpath(__file__))
configFile = rootPath + "\\..\\..\\config.json"

if exists(configFile):
    f = open(configFile, "r", encoding="utf8").read()
    config = json.loads(f)
    config = config["webgui"]
    speakerPaths = config["sprecher"]
else:
    print("config file does not exist: "+ configFile)
    exit()

# read from inhaltsverzeichniss.html all songs and create a new_songs.json file

b = get_songTitles(config)
generate_songText(config, b.keys())
