import pandas as pd
import subprocess
def data_preprocessing(train):
    # Data Cleaning
    train = train.drop(columns='Cabin', axis=1)
    
    train['Age'] = train['Age'].astype(float)
    # replace null values with  mean of the Age column
    train['Age'].fillna(train['Age'].mean(), inplace=True)
    # replace null values with mode of the Embarked column
    train['Embarked'].fillna(train['Embarked'].mode()[0], inplace=True)
    # data normalization
    train.replace({'Sex':{'male':0,'female':1}, 'Embarked':{'S':0,'C':1,'Q':2}}, inplace=True)
    # remove useless  columns
    train= train.drop(columns = ['PassengerId','Name','Ticket'],axis=1)
    print(train.head())
    return train

def call_next_script():
    print("Calling eda.py...")
    subprocess.run(["python3", "eda.py"])

if __name__ == "__main__":
    file_path = "train_titanic.csv" 
    df = pd.read_csv(file_path)

    # Perform data preprocessing
    df_processed = data_preprocessing(df)

    # Save resulting data frame
    df_processed.to_csv("results/res_dpre.csv", index=False)
    call_next_script()

