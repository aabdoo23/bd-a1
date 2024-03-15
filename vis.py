import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import subprocess

def create_visualization(df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df)
    plt.title("Visualization of Age vs Fare with Survival")
    plt.xlabel("Age")
    plt.ylabel("Fare")
    plt.savefig("results/vis.png")
    
    sns.countplot(x='Pclass', hue='Survived', data=df)
    plt.savefig("results/vis2.png")

def call_next_script():
    print("Calling model.py...")
    subprocess.run(["python3", "model.py"])

if __name__ == "__main__":
    file_path = "results/res_dpre.csv" 
    df = pd.read_csv(file_path)
    create_visualization(df)
    call_next_script()
