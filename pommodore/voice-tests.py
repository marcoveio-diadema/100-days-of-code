from gtts import gTTS
import pygame

# ----------------------------- VOICE OBJECTS ---------------------------- #
short_break = "Five minute break"
language = 'en'  # Language code (e.g., 'en' for English)
slow = False     # Set to True for slower speech

short_break_tts = gTTS(short_break, lang=language, slow=slow)
short_break_mp3 = "short_break.mp3"
short_break_tts.save(short_break_mp3)

# listen to it

pygame.mixer.init()
pygame.mixer.music.load(short_break_mp3)
pygame.mixer.music.play()