# IterativeClosestPoint Algorithm<br/>
1.Make data centered by subtracting the mean<br/>
2.Find correspondences for each point in P<br/>
3.Perform a single iteration by computing the cross-covariance matrix and performing the SVD(Singular Value Decomposition)<br/>
4.Apply the found rotation to P<br/>
5.Repeat until correspondences don't change<br/>
6.Apply the found rotation to the mean vector of P and uncenter P with it<br/>
