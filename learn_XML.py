# -*- coding: utf-8 -*-

from xml.parsers.expat import ParserCreate
from urllib import request
import ssl

class DefaultSaxEandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

# handler = DefaultSaxEandler()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(xml)

yahoo_xml = r'''This XML file does not appear to have any style information associated with it. The document tree is shown below.
<query xmlns:yahoo="http://www.yahooapis.com/v1/base.rng" yahoo:count="1" yahoo:created="2018-02-22T10:27:23Z" yahoo:lang="zh-CN">
<results>
<channel>
<yweather:units xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" distance="mi" pressure="in" speed="mph" temperature="F"/>
<title>Yahoo! Weather - Beijing, Beijing, CN</title>
<link>
http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2151330/
</link>
<description>Yahoo! Weather for Beijing, Beijing, CN</description>
<language>en-us</language>
<lastBuildDate>Thu, 22 Feb 2018 06:27 PM CST</lastBuildDate>
<ttl>60</ttl>
<yweather:location xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" city="Beijing" country="China" region=" Beijing"/>
<yweather:wind xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" chill="48" direction="335" speed="4"/>
<yweather:atmosphere xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" humidity="12" pressure="1009.0" rising="0" visibility="16.1"/>
<yweather:astronomy xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" sunrise="6:58 am" sunset="5:59 pm"/>
<image>
<title>Yahoo! Weather</title>
<width>142</width>
<height>18</height>
<link>http://weather.yahoo.com</link>
<url>
http://l.yimg.com/a/i/brand/purplelogo//uh/us/news-wea.gif
</url>
</image>
<item>
<title>
Conditions for Beijing, Beijing, CN at 05:00 PM CST
</title>
<geo:lat xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">39.90601</geo:lat>
<geo:long xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">116.387909</geo:long>
<link>
http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2151330/
</link>
<pubDate>Thu, 22 Feb 2018 05:00 PM CST</pubDate>
<yweather:condition xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="30" date="Thu, 22 Feb 2018 05:00 PM CST" temp="49" text="Partly Cloudy"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="34" date="22 Feb 2018" day="Thu" high="51" low="20" text="Mostly Sunny"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="30" date="23 Feb 2018" day="Fri" high="49" low="22" text="Partly Cloudy"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="30" date="24 Feb 2018" day="Sat" high="37" low="27" text="Partly Cloudy"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="34" date="25 Feb 2018" day="Sun" high="43" low="21" text="Mostly Sunny"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="34" date="26 Feb 2018" day="Mon" high="50" low="26" text="Mostly Sunny"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="30" date="27 Feb 2018" day="Tue" high="50" low="30" text="Partly Cloudy"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="34" date="28 Feb 2018" day="Wed" high="45" low="28" text="Mostly Sunny"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="30" date="01 Mar 2018" day="Thu" high="40" low="27" text="Partly Cloudy"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="30" date="02 Mar 2018" day="Fri" high="41" low="24" text="Partly Cloudy"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="30" date="03 Mar 2018" day="Sat" high="42" low="26" text="Partly Cloudy"/>
<description>
<![CDATA[<img src="http://l.yimg.com/a/i/us/we/52/30.gif"/> <BR /> <b>Current Conditions:</b> <BR />Partly Cloudy <BR /> <BR /> <b>Forecast:</b> <BR /> Thu - Mostly Sunny. High: 51Low: 20 <BR /> Fri - Partly Cloudy. High: 49Low: 22 <BR /> Sat - Partly Cloudy. High: 37Low: 27 <BR /> Sun - Mostly Sunny. High: 43Low: 21 <BR /> Mon - Mostly Sunny. High: 50Low: 26 <BR /> <BR /> <a href="http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2151330/">Full Forecast at Yahoo! Weather</a> <BR /> <BR /> <BR /> ]]>
</description>
<guid isPermaLink="false"/>
</item>
</channel>
</results>
</query>
<!--  total: 5  -->
'''

class WeatherSaxEandler(object):

    result = {}
    arr = []

    def start_element(self, name, attrs):
        if 'city' in attrs:
            self.result['city'] = attrs['city']
        
        if 'forecast' in name:
            d = dict()
            d['date'] = attrs['date']
            d['high'] = attrs['high']
            d['low'] = attrs['low']
            self.arr.append(d)
            self.result['forecast'] = self.arr
            

def parseXml(xml_str):
    handler = WeatherSaxEandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.Parse(xml_str)

    return handler.result

# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4, context=ssl._create_unverified_context()) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
print(result)
assert result['city'] == 'Beijing'