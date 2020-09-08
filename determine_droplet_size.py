import os
import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

if __name__=="__main__":
    # Input parameters
    image_name = os.path.join("/Users/nrnatesh/shenlab/Droplet-organoid/image-scripts/input_images", "T2.tif")
    output_basename = "T2_out"
    output_image = os.path.join("output_images", "{}.png".format(output_basename))
    output_histogram = os.path.join("output_images", "{}_hist.png".format(output_basename))
    pixels_to_microns = 250/94 # <<<< @Naveen -- this may not be true for your images
    max_droplet_radius = 1000 #pixels

    # Reads in image
    img = cv2.imread(image_name,0)
    img = cv2.medianBlur(img,5)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

    # Identifies circles
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,0.4,20,minRadius = 50, maxRadius = 65)

    # Draws the circles
    circles = np.uint16(np.around(circles))
    radii = []
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
        
        # Convert pixels to microns
        # 94 pixels = 250micron
        radii.append(i[2] * pixels_to_microns)

    
    # Calculates some statistics about droplet number, size, and s.d.
    total_droplets = len(radii)
    mean_radius = round(np.mean(radii), 1)
    std_dev = round(np.std(radii), 1)


    # Draws histogram of radius sizes
    plt.hist(radii, bins=20)
    plt.title("droplets: {}, mean_radius: {}, std_dev: {}".format(total_droplets, mean_radius, std_dev))
    plt.xlabel("droplet radius (microns)")
    plt.ylabel("num droplets")
    plt.savefig(output_histogram)
    plt.close()

    # Writes image to file
    cv2.imwrite(output_image,cimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
