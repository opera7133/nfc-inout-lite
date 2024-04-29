import requests
import os
from pydub import AudioSegment


def download_effects():
    url = 'https://soundeffect-lab.info/sound/button/mp3/decision35.mp3'
    response = requests.get(url)

    if response.status_code == 200:
        success_sound = response.content
        with open(os.path.join(os.path.dirname(__file__), 'success.mp3'), 'wb') as f:
            f.write(success_sound)
        sound = AudioSegment.from_file(os.path.join(
            os.path.dirname(__file__), 'success.mp3'), format="mp3")
        sound.export(os.path.join(os.path.dirname(
            __file__), 'success.wav'), format="wav")
        os.remove(os.path.join(os.path.dirname(__file__), 'success.mp3'))


download_effects()
