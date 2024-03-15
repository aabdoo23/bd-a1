from sklearn.cluster import KMeans
import pandas as pd

def kmeans_clustering(df):
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(df[['Age', 'Fare']])
    
    labels = kmeans.labels_
    cluster_counts = pd.Series(labels).value_counts().sort_index()
    with open('results/k.txt', 'w') as file:
        for cluster, count in cluster_counts.items():
            file.write(f'Cluster {cluster}: {count}\n')

if __name__ == "__main__":
    file_path = "results/res_dpre.csv" 
    df = pd.read_csv(file_path)

    kmeans_clustering(df)
    print("End of pipeline.")