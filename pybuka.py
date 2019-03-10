import pygame
from pygame import mixer
import time


RYTHM = 'D-T---T-D---T-tkD-T---T-D---T---'  # Maksum
BPM = 120


mixer.pre_init(44100, -16, 1, 2048)
pygame.init()


class SoundPlayer:
    def __init__(self):
        self.map = {}
        self.sounds = {}

    def add_sound(self, note, name, volume=1.0):
        ch_id = len(self.map)
        channel = mixer.Channel(ch_id)
        channel.set_volume(volume)

        if name in self.sounds:
            sound = self.sounds[name]
        else:
            sound = mixer.Sound(f'sb/{name}.ogg')
            self.sounds[name] = sound

        self.map[note] = (sound, channel)

    def play_note(self, note):
        if note in self.map:
            sound, channel = self.map[note]
            channel.play(sound)


def play_forever(player: SoundPlayer, rythm, bpm):
    notes_n = len(rythm)
    delay = 60 / bpm / 4

    print(f'Notes = {notes_n}; BPM = {bpm}; Delay = {delay}')

    ptr = 0
    while True:
        note = rythm[ptr]
        player.play_note(note)

        ptr += 1
        if ptr >= len(rythm):
            ptr = 0

        time.sleep(delay)


player = SoundPlayer()
player.add_sound('D', 'dum')
player.add_sound('T', 'tek')
player.add_sound('t', 'tek', 0.2)
player.add_sound('k', 'tek', 0.2)
play_forever(player, RYTHM, BPM)
