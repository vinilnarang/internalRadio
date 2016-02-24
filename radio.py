import json
import subprocess
from pprint import pformat
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

songs_file = "songs.json"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/addSong', methods=['GET', 'POST'])
def addSong():
    if request.method == 'GET':
        return render_template('addSong.html')
    elif request.method == 'POST':
        url = request.form['url']
        with open(songs_file) as fo:
            obj = json.load(fo)
        obj.append(url)
        with open(songs_file, "w") as fo:
            json.dump(obj, fo)
        return redirect(url_for('listSongs'))


@app.route('/listSongs')
def listSongs():
    #x = subprocess.check_output(['wc','-l','songs.txt'])
    #numLines = x.split(" ")[0]
    #l = []
    #with open(songs_file,"r") as f:
    #    for line in f:
    #        l.append(line[:-1])
    #return pformat(l)
    with open(songs_file) as fo:
        songs = json.load(fo)
    return render_template('listSongs.html', songs=songs)


if __name__ == '__main__':
    obj = []
    with open(songs_file, "w") as fo:
        json.dump(obj, fo)
    app.run(debug=True, host='0.0.0.0')
