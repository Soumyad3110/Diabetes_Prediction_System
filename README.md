# 🧠 Diabetes Prediction Using Random Forest Classifier

Welcome to the **Diabetes Prediction Project**! This machine learning project aims to predict whether an individual has diabetes based on medical diagnostic data. We use the **Random Forest Classifier**, a powerful ensemble learning algorithm, for classification.

---
## 📁 Dataset Overview

> Project Structure
- `README.md`: Explains the details of the project
- `main.py`: Run the pipeline
- `src/`: Source code
- `data/`: Dataset file (diabetes.csv)
- `notebooks/`: Jupyter notebooks for exploration
- `results.ipynb`: Confusion matrix, ROC curve, EDA plots
- `setup.py`: Packaging the project as a module.
- `config.yaml`: Settings and paths
- `environment.yml`: If using conda. Alternative to requirements.txt.
- `.gitignore`: Lists files/folders Git should ignore (e.g., __pycache__, .ipynb_checkpoints/)
- **Source**: Pima Indians Diabetes Database
- **Samples**: 768
- **Features**: 8 medical attributes
- **Target**: `Outcome` (0 = Non-Diabetic, 1 = Diabetic)

### 🔬 Features Description:

| Feature                    | Description                                      |
|---------------------------|--------------------------------------------------|
| Pregnancies               | Number of pregnancies                           |
| Glucose                   | Plasma glucose concentration                    |
| BloodPressure             | Diastolic blood pressure (mm Hg)               |
| SkinThickness             | Triceps skin fold thickness (mm)               |
| Insulin                   | 2-Hour serum insulin (mu U/ml)                 |
| BMI                       | Body mass index                                 |
| DiabetesPedigreeFunction  | Diabetes pedigree function                      |
| Age                       | Age in years                                     |
| Outcome                   | Class variable (0 or 1)                         |

---

## 🧰 Tech Stack & Libraries Used

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/3/31/NumPy_logo_2020.svg" alt="NumPy" width="60"/>
  &nbsp;&nbsp;&nbsp;
  <img src="https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg" alt="Pandas" width="60"/>
  &nbsp;&nbsp;&nbsp;
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg" alt="Matplotlib" width="50"/>
  &nbsp;&nbsp;&nbsp;
  <img src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" alt="Seaborn" width="100"/>
  &nbsp;&nbsp;&nbsp;
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="Scikit-learn" width="100"/>
</p>

### 📦 Libraries
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`

---

## 🧪 Project Workflow

### 📊 1. Exploratory Data Analysis (EDA)
- Summary statistics
- Missing value analysis
- Correlation matrix
- Violin plots and scatter plots

### 🛠️ 2. Data Preprocessing
- Feature-target separation
- Train-test split (`70% train / 30% test`)
- Outlier detection using IQR

### 🌳 3. Model Building - Random Forest Classifier
- Default training with `n_estimators=100`
- Feature importance ranking
- Grid search with `GridSearchCV`
  
### 🧾 4. Model Evaluation
- Accuracy
- Precision, Recall, F1-Score
- Confusion Matrix
- ROC-AUC Curve
- Precision-Recall Curve

---

## 🎯 Results

- ✅ **Train Accuracy**: 100% (initial)
- ✅ **Test Accuracy** (tuned): ~75.6%

-- 
# 🧠 Final Thoughts

💡 Top 3 Influential Features:

- Glucose
- BMI
- Age

📈 Visual Insights
- Confusion Matrix
- Feature Importance
- ROC Curve
- Precision-Recall Curve
= Violin Plot
- Correlation Heatmap

🚀 Future Improvements: 
Try different models (XGBoost, Logistic Regression, SVM)
- Handle class imbalance (e.g., SMOTE)
- Web deployment (Flask / Streamlit)
- Model saving (joblib or pickle)

👨‍💻 Author: Soumyadeep Dutta

