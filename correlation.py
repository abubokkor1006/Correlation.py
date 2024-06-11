import numpy as np

def calculate_correlation(x, y):
    """
    Calculate the Pearson correlation coefficient between two arrays.
    
    Parameters:
    x (list or np.array): First set of observations
    y (list or np.array): Second set of observations
    
    Returns:
    float: Pearson correlation coefficient
    """
    # Convert to numpy arrays if not already
    x = np.array(x)
    y = np.array(y)
    
    # Ensure the lengths of x and y are the same
    if len(x) != len(y):
        raise ValueError("The number of observations in x and y must be the same")
    
    # Calculate the means of x and y
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    
    # Calculate the deviations from the mean
    dev_x = x - mean_x
    dev_y = y - mean_y
    
    # Calculate the covariance
    covariance = np.sum(dev_x * dev_y)
    
    # Calculate the standard deviations
    std_x = np.sqrt(np.sum(dev_x ** 2))
    std_y = np.sqrt(np.sum(dev_y ** 2))
    
    # Calculate the correlation coefficient
    correlation_coefficient = covariance / (std_x * std_y)
    
    return correlation_coefficient

def get_observations():
    """
    Get observations from the user.
    
    Returns:
    tuple: Two lists containing the observations for x and y
    """
    x = list(map(float, input("Enter observations for x, separated by spaces: ").split()))
    y = list(map(float, input("Enter observations for y, separated by spaces: ").split()))
    
    return x, y

# Get observations from the user
x, y = get_observations()

# Calculate the correlation
correlation = calculate_correlation(x, y)
print(f"Correlation coefficient: {correlation}")