With this tool you can create music from:
  1. random bytes
  2. raw data, like binary dump, pictures etc.

Possible usages:
  1. Create a music :)
  2. Analyze patterns in a raw data by listenning to it.
  
The idea is to "translate" bytes to indexes in a music chunks list.
I don't actually translate bytes to pcm frames, but I think this is much cooler method.
You can take music parts from your favourite song and generate from them a new music.

Usage
------
In order to use bin2music you need to install these packages:
  1. pygame
  2. wave
  3. numpy
  4. baker
And you gonna need a wav music file.
  
Then you can get random music by running:
> python ./bin2music.py run_random ./some_music.wav
Or translate raw data to music:
> python ./bin2music.py play_binary ./binary_data ./some_music.wav
It works also with stdin:
> cat ./binary_data | python ./bin2music.py /proc/self/fd/0 ./some_music.wav

Configurations
----------------
1. The global CHUNK_SIZE stores the size of each music chunk.
2. You can pass should_shuffle flag to Binary2Music init function to determine if the chunks should be shuffled after loading.
