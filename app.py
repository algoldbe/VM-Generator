from flask import Flask, render_template, request, send_file
import asyncio
import edge_tts
from pydub import AudioSegment
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    name = request.form['name']
    gender = request.form['gender']
    if gender == '1':
        voice = 'en-US-GuyNeural'
    else:
        voice = 'en-US-JennyNeural'
    text = f"Hello, you have reached {name} at Cisco Tac, my working hours are from 9 am to 5 pm Monday through Friday, Pacific Time, so I'm not available right now, Please leave your name and service request number, I'll review the information and contact you as soon as possible. For immediate Tac assistance, please call 001,800,553,2447; Thank you!"
    output_file = "vm.mp3"
    asyncio.run(_generate_voice(text, voice, output_file))

    # Convert the output file to WAV format
    wav_output_file = "vm.wav"
    convert_to_wav(output_file, wav_output_file)

    # Delete the original MP3 file
    os.remove(output_file)

    message = "Your new voicemail has been generated successfully!"
    file_url = f"/download/{wav_output_file}"
    return render_template('result.html', message=message, file_url=file_url)

@app.route('/download/<path:filename>', methods=['GET'])
def download(filename):
    return send_file(filename, as_attachment=True)

async def _generate_voice(text, voice, output_file):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)

def convert_to_wav(input_file, output_file):
    audio = AudioSegment.from_mp3(input_file)
    audio.export(output_file, format="wav")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
