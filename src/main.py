import time

import pygame
import requests
from pygame import mixer

from src.commandline_args import CommandlineArgs
from src.config import Config

"""

Usage: 

- Replace API key below with your own.
- Install pygame with `pip install pygame`
- Replace tts_to_generate_audio_for with your own text
- 

"""

commandline_args = CommandlineArgs()
config = Config()

tts_to_generate_audio_for = commandline_args.get_text()
voice_id = config.get("voice_id")
api_key = config.get("api_key")
output_filename = config.get("output_filename")

url = "https://api.elevenlabs.io/v1/text-to-speech/" + voice_id

headers = {
    "accept": "audio/mpeg",
    "xi-api-key": api_key,
    "Content-Type": "application/json"
}

data = '{"text": "<MYTEXT>"}'
data = data.replace("<MYTEXT>", tts_to_generate_audio_for)

print("Sending request to ElevenLabs API...")

response = requests.post(url, headers=headers, data=data)

print(f"Received response from ElevenLabs API: {response.status_code}")

# response 200 means success
if response.status_code == 200:

    filename = output_filename

    # Save to a file
    with open(filename, "wb") as f:
        f.write(response.content)
        f.close()

    # Play the audio in response.content in default windows
    # import os
    # os.startfile(filename)

    # Play in the python script on Windows without opening an external application
    # Mixer will play it in another thread, there are other easy libraries to use if you want the call to block instead
    # Mixer can also be used to pause and resume playback
    pygame.init()
    mixer.music.load(filename)
    mixer.music.play()
    # Other examples
    # mixer.music.pause()
    # mixer.music.unpause()
    # mixer.music.set_volume(0.5)

    print("Playing audio: " + tts_to_generate_audio_for)
    while mixer.music.get_busy():
        # print("Waiting for audio to finish playing...")
        time.sleep(0.1)

    print("Complete")

else:
    print("Request failed with status code: {}".format(response.status_code))
