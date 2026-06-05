# import shutil
#
# width = shutil.get_terminal_size().columns
# print(width)
#
# def ft_tqdm(iterable):
#     total = len(iterable)
#     count = 0
#
#     for elem in iterable:
#         count += 1
#         print(f"\r{count}/{total} processed", end="", flush=True)
#         yield elem
#
#     print()

import shutil
import time

def format_time(s):
    m = int(s) // 60
    sec = int(s) % 60
    return f"{m:02d}:{sec:02d}"

def ft_tqdm(iterable):
    width = shutil.get_terminal_size(fallback=(80, 24)).columns
    total = len(iterable)
    count = 0
    last_update = 0
    start = time.time()
    obj_len = len(str(2 * total + 3 ))
    bar_width = width - 35 - obj_len  # reserve space for text
    for i, elem in enumerate(iterable,  start=1):
        now = time.time()
        count += 1
        if time.time() - last_update > 0.1 or i == total:
            elapsed = int(time.time() - start)
            speed = i / elapsed if elapsed > 0 else 0.0
            eta = (total - i) / speed if speed > 0 else 0
            percent = int(100 * i / total)
            filled = int(bar_width * i / total)
            bar = "█" * filled + "-" * (bar_width - filled)
            end_line = f"[{format_time(elapsed)}<{format_time(eta)}, {speed:.2f}it/s]"
            print(f"\r{percent:3d}%|{bar}| {count}/{total} {end_line}", end="", flush=True)
            last_update = now
        yield elem
    print()    
