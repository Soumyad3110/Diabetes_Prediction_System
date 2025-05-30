# src/model.py

from sklearn.ensemble import RandomForestClassifier

def train_random_forest(X_train, y_train):
    """
    Trains a RandomForestClassifier.
    """
    print("Training RandomForestClassifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model
