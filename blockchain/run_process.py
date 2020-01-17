import os
from multiprocessing import Pool

processes = ('miner.py', 'miner.py', 'miner.py', 'miner.py', 'miner.py')

def run_process(process):
    os.system('python {}'.format(process))

pool = Pool(processes=5)
pool.map(run_process, processes)