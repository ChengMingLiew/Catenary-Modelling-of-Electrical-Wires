# About the project

For this project, we are using LiDAR point cloud datasets in .parquet files (https://enea.egnyte.com/fl/ublORUqrwH) and to generate the best fit Catenary models for each wire within the dataset. 

The model will follow the Catenary equation:

$$ y(x) = y_0 + c x [cosh(\frac{x - x_0}{c} - 1] $$

Where $c$ is a curvature parameter, x is the distance along the wire $x_0$ is the $x$ value of the trough, $y$ is the elevation of the wire, and $y_0$ is the lowest elevation of the wire.

## Getting started
To get started, there are some libraries and dependencies where we have to install before setting up the project locally.

- Downloading requirements.txt
```
$ pip install -r requirements.txt
```

This will allow for us to have the proper tools to be able to run our Jupyter folder 'finding_catenary' in order to find the best fit Catenary models. 

## Usage
For this project, the parquet files have already been imported into the Jupyter file under the name 'finding_catenary'. In the first few coding blocks, you will notice that there is a line of code like so:

```python
difficulty = ['easy', 'medium', 'hard', 'extrahard']
choose_difficulty = random.randint(0, 3)

lidar_df = spark.read.parquet(f'lidar_cable/lidar_cable_points_{difficulty[choose_difficulty]}.parquet')
```

The difficulty of the parquet files chosen is currently set at random. However, by changing the choose_difficulty variable from 0 to 3, we are able to choose which difficulty we desire. Then by running the Jupyter notebook 'finding_catenary' we will be able to get the best catenary models for the wires that are found in the datasets.

## Steps to the Algorithm
### DBSCAN Algorithm
First, to handle for the case where there are mutliple bunches of wires that are present, and hanging with vastly different heights, we will be using DBSCAN to cluster those groups. The hyperparameter 'min_samples' is chosen to be $2 * d = 6$ following the guideline that it should be double the number of dimensionality our data, $d = 3$. For the hyperparameter 'eps', which defines the maximum distance allowed for two clusters to be within the cluster, the value 0.9 was arbitrarily chosen as this is what worked the best.

### K-Means and PCA Algorithm
Next, to label each individual wires from those bunches of wires, PCA algorithm and K-means were chosen. We start out by looking at only the x and y values of the data points for each groups of wires, by plotting out in the 2D plane. Visually, we can tell that the wires and separated and parallel to each other. By using PCA, we can find the orthogonal line, perpendicular to the direction of those wires. This allows us to then project those points onto the line, reducing it into a 1D problem, which we can then use K-Means to cluster and label those wires accordingly. The Elbow Method was also employed in this process, in order to find the optimal cluster number, K to label the wires.

### Finding the best plane for each wire cluster
By using 3 points from each wire cluster, we are able to create two coplanar vectors between those points. By finding the cross product between these 3 points, we are then able to find the coefficients of our 3d plane following the equation:

$$
Ax + By + Cz = D
$$
This is done with points taken from the trough of the wire, the start of the wire and the end of the wire. We then calculate the sum of the distance between all points in that wire cluster, from the plane, and choose the plane with the least distance, dubbing it as our best plane.

### Finding new x-y coordinates of the wire cluster
Then, we will project the points, onto the plane, giving us a new set of coordinates in 2d, in order to find the best catenary model. This is done by making a vector from our origin point (point from the plane), taking the dot product of thatvector with the unit normal vector, multiplying the unit normal vector by distnace, and then substracting that vector from our poin. This wil give us the projection of our point onto the plane in 3D.





