"""All the general configuration of the project."""
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

SRC = Path(__file__).parent.resolve()
BLD = SRC.joinpath("..", "..", "bld").resolve()

TEST_DIR = SRC.joinpath("..", "..", "tests").resolve()
PAPER_DIR = SRC.joinpath("..", "..", "paper").resolve()

GROUPS = ["marital_status", "qualification"]

__all__ = ["BLD", "SRC", "TEST_DIR", "GROUPS"]


# Configure Matplotlib to use LaTeX
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

color_scheme = ["#3c5488", "#e64b35", "#4dbbd5", "#00a087", "#f39b7f"]
sns.set_theme(style="white", palette=color_scheme)
