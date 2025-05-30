# main.py

import yaml
from src.data_loader import load_data
from src.model import train_random_forest
from src.evaluation import evaluate_model
from src.visualization import plot_confusion_matrix, plot_roc_curve


# Load configuration
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)
    
with open("environment.yml", "r") as f:
    env_config = yaml.safe_load(f)
    
# Suppress warnings
import warnings
warnings.filterwarnings("ignore")

# Load data
df = load_data("C:/Users/KIIT/Downloads/diabetes.csv")

# Features and labels
target_col = "Outcome"
X = df.drop(columns=[target_col])
y = df[target_col]

# Train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = train_random_forest(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
evaluate_model(y_test, y_pred)

# Visualize
plot_confusion_matrix(y_test, y_pred)
plot_roc_curve(model, X_test, y_test)
