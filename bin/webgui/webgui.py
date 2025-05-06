from flask import Flask, render_template, abort, flash, url_for, redirect, request
from jinja2 import TemplateNotFound
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField
from wtforms.validators import input_required, length

from os import  path,system
from os.path import exists
import json
from lib.speakers import get_speaker,get_speakers,set_speaker
from lib.music_gen import generate_songText,get_songTitles

class EditSpeakerForm(FlaskForm):
    name = StringField("Name", validators=[input_required(), length(max=64)])
    info = StringField("Info", validators=[input_required(), length(max=64)])
    position = StringField("position", validators=[ length(max=64)])
    submit = SubmitField('Speichern')

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

app  = Flask(__name__)
app.config['SECRET_KEY'] = ']\Z_GA<+*41&b\]Z1aJ9TyEs2NJM9cJl=6'

songTitles = get_songTitles(config)


@app.route('/', methods=["GET", "POST"])
def root():
    if request.method == "POST":
        songList = []
        formSongs = ["songNR1","songNR2","songNR3","songNR4","songNR5","songNR6"]
        for formsong in formSongs:
            if request.form.get(formsong):
                songList.append(request.form.get(formsong))
        generate_songText(config, songList)
        return redirect(url_for("root", _anchor='schritt3'))
    speakersContent = {}
    for speakerCategory in speakerPaths.keys():
        path = rootPath +"\\"+ speakerPaths[speakerCategory]
        speakersContent[speakerCategory] = get_speakers(path)
    try:
        return render_template('index.html.j2', speakersContent=speakersContent, songTitles=songTitles)
    except TemplateNotFound:
        abort(404)

@app.route('/speakers')
def get_flaskSpeakers():
    speakersContent = {}
    for speakerCategory in speakerPaths.keys():
        speakersContent[speakerCategory] = get_speakers(speakerPaths[speakerCategory])
    try:
        return render_template('speakers.html.j2', speakersContent=speakersContent)
    except TemplateNotFound:
        abort(404)

@app.route('/speakers/edit/<speakerCategory>/<position>', methods=["Get", "POST"])
def edit_flaskSpeaker(speakerCategory, position):
    speaker = get_speaker(speakerPaths[speakerCategory], position)
    form = EditSpeakerForm()
    form.name.data     = speaker['name']
    form.info.data     = speaker['info']
    form.position.data = speaker['position']
    if form.is_submitted():
        if form.validate():
            updatedSpeaker = {
                'name': request.form['name'],
                'info': request.form['info'],
                'position': speaker['position']
            }

            set_speaker(speakerPaths[speakerCategory], updatedSpeaker)
            flash("Changes saved", "success")
            return redirect(url_for("root", _anchor='schritt2'))
        else:
            flash("Invalid input", "danger")
    return render_template(
        "edit_speaker.html.j2",
        speakerCategory=speakerCategory,
        position=position,
        form=form
    )

@app.route('/start-zoom')
def restart_allApps():

    system("powershell \".\\lib\\restart-apps.ps1 \'"+ configFile +"\'\"")
    return redirect(url_for("root", _anchor='schritt4'))

if __name__ == "__main__":
    app.run()
