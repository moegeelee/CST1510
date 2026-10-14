# Fixed worked example: the supplied file is records_sample.txt in LAB.
# Original open("records.txt") raised FileNotFoundError.
from pathlib import Path

# Locate the file beside the lab notebook, regardless of the terminal folder.
path = Path(__file__).resolve().parents[1] / "records_sample.txt"
with open(path) as f:
    print(f.read())
