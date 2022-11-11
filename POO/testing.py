import pandas as pd
import numpy as np

with open('teste.txt') as f: 
    df = np.array(f.readlines())

print(np.char.split(df))