#!/usr/bin/env python
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play

class SayMyText:
  def __init__(self, text, lang):
    self.text = text
    self.lang = lang
    
  def say(self):
    speech = gTTS(text=self.text, lang=self.lang)
    mp3_fp = BytesIO()
    speech.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    audio = AudioSegment.from_file(mp3_fp, format="mp3")
    play(audio)