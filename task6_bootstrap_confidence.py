import numpy as np
X = np.array([12, 15, 14, 10, 9, 8, 13, 11, 16, 14], dtype=float)
N = 1000 
np.random.seed(42)  
sample_means = []

for _ in range(N):
    sample = np.random.choice(X, size=len(X), replace=True)
    sample_means.append(sample.mean())

sample_means = np.array(sample_means)
lower, upper = np.percentile(sample_means, [2.5, 97.5])

print("Original mean:", X.mean())
print(f"Bootstrap 95% CI for mean: [{lower:.3f}, {upper:.3f}]")
