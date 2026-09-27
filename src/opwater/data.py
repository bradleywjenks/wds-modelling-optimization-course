"""Locate the repository's data folder."""

from pathlib import Path


def data_dir():
    """Return the `data/` folder of the repository containing the current working directory."""
    cwd = Path.cwd().resolve()
    for folder in (cwd, *cwd.parents):
        if (folder / "data" / "networks").is_dir():
            return folder / "data"
    raise FileNotFoundError(
        "Could not find the 'data/' folder. Open the notebook from inside the repository."
    )


def network_file(name):
    """Return the path to an EPANET .inp file in `data/networks/`."""
    return data_dir() / "networks" / name
