from flask import Flask, render_template, request
import asyncio
import edge_tts

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate', methods=['POST'])
def generate():
    name = request.form['name']
    gender = request.form['gender']
    if gender == '1':
        voice = 'en-US-GuyNeural'
    else:
        voice = 'en-US-JennyNeural'
    text = f"Hello, you have reached {name} at Cisco Tac, my working hours are from 10 am to 6 pm Monday through Friday, so I'm not available right now, Please leave your name and service request number, I'll review the information and contact you back as soon as possible, thank you!"
    output_file = "vm.wav"
    asyncio.run(_generate_voice(text, voice, output_file))
    message = "Your new voicemail audio file has been generated successfully, please download it from the link below and upload it to your phone profile."
    file_url = f"/static/{output_file}"
    return render_template('result.html', message=message, file_url=file_url)

async def _generate_voice(text, voice, output_file):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
