import os
import sys
import pandas as pd
import numpy as np


print("Importing data ...")

parent_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
laps_path = os.path.join(parent_dir, "CSV_generated/cycling_2022-02-01_12-24-44_laps.csv")
activity_path = os.path.join(parent_dir, "CSV_generated/cycling_2022-02-01_12-24-44.csv")
starts_path = os.path.join(parent_dir, "CSV_generated/cycling_2022-02-01_12-24-44_starts.csv")

laps_dataset = pd.read_csv(laps_path)
activity_dataset = pd.read_csv(activity_path)
starts_dataset = pd.read_csv(starts_path)

print("Data imported")

