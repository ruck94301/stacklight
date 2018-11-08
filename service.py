import time

import cherrypy

import stacklight


lamp_index = {
    'red': 0,
    'yellow': 1,
    'green': 2,
    'blue': 3,
    'white': 4,
    }

red_off = '5700006464646464'.decode('hex')
red_on = '5700016464646464'.decode('hex')
red_flash = '5700026464646464'.decode('hex')

yellow_off = '5700640064646464'.decode('hex')
yellow_on = '5700640164646464'.decode('hex')
yellow_flash = '5700640264646464'.decode('hex')


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"


class Stacklight(object):
    @cherrypy.expose
    def index(self):
        # return "Hello World!"
        return """<html>
            <head></head>
            <body>
              <table>
              <tr>
                <td>
                  <form method="get" action="red_on">
                  <button type="submit">Red On</button>
                  </form>
                </td>
                <td>
                  <form method="get" action="red_flash">
                  <button type="submit">Red Flash</button>
                  </form>
                </td>
                <td>
                  <form method="get" action="red_off">
                  <button type="submit">Red Off</button>
                  </form>
                </td>
              </tr>
              </table>
            </body>
            </html>"""

    @cherrypy.expose
    def red_on(self):
        stacklight.send(red_on)
        # return "Hello World!"
        cherrypy.response.status = '204'

    @cherrypy.expose
    def red_off(self):
        stacklight.send(red_off)
        # return "Hello World!"
        cherrypy.response.status = '204'

    @cherrypy.expose
    def red_flash(self):
        stacklight.send(red_flash)
        # return "Hello World!"
        cherrypy.response.status = '204'

# this to serve to the publicly accessible interface(s).  The default,
# 127.0.0.1, is not publicly accessible.
cherrypy.config.update({'server.socket_host': '0.0.0.0'})

# host an instance of the application, accessible via base path
# '/stacklight', like http://172.21.80.81:8080/red_on
cherrypy.tree.mount(Stacklight(), '/stacklight')

cherrypy.quickstart(HelloWorld())
