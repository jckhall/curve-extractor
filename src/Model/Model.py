"""logic handler for the tool"""

import sys
import pydicom
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
#import PIL
#import gdcm
import csv

us_designation = (0x0008, 0x0016)
regions = (0x0018, 0x6011)
region_type = (0x0018, 0x6014)
spectral_doppler_id = 4
y_region_min = (0x0018, 0x601a)
y_region_max = (0x0018, 0x601e)
y_reference_pixel = (0x0018, 0x6022) # x axis location
x_reference_pixel = (0x0018, 0x6020)
physical_y_conversion = (0x0018, 0x602E)
physical_x_conversion = (0x0018, 0x602C)
value_at_ref_x = (0x0018, 0x6028)
value_at_ref_y = (0x0018, 0x60AC)

class Model():
    def __init__(self):
        self.dicom = object
        self.directory = ""
        self.roi_pix_array = np.array([0])
        self.max_pix = 0
        self.min_pix = 0
        self.defaultThresh = 0
        self.greyscale_image = object
        self.threshold_image = object
        self.pil_threshold_image = object
        self.image_width = 0
        self.graph = []
        self.axis_row = 0
        self.roi = -1
        self.final_image = object
        self.red_graph = 0
        self.green_graph = 0
        self.x_max = 0
        self.x_min = 0
        ## if adding to attributes, add to self.reset() function as well



    def loadDicom(self):
        dicom = pydicom.dcmread(self.directory)
        self.dicom = dicom
        #print(self.dicom)
        if (dicom[us_designation].value != "1.2.840.10008.5.1.4.1.1.6.1"):
            print("US designation failed")
            return -1
        self.roi = -1
        count = 0
        for i in dicom[regions]:
            if int(i[region_type].value) == 4 or int(i[region_type].value) == 3:
                self.roi = count
                break
            count += 1
        if self.roi == -1:
            print("no roi failed")
            return -1

        roi_data = dicom[regions][self.roi]
        y_min = int(roi_data[y_region_min].value)
        y_max = int(roi_data[y_region_max].value)
        mod_image = dicom.pixel_array[y_min:y_max,:,:]
        grey = Image.fromarray(mod_image).convert('L')
        self.greyscale_image = grey
        pixel_list = grey.getdata()
        self.max_pix = max(pixel_list)
        self.min_pix = min(pixel_list)
        del pixel_list
        self.defaultThresh = (self.max_pix + self.min_pix)/2
        grey_thresh = grey.point(lambda p: 255 if p > self.defaultThresh else 0)
        grey_thresh = grey_thresh.convert('1')
        self.pil_threshold_image = grey_thresh
        #plt.imshow(grey_thresh)
        #plt.show()
        self.threshold_image = np.array(grey_thresh)
        self.image_width = self.threshold_image.shape[1]
        self.axis_row = int(roi_data[y_reference_pixel].value)
        self.image_add_lines(0, self.image_width)
        self.update_graph()

    def update_image_thresh(self, threshold):
        grey_thresh = self.greyscale_image.point(lambda p: 255 if p > threshold else 0)
        grey_thresh = grey_thresh.convert('1')
        self.threshold_image = np.array(grey_thresh)
        self.pil_threshold_image = grey_thresh


    def update_graph(self):
        self.graph = []
        roi = self.threshold_image#[:, 0:900]
        roi = roi[0:int((roi.shape[0])*0.96)] ## remove interval markers
        pointCloudArr = []
        count = 0
        for column in roi.T:
            try:
                yval = np.where(column == True)[0].max()
            except:
                yval = 0
            yval = int(yval - self.axis_row)
            pointCloudArr.append((count, yval))
            count += 1
        realValueArr = []
        for i in pointCloudArr:
            x = i[0]
            y = i[1]
            x_conversion = float(self.dicom[regions][self.roi][physical_x_conversion].value)
            y_conversion = float(self.dicom[regions][self.roi][physical_y_conversion].value)
            try:
                x_ref = float(self.dicom[regions][self.roi][value_at_ref_x].value)
                y_ref = float(self.dicom[regions][self.roi][value_at_ref_y].value)
            except:
                x_ref = 0
                y_ref = 0
            x = (x * x_conversion) + x_ref
            y = (y * y_conversion) + y_ref
            realValueArr.append([x,y])

        #print("funct attr" + realValueArr)

        self.graph = realValueArr

    def reset(self):
        self.dicom = object
        self.directory = ""
        self.roi_pix_array = np.array([0])
        self.max_pix = 0
        self.min_pix = 0
        self.defaultThresh = 0
        self.greyscale_image = object
        self.threshold_image = object
        self.pil_threshold_image = object
        self.image_width = 0
        self.graph = []
        self.axis_row = 0
        self.roi = -1
        self.final_image = object
        self.red_graph = 0
        self.green_graph = 0
        self.x_max = 0
        self.x_min = 0

    def image_add_lines(self, red_line, green_line):
        self.final_image = self.pil_threshold_image.convert("RGB")
        draw = ImageDraw.Draw(self.final_image)
        draw.line([(red_line, 0),(red_line, self.final_image.size[1])], fill = (255, 0, 0), width = 2)
        draw.line([(green_line-2, 0),(green_line-2, self.final_image.size[1])], fill = (0, 255, 0), width = 2)

        x_conversion = float(self.dicom[regions][self.roi][physical_x_conversion].value)
        try:
            x_ref = float(self.dicom[regions][self.roi][value_at_ref_x].value)
        except:
            x_ref = 0

        x_red = ((red_line * x_conversion) + x_ref)# * 100
        x_green = ((green_line * x_conversion) + x_ref)# * 100


        self.red_graph = x_red
        self.green_graph = x_green

    def export(self, file_path, point1, point2):
        lower_point = min([point1, point2])
        higher_point = max([point1, point2])

        x_conversion = float(self.dicom[regions][self.roi][physical_x_conversion].value)
        try:
            x_ref = float(self.dicom[regions][self.roi][value_at_ref_x].value)
        except:
            x_ref = 0

        lower_conv = (lower_point * x_conversion) + x_ref
        higher_conv = (higher_point * x_conversion) + x_ref

        outputs = []
        for i in self.graph:
            if(i[0] <= higher_conv and i[0] >= lower_conv):
                outputs.append(i)
        file = open(file_path[0], 'w+', newline ='')
        with file:
            write = csv.writer(file)
            write.writerows(outputs)

