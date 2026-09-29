import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Step 1: Create the dataset
data = {
    "Point": ["P1", "P2", "P3", "P4", "P5", "P6",
              "P7", "P8", "P9", "P10", "P11", "P12"],
    "X": [3, 4, 5, 6, 7, 6, 7, 8, 3, 2, 3, 2],
    "Y": [7, 6, 5, 4, 3, 2, 2, 4, 3, 6, 5, 4]
}

df = pd.DataFrame(data)

# Step 2: Define DBSCAN parameters
eps = 1.9
min_pts = 4

# Step 3: Extract data points
X = df[["X", "Y"]].values

# Step 4: Calculate Euclidean distance matrix
distances = cdist(X, X, metric="euclidean")

dist_df = pd.DataFrame(distances.round(2), index=df["Point"], columns=df["Point"])

print(f"minPts = {min_pts}, epsilon = {eps}")
print("\nDistance Matrix:")
print(dist_df.to_string())

# Step 5: Find eps-neighbours of each point (point itself included)
neighbours = distances <= eps

df["Neighbours"] = [", ".join(df["Point"][row]) for row in neighbours]
df["Count"] = neighbours.sum(axis=1)

# Step 6: Classify each point as Core, Border or Noise
is_core = df["Count"] >= min_pts
is_border = ~is_core & neighbours[:, is_core].any(axis=1)

df["Type"] = np.where(is_core, "Core", np.where(is_border, "Border", "Noise"))

print("\nNeighbourhoods and Point Types:")
print(df[["Point", "X", "Y", "Neighbours", "Count", "Type"]]
      .to_string(index=False))

# Step 7: Apply DBSCAN clustering
model = DBSCAN(eps=eps, min_samples=min_pts, metric="euclidean")

model.fit(X)

# Step 8: Display final clusters (-1 means noise)
df["Cluster"] = np.where(model.labels_ == -1, "Noise", (model.labels_ + 1).astype(str))

print("\nFinal Cluster Assignments:")
print(df[["Point", "X", "Y", "Type", "Cluster"]]
      .to_string(index=False))

# Step 9: Display cluster summary
print("\nCluster Summary:")

for label in sorted(set(model.labels_)):
    members = df.loc[model.labels_ == label, "Point"].tolist()
    name = "Noise" if label == -1 else f"Cluster {label + 1}"
    print(f"{name}: {', '.join(members)}")

# Step 10: Plot the clusters
colors = {"1": "tab:blue", "2": "tab:orange", "3": "tab:green", "Noise": "gray"}
markers = {"Core": "o", "Border": "s", "Noise": "X"}

fig, ax = plt.subplots(figsize=(8, 7))

# eps-circle around each core point shows its neighbourhood
for _, row in df[df["Type"] == "Core"].iterrows():
    ax.add_patch(plt.Circle((row["X"], row["Y"]), eps,
                            color=colors[row["Cluster"]], alpha=0.12))

for _, row in df.iterrows():
    ax.scatter(row["X"], row["Y"], s=160, edgecolors="black",
               c=colors[row["Cluster"]], marker=markers[row["Type"]])
    ax.annotate(row["Point"], (row["X"], row["Y"]),
                textcoords="offset points", xytext=(8, 8))

# Legend: one entry per cluster colour and per point type
legend = [Line2D([], [], marker="o", linestyle="", markersize=10,
                 color=colors[c], label=f"Cluster {c}")
          for c in sorted(df["Cluster"].unique()) if c != "Noise"]
legend += [Line2D([], [], marker=m, linestyle="", markersize=10,
                  color="gray" if t == "Noise" else "white",
                  markeredgecolor="black", label=t)
           for t, m in markers.items()]
ax.legend(handles=legend, loc="upper right")

ax.set_title(f"DBSCAN Clustering (eps = {eps}, minPts = {min_pts})")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_aspect("equal")
ax.grid(True, alpha=0.3)

plt.savefig("dbscan_clusters.png", dpi=120, bbox_inches="tight")
print("\nPlot saved to dbscan_clusters.png")
plt.show()
