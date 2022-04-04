# Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5L) - Drank - log
# Eyes - eyes.mp3 - every 30mins - EyDone - log
# Physical activity - physical.mp3 - every 45 min - ExDone - Log
# Rules
# Pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time


def musicloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f'{msg} {datetime.now()}')


if __name__ == "__main__":
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 5
    exsecs = 10
    eyessecs = 20

    while True:
        if time() - init_water > watersecs:
            print('Drinking water time. Enter DRANK to stop the alarm.')
            musicloop('C:\\Users\\Gunjal\\parag-intern\\Timepass\\water.mp3', 'DRANK')
            init_water = time()
            log_now("Drank water at ")

        if time() - init_exercise > exsecs:
            print('Exercise time. Enter EXERCISED to stop the alarm.')
            musicloop('physical.mp3', 'EXERCISED')
            init_exercise = time()
            log_now("Exercised at ")

        if time() - init_eyes > eyessecs:
            print('Eyes relax time. Enter RELAXED to stop the alarm.')
            musicloop('eyes.mp3', 'RELAXED')
            init_exercise = time()
            log_now("Eyes Relaxed at ")
