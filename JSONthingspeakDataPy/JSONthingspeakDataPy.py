import urllib
import json
input=urllib.urlopen('https://thingspeak.com/channels/245802/field/1.json').read();
#we are getting the string as {"channel":{...},"feeds":[{"field1":"75"}]} but
#for simplicity or for easy parsing we need string from [] i.e after feeds, so
#we are removing unnecessary part from front and back.
pos=input.find('feeds');
#print pos
str1=input[196:len(input)-1];
#print str1

info=json.loads(str1);
print "no.of Heart rate values: ",len(info)
for item in info:
    print item['field1']


#this is with out removing unnecessary part from string, here the problem is we
#dont no how many entries are present.
#info=json.loads(input)
#for i in range(0,12):
#    print info["feeds"][i]["field1"]
