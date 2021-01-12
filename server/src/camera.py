# import the necessary packages
import cv2

class VideoCamera():
  def __init__(self):
    self.video = cv2.VideoCapture(0)

  def __del__(self):
    self.video.release()

  def get_frame(self):
    ret, frame = self.video.read()

    # # encode OpenCV raw frame to jpg and displaying it
    ret, jpeg = cv2.imencode('.jpg', frame)
    return jpeg.tobytes()

  def run(self):
    while(True):
      frame = self.get_frame()
