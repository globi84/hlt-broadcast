from flask import Flask, render_template, abort, flash, url_for, redirect, request
from jinja2 import TemplateNotFound
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField
from wtforms.validators import input_required, length

from os import  path,system
from os.path import exists
import json
from lib.speakers import get_speaker,get_speakers,set_speaker
from lib.music_gen import generate_songText

class EditSpeakerForm(FlaskForm):
    name = StringField("Name", validators=[input_required(), length(max=64)])
    info = StringField("Info", validators=[input_required(), length(max=64)])
    position = StringField("position", validators=[ length(max=64)])
    submit = SubmitField('Speichern')

root = path.dirname(path.realpath(__file__))
configFile = root + "\config.json"

if exists(configFile):
    f = open(configFile, "r", encoding="utf8").read()
    config = json.loads(f)
    speakerPaths = config["sprecher"]
else:
    print("config file does not exist: "+ configFile)
    exit()

app  = Flask(__name__)
app.config['SECRET_KEY'] = ']\Z_GA<+*41&b\]Z1aJ9TyEs2NJM9cJl=6'


@app.route('/', methods=["GET", "POST"])
def root():
    if request.method == "POST":
        if request.form.getlist('songNR'):
            generate_songText(config, request.form.getlist('songNR'))
            return redirect(url_for("root", _anchor='schritt3'))
        else:
            flash("Invalid input", "danger")
    speakersContent = {}
    for speakerCategory in speakerPaths.keys():
        speakersContent[speakerCategory] = get_speakers(speakerPaths[speakerCategory])
    try:
        return render_template('index.html.j2', speakersContent=speakersContent)
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

app.run()
