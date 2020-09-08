from ij import IJ, WindowManager, ImagePlus, Macro
from ij.plugin.filter import ParticleAnalyzer 
from ij.plugin import Duplicator
from ij.gui import Roi, PolygonRoi, GenericDialog, PointRoi
from ij.measure import Measurements, ResultsTable
from ij.plugin.frame import RoiManager
from ij.process import ImageStatistics as IS, ImageProcessor, ImageConverter
from ijopencv.ij import ImagePlusMatConverter
from ijopencv.opencv import MatImagePlusConverter
from net.imglib2.img.display.imagej import ImageJFunctions
from java.lang import Double
from java.io import File
import os

imgdir = "/Users/nrnatesh/shenlab/Droplet-organoid/image-scripts/input_images"
img_path = os.path.join(imgdir,"T2.tif")
imp = IJ.openImage("/Users/nrnatesh/shenlab/Droplet-organoid/image-scripts/input_images/T2.tif")
IJ.run(imp, "8-bit", "")
IJ.run(imp, "Smooth", "")
IJ.run(imp, "Find Edges", "")
IJ.run(imp, "Enhance Contrast...", "saturated=0.3 equalize")
IJ.run(imp, "Auto Threshold", "method=Default white")
IJ.run(imp, "Despeckle", "")
IJ.run(imp, "Remove Outliers...", "radius=2 threshold=50 which=Bright")
#IJ.run("Hough Circle Transform","minRadius=50, maxRadius=65, inc=5, minCircles=1, maxCircles=100, threshold=0.4, resolution=392, ratio=2.0, bandwidth=10, local_radius=10,  reduce show_mask results_table")
IJ.run(imp, "Convert to Mask", "")


imp.show();
