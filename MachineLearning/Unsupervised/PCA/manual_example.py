import numpy as np
import matplotlib.pyplot as plt

# Hand-calculated PCA example: 3 points where Y = 3X
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
INK, MUTED, GRID = "#0b0b0b", "#52514e", "#e4e3df"

# Step 1: Data and centroid
X = np.array([[-2, -6], [-1, -3], [3, 9]], dtype=float)
centroid = X.mean(axis=0)                      # (0, 0)
X_centered = X - centroid

# Step 2: Covariance matrix = 1/2 * X^T X  ->  [[7, 21], [21, 63]]
C = X_centered.T @ X_centered / (len(X) - 1)

# Step 3: Eigenvalues 70 and 0, eigenvectors [1, 3]/sqrt(10) and [-3, 1]/sqrt(10)
pc1 = np.array([1, 3]) / np.sqrt(10)
pc2 = np.array([-3, 1]) / np.sqrt(10)

# Step 4: Project onto PC1  ->  [-6.32, -3.16, 9.49]
scores = X_centered @ pc1
print("Covariance matrix:\n", C)
print("PC1 scores:", scores.round(2))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6), gridspec_kw={"width_ratios": [1, 1.25]})
for ax in (ax1, ax2):
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(MUTED)
    ax.tick_params(colors=MUTED)

# Left: original 2D data with principal components
t = np.linspace(-11, 11, 2)
ax1.plot(t * pc1[0], t * pc1[1], color=BLUE, linewidth=2, alpha=0.35, zorder=1)
ax1.axhline(0, color=GRID, linewidth=1, zorder=0)
ax1.axvline(0, color=GRID, linewidth=1, zorder=0)
ax1.scatter(X[:, 0], X[:, 1], s=90, color=INK, edgecolor="white", linewidth=2, zorder=3,
            label="Data points")
for (x, y), name in zip(X, ["P1", "P2", "P3"]):
    ax1.annotate(f"{name} ({x:g}, {y:g})", (x, y), xytext=(10, -4),
                 textcoords="offset points", color=INK, fontsize=10)
ax1.scatter(*centroid, s=140, marker="X", color=ORANGE, edgecolor="white", linewidth=1.5,
            zorder=4, label="Centroid (0, 0)")
arrow_len = 4
ax1.annotate("", xy=pc1 * arrow_len, xytext=(0, 0),
             arrowprops=dict(arrowstyle="-|>", color=BLUE, linewidth=2.5, mutation_scale=18), zorder=5)
ax1.annotate("", xy=pc2 * arrow_len, xytext=(0, 0),
             arrowprops=dict(arrowstyle="-|>", color=AQUA, linewidth=2.5, mutation_scale=18), zorder=5)
ax1.text(*(pc1 * arrow_len + [0.3, 0.2]), "PC1 = [0.316, 0.949]\nλ = 70 (100%)", color=INK, fontsize=10)
ax1.text(*(pc2 * arrow_len + [-2.2, 0.7]), "PC2 = [-0.949, 0.316]\nλ = 0 (0%)", color=INK, fontsize=10)
ax1.set_xlim(-6, 6)
ax1.set_ylim(-10, 11)
ax1.set_aspect("equal")
ax1.set_xlabel("X", color=MUTED)
ax1.set_ylabel("Y", color=MUTED)
ax1.set_title("Before PCA: original data (Y = 3X)\nwith principal components", color=INK, fontsize=12, loc="left")
ax1.legend(frameon=False, loc="lower right", labelcolor=INK)

# Right: data reduced to 1D along PC1
ax2.axhline(0, color=BLUE, linewidth=2, alpha=0.35, zorder=1)
ax2.scatter(scores, np.zeros_like(scores), s=90, color=INK, edgecolor="white", linewidth=2, zorder=3)
ax2.scatter(0, 0, s=140, marker="X", color=ORANGE, edgecolor="white", linewidth=1.5, zorder=4)
for i, (s, name, (x, y)) in enumerate(zip(scores, ["P1", "P2", "P3"], X)):
    above = i != 1  # alternate label sides so neighbours never collide
    ax2.annotate(f"{name} = {s:.2f}\n0.316({x:g}) + 0.949({y:g})", (s, 0),
                 xytext=(0, 14 if above else -16), textcoords="offset points",
                 ha="center", va="bottom" if above else "top", color=INK, fontsize=9.5)
ax2.set_xlim(-9, 12)
ax2.set_ylim(-1, 1)
ax2.set_box_aspect(0.45)
ax2.set_yticks([])
ax2.spines["left"].set_visible(False)
ax2.set_xlabel("PC1 score", color=MUTED)
ax2.set_title("After PCA: 2D reduced to 1D along PC1\nvariance of scores = 70 = λ1, nothing lost",
              color=INK, fontsize=12, loc="left")

plt.tight_layout()
plt.savefig("pca_manual_example.png", dpi=130, facecolor="white")
plt.show()
