import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, pi


#returns alist of indexes of minimum distances form original point cloud to the moved point cloud
def Corresspondences(moved_data, original_data):
    m_size = moved_data.shape[1]
    o_size = original_data.shape[1]
    correspondences = []
    for i in range(m_size):
        m_point = moved_data[:, i]
        minimumDist = 1000
        index = -1
        for j in range(o_size):
            o_point = original_data[:, j]
            dist = np.linalg.norm(o_point - m_point)
            if dist < minimumDist:
                minimumDist = dist
                index = j
        correspondences.append((i, index))
    return correspondences




def plot_data(A, B):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    ax.axis('equal')
    if A is not None:
        xA, yA = A
        ax.plot(xA, yA, color='#336699',  marker='o' ,label="Moved Data" )
    if B is not None:
        xB, yB = B
        ax.plot(xB, yB, color='green', marker='o',label="Original Data")
    ax.legend()
    return ax



# initialize pertrubation rotation
angle = pi / 4
R_true = np.array([[cos(angle), -sin(angle)], 
                   [sin(angle),  cos(angle)]])
t_true = np.array([[1], [3]])

# Generate data as a list of 2d points
num_points = 40
true_data = np.zeros((2, num_points))
true_data[0, :] = range(0, num_points)
true_data[1, :] = 0.2 * true_data[0, :] * np.sin(0.5 * true_data[0, :]) 
# Move the data
moved_data = R_true.dot(true_data) + t_true

# Assign to variables we use in formulas.
original_data = true_data
moved_data = moved_data


plot_data(moved_data, true_data)
plt.show()



#mean is the sum of data divided by the number of data-points
#measure of the central location of data in a set of values  
def centerPoint(data, exclude_indices=[]):
    reduced_data = np.delete(data, exclude_indices, axis=1)
    center = np.array([reduced_data.mean(axis=1)]).T
    return center, data - center




def crossCovariance(moved_data, original_data, correspondences, kernel=lambda diff: 1.0):
    covariance = np.zeros((2, 2))
    exclude_indices = []
    for i, j in correspondences:
        m_point = moved_data[:, [i]]
        o_point = original_data[:, [j]]
        weight = kernel(m_point - o_point)
        if weight < 0.01: exclude_indices.append(i)
        covariance += weight * o_point.dot(m_point.T)
    return covariance, exclude_indices


Rotation=[]
Translation=[]

def ICP(moved_data, original_data, iterations=5):
    #finding centre pf original data
    center_of_original_data, original_data_centered = centerPoint(original_data)

    moved_data_values = [moved_data.copy()]
    moved_data_copy = moved_data.copy()
    corresp_values = []
    exclude_indices = []
    finalRotation=[[ 1,  0],
    [0,  1]]
    finalTranslation= [[0],[0]]
    
    #iterations
    for i in range(iterations):
        #finding centre pf moved data
        center_of_moved_data, moved_data_centered = centerPoint(moved_data_copy, exclude_indices=exclude_indices)
        
        #finding corresspondences
        correspondences = Corresspondences(moved_data_centered, original_data_centered)
        corresp_values.append(correspondences)
        
        #finding covariance and excluded indices
        covariance, exclude_indices = crossCovariance(moved_data_centered, original_data_centered, correspondences)
        
        #applying singular value decomposition on Covariance
        U, S, V_T = np.linalg.svd(covariance)
        
        #Here we get the rotation for i'th iteration
        R = U.dot(V_T)  
        finalRotation = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*R)] for X_row in finalRotation]
        
        #Here we get the translation for i'th iteration
        t = center_of_original_data - R.dot(center_of_moved_data)  
        finalTranslation = [[finalTranslation[i][j] + t[i][j]  for j in range(len(finalTranslation[0]))] for i in range(len(finalTranslation))]
        
        #applying rotation and translation
        moved_data_copy = R.dot(moved_data_copy) + t
        moved_data_values.append(moved_data_copy)
        
        
    corresp_values.append(corresp_values[-1])
    
    Rotation=finalRotation
    Translation=finalTranslation


    return moved_data_values, corresp_values,Rotation,Translation


moved_data_values, corresp_values,Rotation,Translation = ICP(moved_data, original_data)
ax = plot_data(moved_data_values[-1], original_data)
plt.show()

print("Final Matrix of Rotation " ,Rotation)
print("Final Matrix of Translation " ,Translation)
