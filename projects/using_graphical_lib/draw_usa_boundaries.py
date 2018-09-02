"""
Week 1 practice project template for Python Data Visualization
Load a county-level PNG map of the USA and draw it using matplotlib
"""

import matplotlib.pyplot as plt

# Houston location

USA_SVG_SIZE = [555, 352]


def draw_USA_map(map_name):
    """
    Given the name of a PNG map of the USA (specified as a string),
    draw this map using matplotlib
    """
     
    # Load map image, note that using 'rb'option in open() is critical since png files are binary
    image = open('projects/using_graphical_lib/{}'.format(map_name),'rb')
    
    #  Get dimensions of USA map image
    result = plt.imread(image)
    d1 = result.size
    d2 = result[0].size

    # Plot USA map
    plt.imshow()
    
    # Plot green scatter point in center of map
     
    # Plot red scatter point on Houston, Tx - include code that rescale coordinates for larger PNG files
    pass

#draw_USA_map("USA_Counties_555x352.png")
draw_USA_map("USA_Counties_1000x634.png")   
