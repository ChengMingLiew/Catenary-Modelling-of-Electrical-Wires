from sklearn.cluster import DBSCAN
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from kneed import KneeLocator
import matplotlib.pyplot as plt

# Cluster each group of wires into cables using DBScan
def cluster_cables(lidar_df):

    coords = lidar_df[['x', 'y', 'z']].values
    dbscan = DBSCAN(eps=0.9, min_samples=6)  
    labels = dbscan.fit_predict(coords)

    lidar_df['cable'] = labels

    fig = plt.figure(figsize=(10, 7))
    clustered = fig.add_subplot(111, projection='3d')

    for label in np.unique(lidar_df['cable']):

        cable_points = lidar_df[lidar_df['cable'] == label]

        colour = plt.cm.tab20(label % 20) if label != -1 else 'k'  
        label_name = f'Cable {label}' if label != -1 else 'Noise'
        
        clustered.scatter(cable_points['x'], 
                        cable_points['y'], 
                        cable_points['z'],
                        s=5, c=[colour], label=label_name)

    clustered.set_title("LiDAR Wire Clusters")
    clustered.set_xlabel('X')
    clustered.set_ylabel('Y')
    clustered.set_zlabel('Z')
    clustered.legend(title='Cable', bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.show()

# Clustering the cable into individual wires using PCA and K-means
def clustering_individual_wires(cable_points, cable_num):

    # Using PCA to get the orthogonal vector
    pca = PCA(n_components=2)
    pca.fit(cable_points[['x', 'y']])
    normal = pca.components_[1]   

    # Projecting the points onto the orthogonal Line
    projected = cable_points[['x', 'y']].dot(normal)

    # Finding the optimal K with the Elbow Method
    k_values = list(range(2, 11))
    inertias = []
    for k in k_values:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(projected.values.reshape(-1, 1))
        inertias.append(kmeans.inertia_)

    # Using KneeLocator to find the Elbow point
    kl = KneeLocator(k_values, inertias, curve="convex", direction="decreasing")
    best_k = kl.elbow

    # Clustering the points
    best_kmeans = KMeans(n_clusters=best_k, random_state=42)
    cable_points.loc[:, 'wire'] = best_kmeans.fit_predict(projected.values.reshape(-1, 1))

    plt.figure(figsize=(8, 6))
    for label in sorted(cable_points['wire'].unique()):
        wire_points = cable_points[cable_points['wire'] == label]
        plt.scatter(wire_points['x'], 
                    wire_points['y'], 
                    label=f'Wire {label}')

    plt.legend()
    plt.title(f'Clustering Cable {cable_num} into {len(cable_points['wire'].unique())} Wires')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

    return cable_points