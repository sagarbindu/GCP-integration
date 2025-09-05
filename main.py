#!/usr/bin/env python
import webapp2
class MainHandler(webapp2.RequestHandler):
def get(self):
self.response.write('Hello, World!')
app = webapp2.WSGIApplication([ ('/', MainHandler) ], debug=True)
runtime: python27
api_version: 1
threadsafe: yes
handlers:
- url: .*
script: main.app
libraries:
- name: webapp2
version: "2.5.2"

