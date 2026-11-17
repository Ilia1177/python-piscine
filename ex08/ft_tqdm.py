import os


def f_time(s):
    m = int(s) // 60
    sec = int(s) % 60
    return f"{m:02d}:{sec:02d}"


def ft_tqdm(iterable):
    width = os.get_terminal_size().columns
    total = len(iterable)
    last_update = 0
    start = os.times().elapsed
    for i, elem in enumerate(iterable,  start=1):
        now = os.times().elapsed
        if now - last_update > 0.1 or i == total:
            elapsed = now - start
            speed = i / elapsed if elapsed > 0 else 0.0
            eta = (total - i) / speed if speed > 0 else 0
            percent = int(100 * i / total)
            endl = f"[{f_time(elapsed)}<{f_time(eta)}, {speed:.2f}it/s]"
            prefix = f"{percent:3d}%|"
            suffix = f"| {i}/{total} {endl}"
            bar_width = max(width - len(prefix) - len(suffix), 1)
            filled = int(bar_width * i / total)
            bar = "█" * filled + "-" * (bar_width - filled)
            print(f"\r{prefix}{bar}{suffix}", end="", flush=True)
            last_update = now
        yield elem
    print()
