

from time import sleep
from tqdm import tqdm
from ft_tqdm import ft_tqdm
for elem in ft_tqdm(range(33)):
    sleep(0.005)
print()
for elem in tqdm(range(33)):
    sleep(0.005)
print()


