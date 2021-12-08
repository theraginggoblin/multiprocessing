import multiprocessing
from cpuheavy import calc_and_timer

# https://docs.python.org/3/library/multiprocessing.html

def calc_list(x_list):
    with multiprocessing.Pool(processes=2) as pool:
        result = pool.map(calc_and_timer, x_list)
    return result

if __name__ == "__main__":
    x_list = [2000000, 2000000, 2000000, 2000000]

    total_time = 0
    for x in x_list:
        total_time += calc_and_timer(x)
    print(f"Result in seconds from for loop iteration: {total_time}")

    multi_process_time = calc_list(x_list)
    print(f"Seconds taken for each process in multi-process: {multi_process_time}")