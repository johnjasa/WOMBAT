import numpy as np
import pandas as pd

from wombat import Simulation
from wombat.core.library import load_yaml
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

sim.run(delete_logs=True, save_metrics_inputs=False)

net_cf = sim.metrics.capacity_factor(
    which="net", frequency="project", by="windfarm"
).values[0][0]
gross_cf = sim.metrics.capacity_factor(
    which="gross", frequency="project", by="windfarm"
).values[0][0]
print(f"  Net Capacity Factor: {net_cf:2.1%}")
print(f"Gross Capacity Factor: {gross_cf:2.1%}")

print(sim.metrics.opex("annual"))