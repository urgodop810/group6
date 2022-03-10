# Read in libraries
import json
from statsbombpy import sb          # Used to obtain StatsBomb data.
import statsbomb as sbp
import pandas as pd                 # Read and manipulate data.
import numpy as np                  # Read and manipulate data.
from pandas.io.json import json_normalize

import matplotlib.pyplot as plt     # Plotting data
from mplsoccer.pitch import Pitch

comps = sb.competitions()
comps[comps.competition_gender == 'female']
print(comps)

matches = sb.matches(competition_id=37, season_id=42)
matches.head(5)

print(matches)
plt.show()
