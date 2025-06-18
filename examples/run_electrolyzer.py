from time import perf_counter  # timing purposes only

import numpy as np
import pandas as pd

from wombat import Simulation
from wombat.core.library import load_yaml, DINWOODIE
from pathlib import Path


# Get the base path where the wombat package is located
wombat_base_path = Path(__file__).resolve().parent
library_folder = (wombat_base_path / ".." / "tests" / "library").resolve()

# Seed the random variable for consistently randomized results
np.random.seed(0)

# Improve the legibility of DataFrames
pd.set_option("display.float_format", "{:,.2f}".format)
pd.set_option("display.max_rows", 1000)
pd.set_option("display.max_columns", 1000)

config = load_yaml(".", "poly_electrolyzer.yml")
sim = Simulation(
    library_path=library_folder,  # automatically directs to the provided library
    config=config,
)
sim.env.cleanup_log_files()



# Timing for a demonstration of performance
start = perf_counter()

sim.run(delete_logs=True, save_metrics_inputs=False)

end = perf_counter()

timing = end - start
print(f"Run time: {timing / 60:,.2f} minutes")