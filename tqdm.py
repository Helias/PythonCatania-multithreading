from time import sleep

from tqdm import tqdm

arr = range(100)

for x in tqdm(arr):
    # print(x)
    sleep(1)
