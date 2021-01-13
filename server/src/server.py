from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import render_to_response
from pyramid.response import Response

from camera import VideoCamera
from dronecamera import DroneCamera

def index(req):
  return render_to_response('index.html', [], request=req)

def get_frame(cam):
  while True:
    yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + cam.get_frame() + b'\r\n\r\n')

def video_stream(req):
  # return Response(app_iter=get_frame(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')
  return Response(app_iter=get_frame(DroneCamera()), content_type='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
  with Configurator() as config:
    config.include('pyramid_jinja2')
    config.add_jinja2_renderer('.html')

    config.add_route('index', '/')
    config.add_view(index, route_name='index')

    config.add_route('camera', '/camera')
    config.add_view(video_stream, route_name='camera')

    app = config.make_wsgi_app()

  server = make_server('0.0.0.0', 6543, app)
  print('Web server started on: http://0.0.0.0:6543')
  server.serve_forever()