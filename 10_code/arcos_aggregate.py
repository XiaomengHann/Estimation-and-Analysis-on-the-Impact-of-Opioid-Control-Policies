from fastparquet import ParquetFile
from datetime import datetime
from tqdm import tqdm
import pandas as pd
import numpy as np
import csv
import os
from glob import glob

os.chdir('/Users/joseph.hsieh/Documents/Duke/Course Work/Fall 2019/IDS 690 - Practical Data Science 1/IDS690_team_project/')
# varify the path using getcwd()
cwd = os.getcwd()
# print the current directory
print("Current working directory is:", cwd)
%pwd
path_list = glob('By_State_Parquet/*.parquet')
len(path_list)


arcos_all = pd.concat([pd.read_parquet(path, engine='fastparquet') for path in tqdm(path_list)], ignore_index=True)
arcos_all.STATE.value_counts()
arcos_all.to_csv('arcos_grouped_all')
