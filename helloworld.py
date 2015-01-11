import webapp2
import time

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')
        self.response.write('The current time and date is: ')
        self.response.write(time.ctime())

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
