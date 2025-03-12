# Iterative Closest Point (ICP) Algorithm Implementation

## Overview
This project implements the **Iterative Closest Point (ICP) Algorithm** in Python to align two sets of 2D points. The algorithm iteratively finds the optimal rotation and translation that best aligns the **moved data** (a transformed dataset) with the **original data**.

## Features
- Generates synthetic 2D data and applies a known transformation.
- Finds **correspondences** between moved and original datasets.
- Computes **cross-covariance** and applies **Singular Value Decomposition (SVD)**.
- Iteratively updates the transformation matrix to align the datasets.
- Visualizes the alignment process using **Matplotlib**.

## Dependencies
Ensure you have the following libraries installed:
```bash
pip install numpy matplotlib
```

## How It Works
1. **Data Generation:**
   - A dataset (`original_data`) is generated.
   - A transformation (rotation and translation) is applied to create `moved_data`.
   
2. **Correspondence Matching:**
   - Each point in `moved_data` is matched to its nearest neighbor in `original_data`.
   
3. **Transformation Estimation:**
   - Compute the cross-covariance matrix.
   - Apply **Singular Value Decomposition (SVD)** to extract rotation `R`.
   - Compute translation `t`.
   
4. **Iteration:**
   - Apply `R` and `t` to `moved_data`.
   - Repeat until reaching a fixed number of iterations (default: 5).
   
5. **Visualization:**
   - The initial and final aligned point clouds are plotted.
   
## Code Structure
- `Corresspondences(moved_data, original_data)`: Finds nearest neighbors.
- `plot_data(A, B)`: Plots the point clouds.
- `centerPoint(data)`: Computes the centroid and centers the dataset.
- `crossCovariance(moved_data, original_data, correspondences)`: Computes weighted covariance.
- `ICP(moved_data, original_data, iterations)`: Main function implementing ICP.

## Running the Code
Run the script using:
```bash
python ICP.py
```
This will generate and align two 2D point sets while displaying the transformation results.

## Output
- The console prints the final **rotation matrix** and **translation vector**.
- The plots visually show how the datasets align over iterations.

## Limitations
- The algorithm runs for a **fixed number of iterations (5)** instead of checking for convergence.
- The final transformation does not explicitly re-center the dataset after applying rotation.

## Improvements
- Implement a stopping criterion based on correspondence stability.
- Optimize the nearest neighbor search using **k-d trees** for better performance.

## References
- Iterative Closest Point (ICP) Algorithm: [Wikipedia](https://en.wikipedia.org/wiki/Iterative_closest_point)

