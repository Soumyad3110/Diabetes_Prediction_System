# src/evaluation.py

from sklearn.metrics import classification_report, accuracy_score

def evaluate_model(y_true, y_pred, model=None, X_test=None):
    """
    Evaluates and prints classification metrics.
    """
    acc = accuracy_score(y_true, y_pred)
    print("\nModel Evaluation")
    print("================")
    print(f"Accuracy: {acc:.2f}")
    print("Classification Report:")
    print(classification_report(y_true, y_pred))
