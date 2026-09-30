import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Data
x = [-2, -1, 3]
y = [-6, -3, 9]

# Create dataset: each row is an observation
X = np.array(list(zip(x, y)))

print("Original Data:")
print(X)

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\nStandardized Data:")
print(X_scaled)

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("\nPCA Transformed Data:")
print(X_pca)

# Principal component directions
print("\nPrincipal Components:")
print(pca.components_)

# Explained variance
print("\nExplained Variance:")
print(pca.explained_variance_)

# Explained variance ratio
print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)

# Plot the PCA-transformed data
plt.scatter(X_pca[:, 0], X_pca[:, 1])

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA")
plt.grid()
plt.show()