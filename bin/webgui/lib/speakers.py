from os import listdir
from os.path import isfile, join

def get_speakers(speakerRoot):
    """return a list of speakers infos"""

    speakers = []

    for file in listdir(speakerRoot):
        if "_info" not in file:
            filePath = join(speakerRoot, file)
            if isfile(filePath):
                speaker = open(filePath, "r", encoding="utf8").read()
                info    = open(filePath.replace(".txt", "_info.txt"), "r", encoding="utf8").read()
                speakers.append({ 'name': speaker, 'info': info, 'position': file.replace(".txt","")})

    return speakers

def get_speaker( speakerRoot, position):
    """return a dict of speaker infos"""
    speakers = get_speakers(speakerRoot)

    for speaker in speakers:
        if speaker['position'] == position:
            return speaker

def set_speaker(speakerRoot, speaker):
    """set a speaker text"""
    f = open(speakerRoot+"\\"+speaker['position']+".txt", "w", encoding="utf8")
    f.write(speaker['name'])
    f.close

    f = open(speakerRoot+"\\"+speaker['position']+"_info.txt", "w", encoding="utf8")
    f.write(speaker['info'])
    f.close

def set_speakers(speakerRoot, speakers):
    """set a speaker text"""

    for speaker in speakers.keys():
        f = open(speakerRoot+"\\"+speaker+".txt", "w", encoding="utf8")
        f.write(speakers[speaker])
        f.close
