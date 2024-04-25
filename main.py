import eel
import nfc
import binascii
import sys
from time import sleep
from jinja2 import Environment, FileSystemLoader
import simpleaudio
from setting import session
from user import *
from card import *
from voicevox import Client
import asyncio

eel.init('web', allowed_extensions=['.js', '.html'])

env = Environment(loader=FileSystemLoader('web'))
clf = nfc.ContactlessFrontend('usb')


async def play_voice(message):
    async with Client() as client:
        audio_query = await client.create_audio_query(message, speaker=1)
        with open("voice.wav", "wb") as f:
            f.write(await audio_query.synthesis(speaker=1))
        wav_obj = simpleaudio.WaveObject.from_wave_file("voice.wav")
        play_obj = wav_obj.play()


@eel.expose
def render_template(template_name, **context):
    template = env.get_template(template_name)
    return template.render(context)


@eel.expose
def start_read():
    try:
        tag = clf.connect(rdwr={'on-connect': lambda tag: False})
        idm = binascii.hexlify(tag.identifier).upper()
        idm = idm.decode()
        card = session.query(Card).filter_by(idm=idm).first()
        if card is not None:
            user = session.query(User).filter_by(id=card.userId).first()
            wav_obj = simpleaudio.WaveObject.from_wave_file(
                "success.wav")
            play_obj = wav_obj.play()
            if (user.yomi != "" or user.yomi != None):
                asyncio.run(play_voice(
                    user.yomi + "さん、お疲れ様でした！" if user.state else user.yomi + "さん、こんにちは！"))
            eel.set_readed(user.name, "out" if user.state else "in")
            user.state = not user.state
            session.commit()
            sleep(2)
            eel.remove_readed()
        else:
            eel.set_not_found()
            sleep(2)
            eel.remove_not_found()
        start_read()
    except Exception as e:
        print(e)
        eel.close_window()
        sys.exit()


def close():
    clf.close()


eel.start('templates/index.html', jinja_templates='templates',
          mode='chrome', size=(960, 540), close_callback=close)
