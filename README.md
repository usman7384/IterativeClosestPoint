# IterativeClosestPoint Algorithm
1.Make data centered by subtracting the mean
2.Find correspondences for each point in P
3.Perform a single iteration by computing the cross-covariance matrix and performing the SVD
4.Apply the found rotation to P
5.Repeat until correspondences don't change
6.Apply the found rotation to the mean vector of P and uncenter P with it
