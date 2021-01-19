from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import render_to_response
from pyramid.response import Response

from easytello import tello

drone = tello.Tello()
drone.streamon()

def index(req):
  return render_to_response('index.html', [], request=req)

def video_stream(req):
  while (True):
      return Response(app_iter=drone._video_thread(), content_type='multipart/x-mixed-replace; boundary=frame')

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
