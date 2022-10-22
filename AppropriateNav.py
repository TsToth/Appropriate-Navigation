import urllib.parse
import requests
import PySimpleGUI as sg
import cloudscraper
import io
import os
from PIL import Image

#you may need to run the command "python3 -m pip install PySimpleGUI", "python3 -m pip install cloudscraper" and "python3 -m pip install image" to run this code





""" how to Create GUI's
1. copy this template and add/remove as needed
def guiname():
    layout = [  [sg.Text('this line will allow users to input values'), sg.InputText()],
                [sg.Text('some text')],
                [sg.Text('some text')],
                [sg.Button('button name'), sg.Button('button name')]]
    return sg.Window('name your window', layout)

2. create your window using the following code

window = guiname()

this will open the window you created in the def block
the whole layout is modular you can add some of the text lines or make more button lines, if you get stuck feel free to ask for help or google it.
other useful code:

window.close()                 <- this closes the current window
event, values = window.read()  <- allows your buttons to work as well as store input from users
varName = values[0]            <- this will store the user's input from the first sg.InputText() box incriment the 0 for more than one box eg(values[1] will be used for the second sg.InputText() box)
if event == 'button name':     <- this lets the program respond to button press
sg.theme('DarkBrown4')         <- changes the color of the GUI

sg.theme_previewer()           <-throw this code into the program to get a window displaying all the themes
"""


sg.theme('Dark2')
#home GUI
def Home():
    layout = [  [sg.Text('         Welcome to Appropriate navigation')],
                [sg.Text('               What would you like to do?')],
                [sg.Text("", key='-CONDITION-')],
                [sg.Text("")],
                [sg.Text('')],
                [sg.Button('Navigate'), sg.Text("           "), sg.Button('Map'), sg.Text("            "), sg.Button('Close')]]
    return sg.Window('Appropriate Navigation', layout)

#Navigation GUI
def nav():
    layout = [  [sg.Text('                                   Welcome to navigation')],
            [sg.Text("", key='-TEXT-')],  
            [sg.Text("")],
            [sg.Text('Where are you coming from?'), sg.InputText()],
            [sg.Text('Where are you going?          '), sg.InputText()],
            [sg.Button('Route'), sg.Text("    "), sg.Button('Back')]]
    return sg.Window('Appropriate Navigation', layout)

def map():
    layout = [[ sg.Column(imgViewer)],
              [sg.Button('Close')]] 
    return sg.Window('Appropriate Navigation', layout)


mapcondition = False
window = Home()
#main GUI program
while True:
    #creates GUI
    
    #detects user interaction
    event, values = window.read()
    
    #closes program
    if event == 'Close' or event == sg.WIN_CLOSED:
        break
    #begins navigation page
    if event == "Navigate":
        window.close()
        window = nav()
        true = True
        while true == True:
            
            event, values = window.read()
            #closes window
            if event == 'Back' or event == sg.WIN_CLOSED:
                window.close()
                window = Home()
                true = False
            #does Mapquest_parse-json_7's fuction
            if event == 'Route':
                route = True
                start = values[0]
                dest = values[1]
                main_api = "https://www.mapquestapi.com/directions/v2/route?"
                key = "efB9HJE5qFfoI6xGr5xqkDmnDAb0oCOe"
                
                while route == True:
                    url = main_api + urllib.parse.urlencode({"key":key, "from":start, "to":dest})
                    window['-TEXT-'].update("Route Saved. You may now view the map")
                    mapcondition = True
                    
                    json_data = requests.get(url).json()
                    map_api = "https://www.mapquestapi.com/staticmap/v5/map?"
                    size = "@2x" #map size
                    Type = "map" #this will determine the type of map displayed; map, hyb, sat, light, darkwhile True:
                    size = "@2x"
                    Type = "map"
                    traffic = "flow|con|inc"
                    map_url = map_api + urllib.parse.urlencode({"key":key, "start":start, "end":dest, "size":size, "type":Type, "traffic":traffic})
                    #ends loop
                    route = False
    if event == 'Map':
        if mapcondition == False:
        
            window['-CONDITION-'].update("No map data stored, please use 'Navigate' first.")
            
        else:
            
            window.close()
            jpg_data = (
                cloudscraper.create_scraper(browser={"browser": "firefox", "platform": "windows", "mobile": False}).get(map_url).content)

            pil_image = Image.open(io.BytesIO(jpg_data))
            png_bio = io.BytesIO()
            pil_image.save(png_bio, format="PNG")
            png_data = png_bio.getvalue()

            imgViewer = [
                [sg.Image(data=png_data)]]
            true = True
            window = map()
            while true == True:
                event, values = window.read()
            
                if event == 'Close'or event == sg.WIN_CLOSED:
                    window.close()
                    window = Home()
                    true = False
            
        
#ive made it up to the point of implimenting the original program, none of the data is parsed but the URL integer works like normal so programming should work as if you were in the original file.            
                    
#url = "https://upload.wikimedia.org/wikipedia/commons/d/d9/Test.png"
#response = requests.get(url, stream=True)
#response.raw.decode_content = True
# img = ImageQt.Image.open(response.raw)
# data = image_to_data(img)
#img_box = sg.Image(data=response.raw.read())    
      






#this is just the main block from the original lab, i've implimented it into my UI but leave it here for reference
#main_api = "https://www.mapquestapi.com/directions/v2/route?"
#key = "efB9HJE5qFfoI6xGr5xqkDmnDAb0oCOe"
#main loop
#while True:
#    url = main_api + urllib.parse.urlencode({"key":key, "from":start, "to":dest})
#
    #retrieve url
#    json_data = requests.get(url).json()
    
    #print url and info sorting
#    print("URL: " + (url))