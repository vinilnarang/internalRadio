from flask import Flask, render_template, request
import subprocess
from pprint import pformat
import json

app = Flask(__name__)

@app.route('/')
def index():
	return 'Welcome to internal radio 8finatics'

@app.route('/addSong')
def addSong():
	return render_template('index.html')

@app.route('/add')
def add():
	url = request.args.get('url')
	fo = open("songs.json", "r")
	obj = json.load(fo)
	fo.close()

	
	obj.append(url)
	fo = open("songs.json", "w")
	json.dump(obj, fo)
	fo.close()

	return url


@app.route('/listSongs')
def listSongs():
	#x = subprocess.check_output(['wc','-l','songs.txt'])
	#numLines = x.split(" ")[0]
	#l = []
	#with open("songs.txt","r") as f:
	#	for line in f:
	#		l.append(line[:-1])
	#return pformat(l)
	fo = open("songs.json", "r")
	obj = json.load(fo)
	fo.close()
	return pformat(obj)

if __name__ == '__main__':
	obj=[]
	fo = open("songs.json", "w")
	json.dump(obj, fo)
	fo.close()
	app.run(debug=True, host='0.0.0.0')
