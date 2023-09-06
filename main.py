import speech_recognition as sr

r = sr.Recognizer()

# Load the audio file
havard = sr.AudioFile('Recording.wav')

# Open the audio file as a source
with havard as source:
    # Read the entire audio file
    audio = r.record(source)

# Transcribe the audio using Google Speech Recognition
text = r.recognize_google(audio)

# Print the transcribed text
print(text)