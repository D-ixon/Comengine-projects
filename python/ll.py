from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import fetch_openml

# 1. Load the data
mnist = fetch_openml('mnist_784', version=1, as_frame=False)
X, y = mnist.data, mnist.target

# Split into training and test sets (standard MNIST split is 60k/10k)
X_train, X_test = X[:60000], X[60000:]
y_train, y_test = y[:60000], y[60000:]

# 2. Define the parameter grid
param_grid = [
    {
        'n_neighbors': [3, 4, 5],
        'weights': ['uniform', 'distance']
    }
]

# 3. Perform Grid Search
# n_jobs=-1 uses all available CPU cores to speed up the search
knn_clf = KNeighborsClassifier()
grid_search = GridSearchCV(knn_clf, param_grid, cv=3, verbose=2, n_jobs=-1)
grid_search.fit(X_train, y_train)

# 4. Evaluate the best model
print("Best parameters:", grid_search.best_params_)
print("Best score:", grid_search.best_score_)

best_model = grid_search.best_estimator_
accuracy = best_model.score(X_test, y_test)
print(f"Test set accuracy: {accuracy:.4f}")