from flask import Flask, request, render_template, jsonify
import speech_recognition as sr
import io
import os
from gpiozero import LED
from signal import pause

from pydub import AudioSegment

app = Flask(__name__)


red = LED(17)
green = LED(27)
yellow = LED(22)


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
        recorded_sound = sr.AudioFile(io.BytesIO(wav_data))

    # Open the audio file as a source
        with recorded_sound as source:
        # Read the entire audio file
            audio = r.record(source)

    # Transcribe the audio using Google Speech Recognition
        text = r.recognize_google(audio)
        print(text)

        if 'fan on' in text:
            red.on()
        elif 'fun on' in text:
            red.on()
            
        elif 'television on' in text:
            green.on()
            
        elif 'light on' in text:
            yellow.on()
          
        elif 'light off' in text:
            yellow.off()

        elif 'fan off'  in text:
            red.off()
        elif 'fun off' in text:
            red.off()

        elif 'television off' in text:
            green.off()

        else:
            red.blink()
            yellow.blink()
            green.blink()
            red.off()
            yellow.off()
            green.off()

            
            
        

# Print the transcribed text
    
    
      # Print the text in the console
    return 'Success'

if __name__ == '__main__':
    app.run(debug=True, host = '192.168.137.10' ,port=3000)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
