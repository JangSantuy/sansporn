from flask import Flask, jsonify, render_template, send_from_directory, request
import os
import glob

app = Flask(__name__)

@app.route('/videos')
def videos():
    video_files = glob.glob("static/videos/*.mp4")
    return jsonify(videos=video_files)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play')
def play():
    video = request.args.get('video')
    return render_template('play.html', video=video)

if __name__ == '__main__':
    app.run(debug=True)
