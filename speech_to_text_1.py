from google.cloud import speech_v1p1beta1 as speech
from pydub import AudioSegment
import io

client = speech.SpeechClient.from_service_account_file('/Users/pavankumar/Documents/Programming/Python/Project/key.json')

file_name = "/Users/pavankumar/Documents/Programming/Python/Project/t_test.m4a"

# Convert m4a to flac (Speech-to-Text API requires flac)
audio = AudioSegment.from_file(file_name, format="m4a")
flac_data = io.BytesIO()
audio.export(flac_data, format="flac")
flac_data.seek(0)

# Create RecognitionAudio object
audio = speech.RecognitionAudio(content=flac_data.read())

config = speech.RecognitionConfig(
    sample_rate_hertz= 16000,
    enable_automatic_punctuation=True,
    language_code='te-IN',
    encoding = 'FLAC'
)

operation = client.long_running_recognize(
    config=config,
    audio=audio   
)
response = operation.result()
print("The response is running")
print(response)

for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))
