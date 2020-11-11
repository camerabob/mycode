#!/usr/bin/env python3
import requests
from pprint import pprint as pp # part of the standard libray
# import webbrowser

## define some constants
NASAAPI = 'https://api.nasa.gov/planetary/apod' # this is our API to call
MYKEY = '?api_key=DEMO_KEY'

testkey = input('Would you like use your own API key? (If so, input here) ')
if len(testkey) >= 0:
    MYKEY = "?api_key=" + testkey

testdate = input('Would you like to change the date? Enter in formate yyyy-mm-dd) ')
if len(testdate) >= 0:
    DATE = "&date=" + testdate

testreso= input('Would you like to get a high resolution image? (yes or no please) ')
HD = ''
if testreso == "YES":
    HD = "&hd=true"

## pretty print json
def main():
    """run-time code"""
    nasaapiobj = requests.get(NASAAPI + MYKEY + DATE + HD) # call the webservice
    nasaread = nasaapiobj.json() # parse the JSON blob returned

    # Show converted json
    print(nasaread) # show converted JSON without pprint
    input('\nThis is converted json. Press ENTER to continue.') # pause for enter

    # Show Pretty Print json
    pp(nasaread) # this is pretty print in action
    # pprint.pprint(convertedjson) # if you do a simple import pprint, the result is a long usage
    input('\nThis is pretty printed JSON. Press ENTER to continue.') # pause for ENTER

    # Print the description of the photo we are about to view
    print(nasaread['explanation']) # display the value for the key explanation
    print("Link to the APOD:", nasaread.get('hdurl',"No HD URL for today!"))


    #input('\nPress ENTER to view this photo of the day') # pause for ENTER
    # webbrowser.open(nasaread['hdurl']) # open in the webbrowser

main()

