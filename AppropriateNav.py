import urllib.parse
import webbrowser

import PySimpleGUI as sg
import requests

#you may need to run the command "python3 -m pip install PySimpleGUI" 


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
              [sg.Text("Map Type:")],
              [sg.Button("Fast Map", key='-fast-'), sg.Button("Detailed Map", key='-detail-')],
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
                [sg.Text("Note: Going more that 50 miles with the 'detailed map' \n                   and 'elec' car setting doesnt work")],
                [sg.Text('                                '), sg.Button('How To Use', key='-tutorial-')],
                [sg.Text('')],
                [sg.Button('Navigate'), sg.Text("        "), sg.Button('Map'), sg.Text("         "), sg.Button('Settings'), sg.Text("        "), sg.Button('Close')]]
    return sg.Window('Appropriate Navigation', layout)

#Help page GUI
def Tutorial():
    layout = [  [sg.Text('Welcome to Appropriate navigation Tutorial\n')],
                [sg.Text("(optional) go to settings and select your map type")],
                [sg.Text("1. press the 'Navigate' button")],
                [sg.Text("2. Enter your starting location and where you're going.")],
                [sg.Text("2.5. If you are using the default map\n go to the car settings and select your fuel type\n if you use normal gas, select BD as it wont affect your trip.\n if you're using the 'Fast Map' you dont need this step")],
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

#Car Settings GUI
def car():
    layout = [  [sg.Text('         Car Settings')],
                [sg.Text('Fuel Type:')],
                [sg.Button("BD"),sg.Button("CNG"),sg.Button("ELEC"),sg.Button("E85"),sg.Button("HY"),sg.Button("LNG"),sg.Button("LPG")],
                [sg.Text('')],
                [sg.Button('Back', key='-back-')]]
    return sg.Window('Appropriate Navigation', layout)


trigger = False
fastmap = False
fuel_type = 'none'
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
            if event == '-fast-':
                fastmap = True
            if event == '-detail-':
                fastmap = False
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
                    if event == 'BD':
                        fuel_type = 'BD'
                    if event == 'CNG':
                        fuel_type = 'CNG'
                    if event == 'ELEC':
                        fuel_type = 'ELEC'
                    if event == 'E85':
                        fuel_type = 'E85'
                    if event == 'HY':
                        fuel_type = 'HY'
                    if event == 'LNG':
                        fuel_type = 'LNG'
                    if event == 'LPG':
                        fuel_type = 'LPG'           
                    if event == '-back-' or event == sg.WIN_CLOSED:
                        window.close()
                        window = nav()
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
                
                if fastmap == False:
                    map_api = "https://afdc.energy.gov/stations/#/find/route?"
                    evkey = "b8OUe9tgtqpB8GKogYA1xhpjlb6G37UgAF6DNNsG"
                    
                    map_url = map_api + urllib.parse.urlencode({"api_key":evkey, "fuel":fuel_type, "start":start, "end":dest, "distance":2})
                    window['-url-'].update(map_url)
                    mapcondition = True
                    
                elif fastmap == True:
                    while route == True:
                        main_api = "https://www.mapquestapi.com/directions/v2/route?"
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
                else:
                    break
    if event == 'Map':
        if mapcondition == False:
            #checks if a map exists or possibly exists
            window['-CONDITION-'].update("No map data stored, please use 'Navigate' first.")
            
        else:
            #scrapes map_url from the internet and displays the image as a PNG inside of the GUI
            if trigger == True:
                map_url = "https://www.imdb.com/title/tt5108870/?ref_=ttls_li_tt"
            get_url = webbrowser.open(map_url)
