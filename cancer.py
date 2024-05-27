import pandas as pd 

# To load Cancer's dataset directly from the web-url run this
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wpbc.data'
column_names = [
    'ID', 'Outcome', 'Time', 'radius_mean', 'texture_mean', 'perimeter_mean', 
    'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean', 
    'concave_points_mean', 'symmetry_mean', 'fractal_dimension_mean', 
    'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se', 
    'compactness_se', 'concavity_se', 'concave_points_se', 'symmetry_se', 
    'fractal_dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst', 
    'area_worst', 'smoothness_worst', 'compactness_worst', 'concavity_worst', 
    'concave_points_worst', 'symmetry_worst', 'fractal_dimension_worst', 
    'Tumor_Size', 'Lymph_Node_Status'
]
# Load the dataset
data = pd.read_csv(url, header=None, names=column_names)
print(data.head(10))

