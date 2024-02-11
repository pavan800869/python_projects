from google.cloud import texttospeech_v1
import os
from unicodedata import name
from urllib import response
#instatiation of client 
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/pavankumar/Documents/Programming/Python/Project/test_to_speech/key.json'
client = texttospeech_v1.TextToSpeechClient()
sample = input("Enter the text: ")
text = f'<speak>{sample}</speak>'

synthesis_input = texttospeech_v1.SynthesisInput(ssml=text)

voice1 = texttospeech_v1.VoiceSelectionParams(
    language_code = 'en-in',
    ssml_gender = texttospeech_v1.SsmlVoiceGender.FEMALE
)
voice2 = texttospeech_v1.VoiceSelectionParams(
    name='vi-VN-Wavenet-D',
    language_code='vi-VN'
)

print(client.list_voices)
audio_config = texttospeech_v1.AudioConfig(
    audio_encoding = texttospeech_v1.AudioEncoding.MP3
)
response1 = client.synthesize_speech(
    input=synthesis_input,
    voice=voice1,
    audio_config=audio_config
)

with open('/Users/pavankumar/Documents/Programming/Python/Project/test_to_speech/audio.mp3','wb') as out:
    out.write(response1.audio_content)