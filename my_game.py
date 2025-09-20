from pygame import *
import sounddevice as sd
import scipy.io.wavfile as wav
fs = 44100
recording = None
is_recording = False
voise_file = "voice_record.wav"
minus_track = "MinusDuHast"
init()
mixer.init()
mixer.music.set_volume(0.5)
window_size = 1200, 600
window = display.set-mode(window_size)
clock = time.Clock()
font.init()
font_big = font.sysfont("Arial", 32)
btn_rect = Rect(425, 250, 350, 80)
rect_color = "white"
btn_text = "Запис"
def start_voice_record():
    global recording
    recording = sd.rec(int(fs * 5), samplerate = fs, channels = 1, dtype = "int16")
def stop_voice_recording():
    global recording
    sd.stop()
    if recording is not None:
        wav.write(voice_file, fs, recording)
def play_song_and_voice_together():
    mixer.music.load(minus_track)
    mixer.music.play()
    voice_sound = mixer.Sound(voice_file)
    voice_sound.play()
while True:
    for e in event.get:
        if e.type == QUIT:
            guit()
        if e.type == MOUSEBUTTONDOWN:
            if btn_rect.collidepoint(e.pos):
                if not is_recording:
                    rect_color = "red"
                    btn_text = "Стоп та прослухати"
                    is_recording = True
                    mixer.music.load(minus_track)
                    mixer.music.pllay()
                    start_voice_record()
                else:
                    rect_color = "white"
                    btn_text = "Запис"
                    is_recording = False
                    stop_voice_recording()
                    play_song_and_voice_together()                    
