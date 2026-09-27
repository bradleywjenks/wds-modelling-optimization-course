# Modelling and Optimization of Water Distribution Systems

Notebooks on modelling and optimization of water distribution systems.

Materials based on module taught by Ivan Stoianov and Aly-Joy Ulusoy at Imperial College London. Used in:

- CIVE70019/70057, Imperial College London
- CV8100 Directed Studies in Civil Engineering, Toronto Metropolitan University (Fall 2026)

## Notebooks

| Notebook | Topic | |
| --- | --- | --- |
| [`hydraulic_modelling.ipynb`](notebooks/hydraulic_modelling.ipynb) | Newton-Raphson hydraulic solvers, Schur complement, comparison with EPANET and field data | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/bradleywjenks/wds-modelling-optimization-course/blob/main/notebooks/hydraulic_modelling.ipynb) |

## Google Colab

Click a notebook's **Open in Colab** badge and run the setup cell at the top. It clones this repository and installs the `opwater` helper package with its dependencies. Changes you make in Colab are not saved unless you use **File > Save a copy in Drive**.

## Local setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/bradleywjenks/wds-modelling-optimization-course.git
cd wds-modelling-optimization-course
uv sync
uv run jupyter lab
```

In VS Code, open the repository folder and select the `.venv` interpreter as the notebook kernel.

Helper code used across the notebooks lives in the `opwater` package (`src/opwater/`), which is installed into the environment by `uv sync`. Network files and datasets are in `data/`.
