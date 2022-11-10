from pathlib import Path

import pytest
from torch_geometric.data import Data

from gvp.data.biotite import convert_to_pyg, load_mmtf_file


@pytest.fixture
def data() -> Data:
    filename = Path(Path(__file__).parent, "data/4HHB.mmtf.gz").absolute()
    return convert_to_pyg(load_mmtf_file(filename))