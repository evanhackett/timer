import argparse
import os
import sys
import time

from playsound import playsound


def pad(n: int):
    return f'{n:02}'

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("time", help="the time in mm:ss format (minutes:seconds).")
    args = parser.parse_args()

    minutes_seconds = args.time.split(':')

    minutes = int(minutes_seconds[0])
    seconds = int(minutes_seconds[1])

    total_seconds = minutes * 60 + seconds

    for elapsed in range(total_seconds):
        time_left = total_seconds - elapsed
        min_left = time_left // 60
        sec_left = time_left % 60

        sys.stdout.write(f'\r {pad(min_left)}:{pad(sec_left)}')
        time.sleep(1)
        sys.stdout.flush()


    print('\nTimer finished!')
    sound_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'alarm.mp3')
    playsound(sound_file_path)
