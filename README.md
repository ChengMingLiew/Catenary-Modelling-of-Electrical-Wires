# About the project

For this project, we are using LiDAR point cloud datasets in .parquet files (https://enea.egnyte.com/fl/ublORUqrwH) and to generate the bets fit Catenary models for each wire within the dataset. 
The model will follow the Catenary equation:

$$ y(x) = y_0 + c x [cosh(\frac{x - x_0}{c} - 1] $$

where $c$ is a curvature parameter, x is the distance along the wire $x_0$ is the $x$ value of the trough, $y$ is the elevation of the wire, and $y_0$ is the lowest elevation of the wire.
