import pygame
import itertools
import wave
import time
import numpy
import random
import baker

CHUNK_SIZE = 4 * 4000

class Binary2Music(object):
    def __init__(self, music_path, should_shuffle=True):
        self.should_shuffle = should_shuffle
        self.load_music(music_path)

    def load_music(self, music_path, chunk_size=CHUNK_SIZE):
        wave_file = wave.open(music_path)
        wave_frames = wave_file.readframes(wave_file.getnframes())
        self.frames = [wave_frames[x:x+chunk_size] for x in xrange(0, wave_file.getnframes(), chunk_size)]
        if self.should_shuffle:
            random.shuffle(self.frames)
        #now choose only 255 of them
        self.frames = self.frames[:256]

    def shape_number(self, num, start, stop):
        '''
        convert num to be in range(start, stop)
        '''
        cyc = itertools.cycle(xrange(start, stop))
        result = cyc.next()
        for i in xrange(0, num):
            result = cyc.next()
        return result

    def binary2music(self, binary):
        # return binary
        frames = ''
        for b in binary:
            index = self.shape_number(ord(b), 0, len(self.frames))
            frames += self.frames[index]
        return frames

    def play_binary(self, binary, timeout=None):
        pygame.mixer.init()
        my_sound = pygame.mixer.Sound(buffer(self.binary2music(binary)))
        my_sound.play()
        if timeout:
            time.sleep(timeout)
            pygame.mixer.stop()


def play(data, music_path):
    bm = Binary2Music(music_path=music_path)
    bm.play_binary(data)
    raw_input()

@baker.command
def run_random(music_path, size=10000):
    data = ''.join(chr(x) for x in numpy.random.randint(0, 255, size))
    play(data, music_path)

@baker.command
def play_binary(path, music_path, ignore_zeros=True, should_display=True, should_shuffle=False):
    bm = Binary2Music(music_path=music_path, should_shuffle=should_shuffle)
    with open(path, 'rb') as f:
        while True:
            data = f.read(4)
            if should_display:
                print ' '.join('%02x' % (ord(x)) for x in data) + '\t\t%r' % (data)
            if not data:
                break
            if ignore_zeros:
                data = data.replace('\x00', '')
            bm.play_binary(data)
            while pygame.mixer.get_busy():
                # time.sleep(0.1)
                pass

if __name__ == '__main__':
    baker.run()
