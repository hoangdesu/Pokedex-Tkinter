
import tkinter as tk
# from tkinter.ttk import LabelFrame
from tkinter import Label, ttk
from tkinter.constants import *
from PIL import Image, ImageTk

import requests
import io
import json


app = tk.Tk()
app.geometry("1920x1080")
app.title("Doroke's Pokedex")


applicationFrame = ttk.LabelFrame(app)
h1 = tk.Label(app, text="Generation 1 Pokémons", font=('courier', 26, 'bold'))
h1.pack()

scrollCanvas = tk.Canvas(applicationFrame, width=1410, height=800)
scrollCanvas.pack(side=LEFT)

# TIP: SCROLLBAR ONLY WORKS ON A CANVAS!!!

scrollBar = ttk.Scrollbar(applicationFrame, orient=VERTICAL, command=scrollCanvas.yview)
scrollBar.pack(side=RIGHT, fill="y")

scrollCanvas.configure(yscrollcommand=scrollBar.set)

scrollCanvas.bind('<Configure>', lambda e: scrollCanvas.configure(scrollregion=scrollCanvas.bbox('all')))

pokeFrame = tk.Frame(scrollCanvas)


scrollCanvas.create_window((0, 0), window=pokeFrame, anchor="nw")
applicationFrame.pack(fill="both", expand="yes")

# for i in range(20):
#     tk.Button(pokeFrame, text=f"Button {i}").pack()

pokemonObjects = []

for i in range(1, 5):
    # getting pokemon sprites
    response = requests.get(f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{i}.png') # give back response code. 200 means success!
    if response.status_code != 200:
        print("Download error")
    # when we send a request to an IMAGE file, we get back the BYTECODE encryption for that image
    # BYTECODE: text representation of an image
    
    
    content = response.content # returns a JSON in form of STRING
    bytecode_from_string = io.BytesIO(content) # convert string to bytecode so the computer can understand
    image_from_bytecode = Image.open(bytecode_from_string).resize((150, 150)) # make an image from bytecode
    image = ImageTk.PhotoImage(image_from_bytecode)   # make TK's image object to display
    # imagesObj.append(image)
    
    # label = tk.Label(root, image=image)
    # label.grid(column=1, row=1)
    
    # getting pokemon name
    pokeResponse = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}')
    name = pokeResponse.json()['forms'][0]['name'].title()
    
    pokemonObjects.append(
        {
        'id': i,
        'name': name,
        'sprite': image
        }
    )
  
    print(f'Downloaded pokemon {i}')


rowCounter = 0
colCounter = 0

def motion(event):
    print("Mouse position: (%s %s)" % (event.x, event.y))
    return

def getPokemonName(i):
    print('Pokemon clicked:', i)
    smallApp = tk.Tk()
    tk.Label(smallApp, "New window opened").pack()
    return

for i in range(len(pokemonObjects)): # i = 0 -> 30
    # imgFrame = tk.Frame(pokeFrame)

    canvas = tk.Canvas(pokeFrame, width=150, height=150, bg="pink")
    canvas.create_image(0, 0, anchor=NW, image=pokemonObjects[i]['sprite']) 
    # tk.Label(pokeFrame, text=pokemonObjects[i]['name']).grid(row=rowCounter, column=colCounter)
    canvas.grid(row=rowCounter, column=colCounter)
    
    # binding actions
    canvas.bind('<Enter>', motion)
    canvas.bind('<Button-1>', getPokemonName)
    # lambda event: getPokemonName(event)


    
    # pokeFrame.grid(row=rowCounter, column=colCounter)
    colCounter += 1
    if colCounter > 8:
        rowCounter += 1
        colCounter = 0
        




# def frame(event):
#     print("FRAME ENTER position: (%s %s)" % (event.x, event.y))
#     return
# pokeFrame.bind('<Enter>', frame)


# event: action produced when some other actions are performed

# - event: when the X icon is CLICKED
# - action: close the file being opened



app.mainloop()