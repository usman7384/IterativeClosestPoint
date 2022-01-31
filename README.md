# IterativeClosestPoint Algorithm
Make data centered by subtracting the mean
Find correspondences for each point in P
Perform a single iteration by computing the cross-covariance matrix and performing the SVD
Apply the found rotation to P
Repeat until correspondences don't change
Apply the found rotation to the mean vector of P and uncenter P with it
