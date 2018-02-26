# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

# parser = MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')

from urllib import request
import ssl

class pythonEventsParser(HTMLParser):

    __event_title_detected = False
    __event_location_detected = False
    __event_datetime_detected = False
    
    result = []

    @property 
    def event(self):
        return self._event
    
    @event.setter
    def event(self, value):
        if 'title' in dict(value).keys():
            self._event = value
        elif 'datetime' in dict(value).keys():
            temp_d = self._event
            temp_d['datetime'] = value['datetime']
            self._event = temp_d
        elif 'location' in dict(value).keys():
            temp_d = self._event
            temp_d['location'] = value['location']
            self._event = temp_d
            self.result.append(self._event)

    def handle_starttag(self, tag, attrs):
        if attrs.__len__() == 1 and attrs[0].__len__() == 2:
            if attrs[0][0] == 'class' and attrs[0][1] == 'event-title':
                self.__event_title_detected = True
            elif attrs[0][0] == 'class' and attrs[0][1] == 'event-location':    
                self.__event_location_detected = True
            elif attrs[0][0] == 'datetime': 
                self.__event_datetime_detected = True
        # print('<%s>' % tag)

    def handle_endtag(self, tag):
        # print('</%s>' % tag)
        pass

    def handle_startendtag(self, tag, attrs):
        # print('<%s/>' % tag)
        pass

    def handle_data(self, data):
        if self.__event_title_detected:
            self.event = {'title': data}
            self.__event_title_detected = False
        elif self.__event_location_detected:
            self.event = {'location': data}
            self.__event_location_detected = False
        elif self.__event_datetime_detected:    
            self.event = {'datetime': data}
            self.__event_datetime_detected = False

    def handle_comment(self, data):
        # print('<!--', data, '-->')
        pass

    def handle_entityref(self, name):
        # print('&%s;' % name)
        pass

    def handle_charref(self, name):
        # print('&#%s;' % name)
        pass

url = 'https://www.python.org/events/python-events/'

with request.urlopen(url, timeout=4, context=ssl._create_unverified_context()) as response:
    data = response.read()

parser = pythonEventsParser()
parser.feed(data.decode('utf-8'))
print(parser.result)


