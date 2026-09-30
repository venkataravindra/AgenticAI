import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

np.set_printoptions(precision=4, suppress=True)

# ============================================================
# PART 1: PCA from scratch (step by step) on a small 2D dataset
# ============================================================

# Step 1: Create the dataset
data = {
    "X": [2.5, 0.5, 2.2, 1.9, 3.1, 2.3, 2.0, 1.0, 1.5, 1.1],
    "Y": [2.4, 0.7, 2.9, 2.2, 3.0, 2.7, 1.6, 1.1, 1.6, 0.9]
}
df = pd.DataFrame(data)
X = df.values
print("Step 1: Original data")
print(df, "\n")

# Step 2: Center the data (subtract the mean of each feature)
mean = X.mean(axis=0)
X_centered = X - mean
print("Step 2: Mean of each feature:", mean)
print("Centered data:\n", X_centered, "\n")

# Step 3: Covariance matrix
cov_matrix = np.cov(X_centered, rowvar=False)
print("Step 3: Covariance matrix:\n", cov_matrix, "\n")

# Step 4: Eigenvalues and eigenvectors of the covariance matrix
eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

# Step 5: Sort by eigenvalue (largest first)
order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[order]
eigenvectors = eigenvectors[:, order]
print("Step 4-5: Eigenvalues (sorted):", eigenvalues)
print("Eigenvectors (columns = PC1, PC2):\n", eigenvectors, "\n")

# Step 6: Explained variance ratio
explained = eigenvalues / eigenvalues.sum()
print("Step 6: Explained variance ratio:", explained, "\n")

# Step 7: Project the data onto the top k components (k = 1)
k = 1
W = eigenvectors[:, :k]
X_projected = X_centered @ W
print(f"Step 7: Data projected onto top {k} component:\n", X_projected.ravel(), "\n")

# Step 8: Reconstruct back to 2D (shows the information that is kept)
X_reconstructed = X_projected @ W.T + mean

# Verify with scikit-learn (signs of components may be flipped - that is fine)
sk_pca = PCA(n_components=1).fit(X)
print("scikit-learn explained variance ratio:", sk_pca.explained_variance_ratio_)
print("scikit-learn PC1:", sk_pca.components_[0], "\n")

# Plot: original data, principal axes and projection
plt.figure(figsize=(6, 6))
plt.scatter(X[:, 0], X[:, 1], label="Original data", color="tab:blue")
plt.scatter(X_reconstructed[:, 0], X_reconstructed[:, 1],
            label="Projected onto PC1", color="tab:orange", marker="x")
for i in range(len(X)):
    plt.plot([X[i, 0], X_reconstructed[i, 0]], [X[i, 1], X_reconstructed[i, 1]],
             color="gray", linestyle=":", linewidth=1)
for j, color in zip(range(2), ["tab:red", "tab:green"]):
    vec = eigenvectors[:, j] * np.sqrt(eigenvalues[j]) * 1.2
    plt.annotate("", xy=mean + vec, xytext=mean,
                 arrowprops=dict(arrowstyle="->", color=color, linewidth=2))
    plt.text(*(mean + vec * 1.15), f"PC{j + 1}", color=color, fontsize=11, weight="bold")
plt.xlim(0, 3.6)
plt.ylim(0, 3.6)
plt.gca().set_aspect("equal")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("PCA from scratch: principal axes and projection")
plt.legend()
plt.tight_layout()
plt.savefig("pca_scratch.png", dpi=120)

# ============================================================
# PART 2: PCA with scikit-learn on the Iris dataset (4D -> 2D)
# ============================================================

iris = load_iris()
X_iris, y_iris = iris.data, iris.target

# Step 1: Standardize (PCA is sensitive to feature scale)
X_scaled = StandardScaler().fit_transform(X_iris)

# Step 2: Fit PCA with all components to inspect explained variance
pca_full = PCA().fit(X_scaled)
print("Iris explained variance ratio:", pca_full.explained_variance_ratio_)
print("Cumulative:", np.cumsum(pca_full.explained_variance_ratio_), "\n")

# Step 3: Reduce to 2 components
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
print("Iris shape before PCA:", X_iris.shape, "after PCA:", X_pca.shape)
print("Loadings (how much each feature contributes to each PC):")
print(pd.DataFrame(pca.components_, columns=iris.feature_names,
                   index=["PC1", "PC2"]).round(3), "\n")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Scree plot
n = len(pca_full.explained_variance_ratio_)
axes[0].bar(range(1, n + 1), pca_full.explained_variance_ratio_, label="Individual")
axes[0].plot(range(1, n + 1), np.cumsum(pca_full.explained_variance_ratio_),
             marker="o", color="tab:red", label="Cumulative")
axes[0].set_xticks(range(1, n + 1))
axes[0].set_xlabel("Principal component")
axes[0].set_ylabel("Explained variance ratio")
axes[0].set_title("Scree plot")
axes[0].legend()

# 2D projection
for label, color in zip(range(3), ["tab:blue", "tab:orange", "tab:green"]):
    mask = y_iris == label
    axes[1].scatter(X_pca[mask, 0], X_pca[mask, 1], color=color,
                    label=iris.target_names[label], alpha=0.8)
axes[1].set_xlabel(f"PC1 ({pca.explained_variance_ratio_[0]:.1%})")
axes[1].set_ylabel(f"PC2 ({pca.explained_variance_ratio_[1]:.1%})")
axes[1].set_title("Iris projected onto 2 principal components")
axes[1].legend()

plt.tight_layout()
plt.savefig("pca_iris.png", dpi=120)
plt.show()
