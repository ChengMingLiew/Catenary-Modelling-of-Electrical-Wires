import matplotlib.pyplot as plt

# Plotting the intial LiDAR data 
def xyz_3d_plot(lidar_df):

    fig = plt.figure(figsize=(10, 7))
    initial_plot = fig.add_subplot(111, projection='3d')

    initial_plot.scatter(lidar_df['x'], 
                        lidar_df['y'], 
                        lidar_df['z'], 
                        s=5, alpha=0.6)

    initial_plot.set_xlabel('X')
    initial_plot.set_ylabel('Y')
    initial_plot.set_zlabel('Z')
    plt.title('LiDAR Point Cloud')
    plt.show()

# Plotting the cables on the X-Y plane with cabel labels
def xy_cable_plot(cable_points, label):
    
    colour = plt.cm.tab20(label % 20)

    plt.figure(figsize=(8, 6))
    plt.scatter(cable_points['x'], 
                cable_points['y'], 
                color=colour, s=10)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Cable {label} on the XY Plane')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# Plotting the wires in 3d with wire labels
def plot_3d_wire_clusters(lidar_df):

    fig = plt.figure(figsize=(10, 7))
    wire_clusters = fig.add_subplot(111, projection='3d')

    for label in sorted(lidar_df['global_wire'].unique()):
        cluster_points = lidar_df[lidar_df['global_wire'] == label]
        ax.scatter(cluster_points['x'], 
                   cluster_points['y'], 
                   cluster_points['z'], 
                   label=f'Wire {label}', s=10)

    wire_clusters.set_title('3D Wire Plot')
    wire_clusters.set_xlabel('x')
    wire_clusters.set_ylabel('y')
    wire_clusters.set_zlabel('z')
    wire_clusters.legend()
    plt.show()