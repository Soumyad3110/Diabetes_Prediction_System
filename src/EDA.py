import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def perform_eda(data_path):
    df = pd.read_csv(data_path)

    # Create output directory if it doesn't exist
    os.makedirs("output", exist_ok=True)

    # Summary statistics
    print("Summary Statistics:\n")
    print(df.describe())

    # Class distribution
    plt.figure(figsize=(6, 4))
    sns.countplot(x='Outcome', data=df)
    plt.title("Class Distribution")
    plt.savefig("output/class_distribution.png")
    plt.show()

    # Correlation heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title("Feature Correlation")
    plt.savefig("output/correlation_heatmap.png")
    plt.show()

    print("EDA visuals saved in output/")
    
    # Plotting violin plot using the original DataFrame

    plt.figure(figsize = (16,8))
    sns.violinplot(x='Age', y='Glucose', data=df, inner='box', color='yellow', saturation=0.75)
    plt.title('Glucose Distribution by Age (Violin Plot)')
    plt.show()
    
    # Plotting a line plot for visualization using original dataframe

    plt.figure(figsize = (16,8))
    sns.lineplot(x = 'Age', y = 'Glucose', data = df)
    sns.scatterplot(x='Age', y='Glucose', data=df, color='red')
    plt.title('Glucose Distribution by Age (Line Plot)')
    plt.show()
    
    # Outlier detection using IQR

    df=np.random.normal(loc=0,size=100,scale=1)
    len(df), df

    Q1=np.percentile(df,25)
    Q3=np.percentile(df,75)
    IQR=Q3-Q1
    print(IQR)
    
    # Calculate upper and lower boundaries for outliers

    lower_boundary = Q1 - 1.5 * IQR
    upper_boundary = Q3 + 1.5 * IQR

    print("Lower boundary for outliers:", lower_boundary)
    print("Upper boundary for outliers:", upper_boundary)
    
    # Find outliers

    outliers = df[(df < lower_boundary) | (df > upper_boundary)]
    print("Number of outliers:", len(outliers))
    print("Outliers:", outliers)
    
    # Create a box plot using seaborn

    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, color='grey')
    plt.title('Box Plot for Outlier Detection')
    plt.ylabel('Values')
    plt.show()