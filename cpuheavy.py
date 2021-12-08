from math import sqrt
import time

def calc_thing(x):
    countdown = x
    while sqrt(countdown) != 1:
        countdown -= 1
        
    return 1

def calc_and_timer(x):
    start = time.perf_counter()
    calc_thing(x)
    time_taken = time.perf_counter() - start
    return time_taken


if __name__ == "__main__":
    print(calc_and_timer(20000000))