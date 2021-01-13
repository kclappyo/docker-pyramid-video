# import the necessary packages
import cv2
from djitellopy import Tello
import time

class DroneCamera():
  def __init__(self):
    self.drone = Tello()                       # Instantiate a Tello Object
    self.drone.connect()                       # Connect to the drone
    self.drone.streamoff()                     # In case stream never exited before
    self.drone.streamon()                      # Turn on drone camera stream
    time.sleep(5)                              # Give the stream time to start up

  def __del__(self):
    self.drone.streamoff()

  def get_frame(self):
    # Grab a frame and resize it
    frame_read = self.drone.get_frame_read()
    if frame_read.stopped:
      return None
    frame = cv2.resize(frame_read.frame, (360, 240))

    # encode OpenCV raw frame to jpeg
    ret, jpeg = cv2.imencode('.jpg', frame)
    return jpeg.tobytes()