import pygame
from pygame import mixer
import time
import sys


DEMO_RHYMTH = 'D-T---T-D---T-tkD-T---T-D--kS---'  # Maqsum
# DEMO_RHYMTH = 'D-k-D-S-tktkD-tkT-tk'  # Baladi

DEFAULT_BPM = 120


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
        return self

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


def create_sound_player():
    player = SoundPlayer()
    player\
        .add_sound('D', 'dum')\
        .add_sound('T', 'tek')\
        .add_sound('t', 'tek', 0.2)\
        .add_sound('k', 'tek', 0.2)\
        .add_sound('S', 'slap')\
        .add_sound('s', 'slap', 0.3)
    return player


if __name__ == '__main__':
    mixer.pre_init(44100, -16, 1, 2048)
    pygame.init()
    player = create_sound_player()

    rhythm = sys.argv[1] if len(sys.argv) >= 2 else DEMO_RHYMTH
    bpm = int(sys.argv[2]) if len(sys.argv) == 3 else DEFAULT_BPM

    play_forever(player, rhythm, bpm)
