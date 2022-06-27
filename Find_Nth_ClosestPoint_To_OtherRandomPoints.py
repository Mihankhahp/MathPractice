
import numpy as np
import random


def nth_closest_point_to_random_point(
        endCor,
        n_points,
        random_seed,
        n_closest,
        new_coor):

    random.seed(float(random_seed))
    endCor, new_coor = endCor.split(","), new_coor.split(",")
    ndims = len(endCor)
    upper_corner = []
    n_coor = []

    for i in range(ndims):
        upper_corner.append(int(endCor[i]))
        n_coor.append(int(new_coor[i]))

    n_points = int(n_points)

    points = []

    for i in range(n_points):
        point = []

        for j in range(ndims):
            point.append(random.randint(0, upper_corner[j]))

        points.append(point)

    points = np.array(points)
    n_coor = np.array(n_coor)

    distances = np.linalg.norm(points-n_coor, axis=1)

    sorted_dists = np.sort(distances)

    print(sorted_dists[int(n_closest)-1])


nth_closest_point_to_random_point(
    input("Import the area cordination with ", " after each number ==>   "),
    input("How many random points do you want? ==>   "),
    input("Enter random seed ?==>  "),
    input("The nth closest point ==>   "),
    input("New coordinate? ==>  "))
