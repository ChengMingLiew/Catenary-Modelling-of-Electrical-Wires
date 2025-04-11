# About the project

For this project, we are using LiDAR point cloud datasets in .parquet files (https://enea.egnyte.com/fl/ublORUqrwH) and to generate the best fit Catenary models for each wire within the dataset. 

The model will follow the Catenary equation:

$$ y(x) = y_0 + c x [cosh(\frac{x - x_0}{c} - 1] $$

Where $c$ is a curvature parameter, x is the distance along the wire $x_0$ is the $x$ value of the trough, $y$ is the elevation of the wire, and $y_0$ is the lowest elevation of the wire.

## Getting started
To get started there are some libraries and dependencies where we have to install before setting up the project locally.
- Downloading requirments.txt
```
$ pip install -r requirements.txt
```

This will allow for us to have the proper tools to be able to run our Jupyter folder 'finding_catenary' in order to find the best fit Catenary models.
