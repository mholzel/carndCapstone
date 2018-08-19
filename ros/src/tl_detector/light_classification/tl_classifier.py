from styx_msgs.msg import TrafficLight
import rospy
import numpy
import datetime
import os
import cv2


class TLClassifier(object):
    def __init__(self):
        # TODO load classifier
        self.saving = False
        if self.saving:
            time = str(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))
            self.folder = '/home/matt/drive/images/' + time + '/'
            self.count = 0
            os.mkdir(self.folder)

    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """
        # TODO implement light color prediction
        tol = 50
        utol = 255 - tol
        b, g, r = image[:, :, 0], image[:, :, 1], image[:, :, 2]
        is_red = numpy.logical_and(r > utol, numpy.logical_and(g < tol, b < tol))
        red_pixels = numpy.sum(is_red)

        if self.saving:
            self.count += 1
            cv2.imwrite(self.folder + str(self.count) + '.png', image)
            rospy.logerr(str(red_pixels))

        if red_pixels > 30:
            return TrafficLight.RED
        else:
            return TrafficLight.UNKNOWN
