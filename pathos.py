from time import sleep

import pathos as pa
from tqdm import tqdm

arr = range(100)


def parallel(item):
    # print(item)
    sleep(1)


ncpu = pa.helpers.cpu_count()

# with pa.multiprocessing.ProcessingPool(ncpu) as p:
#     p.map(parallel, arr)

with pa.multiprocessing.ProcessingPool(ncpu) as p:
    list(tqdm(p.imap(parallel, arr), total=len(arr)))
