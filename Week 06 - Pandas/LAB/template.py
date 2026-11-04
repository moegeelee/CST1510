"""Week 6 record check with pandas.

Name: Mohammed Mohammed Alhaji
Lane: Data Science
Date: 2026-11-04

Run with: python template.py
The CSV contains invented practice data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


# Load the CSV beside this script, wherever the script is launched from.
lab_folder = Path(__file__).resolve().parent
df = pd.read_csv(lab_folder / "datasets.csv")

# Calculate a percentage for every dataset and apply the lab's status rules.
df["percent"] = (df["rows_loaded"] / df["rows_expected"]) * 100
df["status"] = df["percent"].apply(
    lambda percent: "OVER LIMIT" if percent >= 100 else "WARNING" if percent >= 90 else "OK"
)

print("All datasets")
print(df.to_string(index=False))

print("\nDatasets needing attention")
print(df[df["status"] != "OK"].to_string(index=False))

status_counts = df.groupby("status").size()
print("\nDataset count per status")
print(status_counts)

df.to_csv(lab_folder / "datasets_report.csv", index=False)

status_counts.plot(kind="bar", color="#4169a1", title="Dataset count by status")
plt.xlabel("Status")
plt.ylabel("Number of datasets")
plt.xticks(rotation=0)
plt.yticks([0, 1, 2])
plt.tight_layout()
plt.savefig(lab_folder / "dataset_status_counts.png", dpi=150)
plt.close()

# Hand check: traffic_data has 900 / 1000 * 100 = 90%, so its status is WARNING.
