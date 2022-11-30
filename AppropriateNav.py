import io
import urllib.parse
import webbrowser

import cloudscraper
import PySimpleGUI as sg
import requests
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

#Keys
MQkey = "efB9HJE5qFfoI6xGr5xqkDmnDAb0oCOe"
GOVkey = "bBOUe9tgtqpB8GKogYA1xhpjlb6G37UgAF6DNNsG"

#Custom GUI theme
sg.LOOK_AND_FEEL_TABLE['Custom'] = {'BACKGROUND': '#949494',
                                        'TEXT': '#000000',
                                        'INPUT': '#F6F6F6',
                                        'TEXT_INPUT': '#000000',
                                        'SCROLL': '#99CC99',
                                        'BUTTON': ('#000000', '#0687F6'),
                                        'PROGRESS': ('#D1826B', '#CC8019'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0, 
'PROGRESS_DEPTH': 0, }
sg.theme('Custom')

#settings GUI
def settings():
    layout = [[sg.Text("Settings")],
              [sg.Text("")],
              [sg.Text("Menu Themes:")],
              [sg.Button("Default"), sg.Button("Black"), sg.Button("White"), sg.Button("Mage"), sg.Button("Pastel")],
              [sg.Text("")],
              [sg.Button("Back")]
        
        
        
        
    ]
    return sg.Window('Appropriate Navigation', layout)
#Home GUI
def Home():
    layout = [  [sg.Text('                      Welcome to Appropriate navigation')],
                [sg.Text('                            What would you like to do?')],
                [sg.Text("", key='-CONDITION-')],
                [sg.Text("")],
                [sg.Text('                                '), sg.Button('How To Use', key='-tutorial-')],
                [sg.Text('')],
                [sg.Button('Navigate'), sg.Text("        "), sg.Button('Map'), sg.Text("         "), sg.Button('Settings'), sg.Text("        "), sg.Button('Close')]]
    return sg.Window('Appropriate Navigation', layout)

#Help page GUI
def Tutorial():
    layout = [  [sg.Text('Welcome to Appropriate navigation Tutorial\n')],
                [sg.Text("1. press the 'Navigate' button")],
                [sg.Text("2. Enter your starting location and where you're going.")],
                [sg.Text("3. Press the 'Route' button to save that data")],
                [sg.Text("(Optional) Copy the information that appears in 'URL' \nand enter it into a browser to view the route data")],
                [sg.Text("4. Go back to the main menu by pressing 'Back'")],
                [sg.Text("5. Press 'Map' to view the overview of your Route")],
                [sg.Button('Back')]]
    return sg.Window('Appropriate Navigation', layout)

#Navigation GUI
def nav():
    layout = [  [sg.Text('                                                           Navigation')],
            [sg.Text("", key='-TEXT-')],  
            [sg.Text("")],
            [sg.Text('Where are you coming from?'), sg.InputText()],
            [sg.Text('Where are you going?          '), sg.InputText()],
            [sg.Text('URL:                                  '), sg.InputText(key='-url-')],            
            [sg.Button('Route'), sg.Text("    "), sg.Button('Back'), sg.Text("                                                                    "), sg.Button('Car Settings', key='-CAR-')]]
    return sg.Window('Appropriate Navigation', layout)

#static map GUI
def map():
    layout = [[ sg.Column(imgViewer)],
              [sg.Button('Close')]] 
    return sg.Window('Appropriate Navigation', layout)

#Car Settings GUI
def car():
    layout = [  [sg.Text('         Car Settings')],
                [sg.Text('Fuel Type:')],
                #add all fuel types
                [sg.Button("test"), sg.Button("test"), sg.Button("test")],
                [sg.Text("Charger Type:")],
                #add all charger types
                [sg.Button('Test')],
                [sg.Text('')],
                [sg.Button('Back') ]]
    return sg.Window('Appropriate Navigation', layout)


trigger = False
#used to ensure map data exists
mapcondition = False
#creates GUI
window = Home()
#main GUI program
while True:
    
    
    #detects user interaction
    event, values = window.read()
    
    if event == "Settings":
        window.close()
        window = settings()
        true = True
        while true == True:
            event, values = window.read()
            
            if event == 'Back':
                window.close()
                window = Home()
                true = False
            if event == sg.WIN_CLOSED:
                break
            if event == "Black":
                sg.theme('Black')
                window.close()
                window = settings()
            if event == "Default":
                sg.theme('Custom')
                window.close()
                window = settings()
            if event == "White":
                sg.theme('Default1')
                window.close()
                window = settings()
            if event == "Mage":
                sg.theme('DarkPurple4')
                window.close()
                window = settings()
            if event == "Pastel":
                sg.theme('LightGreen4')
                window.close()
                window = settings()
                
    #closes program
    if event == 'Close' or event == sg.WIN_CLOSED:
        break
    #opens tutorial
    if event == '-tutorial-':
        window.close()
        window = Tutorial()
        true = True
        while true == True:
            event, values = window.read()
            if event == 'Back':
                window.close()
                window = Home()
                true = False
            if event == sg.WIN_CLOSED:
                trigger = True
                window.close()
                window = Home()
                true = False
            
    #begins navigation page
    if event == "Navigate":
        window.close()
        window = nav()
        true = True
        while true == True:

            event, values = window.read()
            
            if event == '-CAR-':
                window.close()
                window = car()
                carloop = True
                while carloop == True:
                    event, values = window.read()
                    #for each button you will need an if statement like so:
                    #if event == "fuel type":
                    #   fuel_type = type
                    #if event == "charg type"
                    #   charg_type = type
                    
                    if event == 'back':
                        window.close()
                        window = nav()
                    if event == sg.WIN_CLOSED:
                        break
                    
                    carloop = False
                    
                
            #closes window
            if event == 'Back':
                window.close()
                window = Home()
                true = False
            if event == sg.WIN_CLOSED:
                break
            #does Mapquest_parse-json_7's fuction
            if event == 'Route':
                route = True
                start = values[0]
                dest = values[1]
                main_api = "https://www.mapquestapi.com/directions/v2/route?"
                
                
                while route == True:
                    url = main_api + urllib.parse.urlencode({"key":MQkey, "from":start, "to":dest})
                    
                    json_data = requests.get(url).json()
                    json_status = json_data["info"]["statuscode"]
                    map_api = "https://www.mapquestapi.com/staticmap/v5/map?"
                    size = "@2x"
                    Type = "map"
                    traffic = "flow|con|inc"
                    map_url = map_api + urllib.parse.urlencode({"key":MQkey, "start":start, "end":dest, "size":size, "type":Type, "traffic":traffic})
                    #ends loop
                    if json_status == 0:
                        window['-TEXT-'].update("Route Saved. You may now view the map")
                        window['-url-'].update(url)
                        mapcondition = True
                    elif json_status == 402 or json_status == 611:
                        window['-TEXT-'].update("There was an error with one or more of your locations and the route could not be established\nPlease check them and try again")
                        mapcondition = False
                    else:
                        window['-TEXT-'].update("You dun broke it, I dont even know what you did but it dont work no more.\nPlease check your entries, internet and possibly physical well being and try again.")
                        mapcondition = False
                    
                    
                    route = False
    if event == 'Map':
        if mapcondition == False:
            #checks if a map exists or possibly exists
            window['-CONDITION-'].update("No map data stored, please use 'Navigate' first.")
            
        else:
            #scrapes map_url from the internet and displays the image as a PNG inside of the GUI
            window.close()
            if trigger == True:
                map_url = "https://i.kym-cdn.com/editorials/icons/original/000/004/374/9e5.jpeg"
            jpg_data = (
                cloudscraper.create_scraper(browser={"browser": "firefox", "platform": "windows", "mobile": False}).get(map_url).content)
            #takes the scrape and converts it into a png with the nessicary data for displaying
            pil_image = Image.open(io.BytesIO(jpg_data))
            png_bio = io.BytesIO()
            pil_image.save(png_bio, format="PNG")
            png_data = png_bio.getvalue()
            #takes the PNG data conversion above and converts it into a layout for pysimplegui
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
                    trigger = False






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