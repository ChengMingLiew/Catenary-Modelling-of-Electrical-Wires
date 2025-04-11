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
