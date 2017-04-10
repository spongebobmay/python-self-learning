from xml.parsers.expat import ParserCreate
class WeatherSaxHandler(object):
    def __init__(self):  
        self.weather_data = {}
        self.date_index = 0
    def start_element(self, name, attrs):
        if name=="yweather:location":
            self.weather_data['city'] = attrs['city']
            self.weather_data['country'] = attrs['country']
        if name=="yweather:forecast" and self.date_index<5:
            if  self.date_index==0:
                self.weather_data['today'] = {}
                self.weather_data['today']['text'] = attrs['text']
                self.weather_data['today']['low'] = int(attrs['low'])
                self.weather_data['today']['high'] = int(attrs['high'])
                self.date_index += 1
            elif self.date_index==1:
                self.weather_data['the-second-day'] = {}
                self.weather_data['the-second-day']['text'] = attrs['text']
                self.weather_data['the-second-day']['low'] = int(attrs['low'])
                self.weather_data['the-second-day']['high'] = int(attrs['high'])
                self.date_index += 1
            elif self.date_index==2:
                self.weather_data['the-third-day'] = {}
                self.weather_data['the-third-day']['text'] = attrs['text']
                self.weather_data['the-third-day']['low'] = int(attrs['low'])
                self.weather_data['the-third-day']['high'] = int(attrs['high'])
                self.date_index += 1
            elif self.date_index==3:
                self.weather_data['the-fourth-day'] = {}
                self.weather_data['the-fourth-day']['text'] = attrs['text']
                self.weather_data['the-fourth-day']['low'] = int(attrs['low'])
                self.weather_data['the-fourth-day']['high'] = int(attrs['high'])
                self.date_index += 1
            elif self.date_index==4:
                self.weather_data['the-fifth-day'] = {}
                self.weather_data['the-fifth-day']['text'] = attrs['text']
                self.weather_data['the-fifth-day']['low'] = int(attrs['low'])
                self.weather_data['the-fifth-day']['high'] = int(attrs['high'])
                self.date_index += 1
    def end_element(self, name):
        pass

    def char_data(self, text):
        pass

def parse_weather(xml):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)
    return handler.weather_data

data= r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <channel>
        <title>Yahoo! Weather - Beijing, CN</title>
        <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
        <yweather:location city="Beijing" region="" country="China"/>
        <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
        <yweather:wind chill="28" direction="180" speed="14.48" />
        <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
        <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
        <item>
            <geo:lat>39.91</geo:lat>
            <geo:long>116.39</geo:long>
            <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
            <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
            <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
            <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
            <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
            <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
        </item>
    </channel>
</rss>
'''
weather = parse_weather(data)
print('Weather:', str(weather))
