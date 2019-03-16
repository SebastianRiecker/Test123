def calc_dataset(numbercount, bincount):
    """Generates numbercount random numbers and calculates histogram data with num_bins number 
    of bins."""
    import numpy as np
    random_numbers = np.random.random(numbercount)*2*np.pi
    histogram_data = np.histogram(random_numbers, bincount, range=(0,2*np.pi))
    histogram_data_normalized = random_numbers-np.mean(random_numbers)
    histogram_std = np.std(random_numbers)
    histogram_av = np.mean(random_numbers)
    return histogram_data, histogram_data_normalized, histogram_std, histogram_av


def generate_bin_positions(bincount):
    """Calculate equally spacced bin positions in rad and degree based on bin numbers"""
    import numpy as np
    angles_deg = np.linspace(0, 360, bincount+1)[:-1]
    angles_rad = np.linspace(0, 2*np.pi, bincount+1)[:-1]
    return angles_deg, angles_rad


def convert_polar_to_kartesian(phi):
    ''' Polar coordinates theta to kartesian coordinates x,y. Return x,y'''
    import numpy as np
    x = 1 * np.cos(phi) # r=1
    y = 1 * np.sin(phi) # r=1
    return x, y


def convert_kartesion_to_polar(x,y):
    """Convert kartesioan coordinates in agnle phi in polar coordinates."""
    import math
    phi = math.atan2(y,x)
    return phi


def calculate_effective_force(x,y):
    ''' Calculate the effective Force out of given Forces (x-vector, y-vector as numpy array). Return effective Force effForce'''
    import numpy as np
    Fx    = np.sum(x)  
    Fy    = np.sum(y)
    F     = np.sqrt(Fx**2 + Fy**2)
    return Fx,Fy, F


def make_bar_plot(angles_deg, histogram_data, histogram_data_normalized, bincount, numbercount, effective_force):
    """Generate two barplots based on given histogram data"""
    import matplotlib.pyplot as plt
    fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(8, 4))
    ax0.bar(angles_deg, histogram_data, width = 360/bincount)
    ax0.set_title(f'Set a, N = {numbercount}')
    ax1.bar(angles_deg, histogram_data_normalized, width = 360/bincount)
    ax1.set_title('Set a - norm., F = '+str(round(effective_force,2)))
    fig.tight_layout()
    return plt.show()
    
