from flask import Flask, request, render_template, jsonify
import speech_recognition as sr

import soundfile as sf

import io
import os
from gpiozero import LED,Buzzer
from signal import pause

from time import sleep
from pydub import AudioSegment


app = Flask(__name__)


red = LED(17)
green = LED(27)
yellow = LED(22)
buzzer = Buzzer(16)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/voice', methods=['POST'])
def process_voice():
    voice_file = request.files['audio']  # Retrieve the uploaded audio file
    voice_data = voice_file.read()  # Read the contents of the audio file
    # Process the voice data to convert it to text
    print("voice Pass here")

    if voice_file.filename == '':
        return jsonify({'error': 'Missing audio file'}), 400
    
    wav_data = b'' 
    
    if voice_file:
        audio = AudioSegment.from_file(io.BytesIO(voice_data), format='webm')
        wav_data = audio.export(format='wav').read()

        

    # text = process_voice_data(voice_data)
        r = sr.Recognizer()

    # Load the audio file
        havard = sr.AudioFile(io.BytesIO(wav_data))

    # Open the audio file as a source
        with havard as source:
        # Read the entire audio file
            audio = r.record(source)

    # Transcribe the audio using Google Speech Recognition
        text = r.recognize_google(audio)
        print(text)

        if 'fan on' in text:
            buzzer.on()
            sleep(0.5)
            buzzer.off()
            red.on()
        elif 'fun on' in text:
            red.on()
            
        elif 'television on' in text:
            buzzer.on()
            sleep(0.5)
            buzzer.off()
            green.on()
            
        elif 'light on' in text:
            buzzer.on()
            sleep(0.5)
            buzzer.off()
            yellow.on()
          
        elif 'light off' in text:
            buzzer.on()
            sleep(0.5)
            buzzer.off()
            yellow.off()

        elif 'fan off'  in text:
            buzzer.on()
            sleep(0.5)
            buzzer.off()
            red.off()

        elif 'fun off' in text:
            buzzer.on()
            sleep(0.5)
            buzzer.off()
            red.off()

        elif 'television off' in text:
            buzzer.on()
            sleep(0.5)
            buzzer.off()
            green.off()

        elif 'all appliances off' in text:
            buzzer.on()
            sleep(0.5)
            buzzer.off()
            red.off()
            yellow.off()
            green.off()

        elif 'all appliances on' in text:
            buzzer.on()
            sleep(0.5)
            buzzer.off()
            red.on()
            yellow.on()
            green.on()

        else:
            buzzer.on()
            sleep(2)
            buzzer.off()

            
            
        return jsonify("Converted Successfully")

# Print the transcribed text
    
    
      # Print the text in the console
    return 'Success'

if __name__ == '__main__':
    app.run(debug=True, host = '192.168.137.10' ,port=3000)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
