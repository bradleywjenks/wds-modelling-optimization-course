# Modelling and Optimization of Water Distribution Systems

Notebooks on modelling and optimization of water distribution systems.

Materials based on module taught by Ivan Stoianov and Aly-Joy Ulusoy at Imperial College London. Used in:

- CIVE70019/70057, Imperial College London
- CV8100 Directed Studies in Civil Engineering, Toronto Metropolitan University (Fall 2026)

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
