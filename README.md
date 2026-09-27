# WDS Modelling & Optimization Course

Teaching notebooks on modelling and optimization of water distribution systems — hydraulic analysis, optimization-based model calibration, and operational optimization.

## Local setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/bradleywjenks/wds-modelling-optimization-course.git
cd wds-modelling-optimization-course
uv sync
uv run jupyter lab
```

Helper code used across the notebooks lives in the `opwater` package (`src/opwater/`), which is installed into the environment by `uv sync`.

> A Google Colab option will be added later.
