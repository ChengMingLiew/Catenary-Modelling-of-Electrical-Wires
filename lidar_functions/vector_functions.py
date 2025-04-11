import numpy as np
import itertools
MAX_DISTANCE = 0.1

# Gets the plane equation (Ax + By + Cz = D) according to three points in the 3D space
def get_plane_equation(p1, p2, p3):

    p1 = np.array(p1)
    p2 = np.array(p2)
    p3 = np.array(p3)

    # Geting the coplanar vectors between the points
    v1 = p2 - p1
    v2 = p3 - p1

    # Cross product between the vectors of the three points
    normal = np.cross(v1, v2)
    A, B, C = normal

    D = -np.dot(normal, p1)

    return A, B, C, D

# Get 3 sets of the points at both ends of the wire, and at the trough of the wire
def get_three_points(wire_points):

    sorted_z = wire_points.sort_values('z').head(3).values
    sorted_end = wire_points.sort_values(['x', 'z'], ascending=[True, False]).head(3).values
    sorted_start = wire_points.sort_values(['x', 'z'], ascending=[False, False]).head(3).values

    return sorted_z, sorted_end, sorted_start

# Finding the best plane such that it has the least distance summed from all points in that wire
def get_best_plane(wire_points):

    best_plane = None
    point_origin = None
    max_inliers = 0
    epsilon = MAX_DISTANCE

    sorted_z, sorted_start, sorted_end = get_three_points(wire_points)
    
    # Getting all possible combinations of the three points
    combinations = list(itertools.product(sorted_start, sorted_end, sorted_z))

    for combo in combinations:

        A, B, C, D = get_plane_equation(combo[0], combo[1], combo[2])

        # Calculate the distance between the plane and the points
        distances = np.abs(A * wire_points['x'] + B * wire_points['y'] + C * wire_points['z'] + D)

        # Considered an inlier if the distance is less than epsilon
        inlier_count = np.sum(distances < epsilon)

        # Update if there is a better plane
        if inlier_count >= max_inliers:
            max_inliers = inlier_count
            best_plane = (A, B, C, D)
            point_origin = (combo[0][0], combo[0][1], combo[0][2])

    return best_plane, point_origin

# Projecting a point onto a plane by using a vector normal to the plane
def project_onto_plane(point, plane_point, normal):
    
    normal = normal / np.linalg.norm(normal)  
    v = point - plane_point                   
    dist = np.dot(v, normal)
    projected_point = point - dist * normal  
     
    return projected_point

# Getting the 2D Coordinates of the points on the wire projected onto the plane
def get_2d_points(wire_points, plane, point_origin):

    A, B, C, D = plane
    projected = []
    plane_normal = np.array([A, B, C])

    # Projecting the 3D points on to the plane
    for point in wire_points.values:
       projected.append(project_onto_plane(point, point_origin, plane_normal))

    # Constructing a coodinate system in the plane
    plane_normal = plane_normal / np.linalg.norm(plane_normal)

    # Normalising the normal vector
    min_idx = np.argmin(np.abs(plane_normal))
    arbitrary = np.zeros(3)
    arbitrary[min_idx] = 1.0

    # Getting two arbitrary orthogonal vectors that are not parallel to the normal
    u = np.cross(plane_normal, arbitrary)
    u = u / np.linalg.norm(u)

    v = np.cross(plane_normal, u)
    v = v / np.linalg.norm(v)

    # Changing the projected 3D points into 2D Coordinates of the plane
    points_2d = np.array([
        [np.dot(p - point_origin, u), -np.dot(p - point_origin, v)]
        for p in projected
    ])
    
    return points_2d