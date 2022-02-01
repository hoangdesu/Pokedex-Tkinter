import tkinter as tk
# from tkinter.ttk import LabelFrame
from tkinter import Label, Tk, ttk
from tkinter.constants import *
from PIL import Image, ImageTk
import io
import json
import sys

class Info:
    activeFrame = "main"

def main():

    app = tk.Tk()
    app.geometry("1920x1080")
    app.title("Doroke's Pokedex")
    
    

    info = Info()

    def h1ClickHandler(event):
        print('Clicked on H1!!')
        for evt in (list(event)):
            print(evt)
            
    def onH1HoverHandler(event):
        h1.config(fg="yellow")
        
    def onH1LeaveHandler(evt):
        h1.config(fg="navy")

    textFrame = tk.Frame(app, width=1920)
    textFrame.pack(fill='x')

    h1 = tk.Label(textFrame, text="Generation 1 Pokémons", font=('iCielSoupofJustice', 28, 'bold'), fg="navy")
    h1.bind('<Button-1>', h1ClickHandler)
    h1.bind('<Enter>', onH1HoverHandler)
    h1.bind('<Leave>', onH1LeaveHandler)
    h1.pack()

    pokeNameLabel = tk.Label(textFrame, text="Welcome!", fg="red", font=('iCielSoupofJustice', 20, 'italic'))
    # pokeNameLabel.pack(side=LEFT, padx=30)
    pokeNameLabel.pack()
  
    
    # tk.Button(textFrame, text="Change frame", command=lambda: switchFrame()).pack()
    
    applicationFrame = ttk.LabelFrame(app)
    
    
    # --- DETAILS FRAME ---
    detailsFrame = tk.Frame(app)
    # tk.Button(detailsFrame, text="Back to main", command=lambda event: switchFrame(event)).pack()
    btnBack = tk.Button(detailsFrame, text="🔙  Pokedex")
    btnBack.bind('<Button-1>', lambda evt: switchFrame(evt))
    # tk.Label(detailsFrame, text="POKEMON NAME PLACEHOLDER!", fg="green", font=('iCielSoupofJustice', 20, 'italic')).pack()
    # detailedImage = ImageTk.PhotoImage(Image.open('./sprites/25.png'))
    
    # imgCanvas = tk.Canvas(detailsFrame, width=350, height=350, bg="pink", cursor="heart")
    # imgCanvas.create_image(0, 0, anchor=NW, image=detailedImage) 
    # imgCanvas.pack()
    detailsFrame_h2_id = tk.Label(detailsFrame, text="ID", font=('iCielSoupofJustice', 25, 'bold'))
    detailsFrame_h2_name = tk.Label(detailsFrame, text="NAME", font=('iCielSoupofJustice', 25, 'bold'))
    detailsFrame_h2_sprite = tk.Label(detailsFrame, image="")
    detailsFrame_h2_height = tk.Label(detailsFrame, text="height", font=('iCielSoupofJustice', 20, 'bold'))
    detailsFrame_h2_weight = tk.Label(detailsFrame, text="weight", font=('iCielSoupofJustice', 20, 'bold'))
    detailsFrame_h2_types = tk.Label(detailsFrame, text="types", font=('iCielSoupofJustice', 20, 'bold'))
    detailsFrame_h2_description = tk.Label(detailsFrame, text="description", font=('iCielSoupofJustice', 17, 'bold'))
    detailsFrame_h2_evolution = tk.Label(detailsFrame, text="evolution", font=('iCielSoupofJustice', 20, 'bold'))
    
    # packing
    detailsFrame_h2_sprite.pack()
    detailsFrame_h2_description.pack()
    detailsFrame_h2_id.pack()
    detailsFrame_h2_name.pack()
    detailsFrame_h2_height.pack()
    detailsFrame_h2_weight.pack()
    detailsFrame_h2_types.pack()
    detailsFrame_h2_evolution.pack()
    btnBack.pack(side='left')
    
    def leftclick(evt):
        print('left')
        
    def rightclick(evt):
        print('rightclick')
    
    detailsFrame.bind('<Left>', leftclick)
    detailsFrame.bind('<Right>', rightclick)
    detailsFrame.focus_set()
    
    

    scrollCanvas = tk.Canvas(applicationFrame, width=1410, height=800)
    scrollCanvas.pack(side=LEFT)

    # TIP: SCROLLBAR ONLY WORKS ON A CANVAS!!!

    scrollBar = ttk.Scrollbar(applicationFrame, orient=VERTICAL, command=scrollCanvas.yview)
    scrollBar.pack(side=RIGHT, fill="y")

    scrollCanvas.configure(yscrollcommand=scrollBar.set)

    def onMousewheelScroll(evt):
        print('Mouse wheel activated')
        print(evt)

    scrollCanvas.bind('<Configure>', lambda e: scrollCanvas.configure(scrollregion=scrollCanvas.bbox('all')))
    h1.bind('<MouseWheel>', onMousewheelScroll)

    pokeFrame = tk.Frame(scrollCanvas)


    scrollCanvas.create_window((0, 0), window=pokeFrame, anchor="nw")
    applicationFrame.pack(fill="both", expand="yes")

    # for i in range(20):
    #     tk.Button(pokeFrame, text=f"Button {i}").pack()

    # pokemonObjects = []

    # for i in range(1, 5):
    #     # getting pokemon sprites
    #     response = requests.get(f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{i}.png') # give back response code. 200 means success!
    #     if response.status_code != 200:
    #         print("Download error")
    #     # when we send a request to an IMAGE file, we get back the BYTECODE encryption for that image
    #     # BYTECODE: text representation of an image
        
        
    #     content = response.content # returns a JSON in form of STRING
    #     bytecode_from_string = io.BytesIO(content) # convert string to bytecode so the computer can understand
    #     image_from_bytecode = Image.open(bytecode_from_string).resize((150, 150)) # make an image from bytecode
    #     image = ImageTk.PhotoImage(image_from_bytecode)   # make TK's image object to display
    #     # imagesObj.append(image)
        
    #     # label = tk.Label(root, image=image)
    #     # label.grid(column=1, row=1)
        
    #     # getting pokemon name
    #     pokeResponse = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}')
    #     name = pokeResponse.json()['forms'][0]['name'].title()
        
    #     pokemonObjects.append(
    #         {
    #         'id': i,
    #         'name': name,
    #         'sprite': image
    #         }
    #     )
    
    #     print(f'Downloaded pokemon {i}')

    with open('./data/pokemon.json') as file:
        pokemonList = json.load(file)
        file.close()
        
    for poke in pokemonList:
        image_from_bytecode = Image.open(f"./sprites/{poke['sprite']}") # make an image from bytecode
        image = ImageTk.PhotoImage(image_from_bytecode.resize((150, 150)))   # make TK's image object to display
        image_big = ImageTk.PhotoImage(image_from_bytecode.resize((300, 300)))   # make TK's image object to display
        poke['image'] = image
        poke['image_big'] = image_big
        # imagesObj.append(image)

    rowCounter = 0
    colCounter = 0

    def motion(event):
        print("Mouse position: (%s %s)" % (event.x, event.y))
        return

    def getPokemonName(i):
        print('Pokemon clicked:', i)
        # smallApp = tk.Tk()
        # tk.Label(smallApp, "New window opened").pack()
        return
    
      
    def switchFrame(event):
        if info.activeFrame == 'main':
            applicationFrame.forget()
            detailsFrame.pack()
            info.activeFrame = 'details'
        elif info.activeFrame == 'details':
            detailsFrame.forget()
            applicationFrame.pack()
            info.activeFrame = 'main'


    def on_mouse_down(event, props):
        switchFrame(event)
        # print(props['name'], props['id'])
        # print(props['image'])
        # image_from_bytecode_big = Image.open(f"./sprites/{props['sprite']}").resize((100, 100)) # make an image from bytecode
        # image_big = ImageTk.PhotoImage(image_from_bytecode_big)   # make TK's image object to display
        # print(image_big)
        print(props['image_big'])
        
        detailsFrame_h2_sprite.configure(image=props['image_big'], width=310, height=310, bg="orange")
        detailsFrame_h2_description.config(text=f"\n\"{props['description']}\"")
        detailsFrame_h2_id.config(text=f"ID:\t {props['id']}")
        detailsFrame_h2_name.config(text=f"Name:\t {props['name']}")
        detailsFrame_h2_height.config(text=f"Height:\t {props['height']} cm")
        detailsFrame_h2_weight.config(text=f"Weight:\t {props['weight']} kg")
        
        type_text = 'Type:\t' if len(props['types']) == 1 else 'Types:\t'
        for i in range(len(props['types'])):
            type_text += f"{props['types'][i]}"
            if i != len(props['types']) - 1:
                type_text += ", "
            
        detailsFrame_h2_types.config(text=type_text)
        
        evolution_text = 'Evolution chain:\t'
        for i in range(len(props['evolution_chain'])):
            evolution_text += f"{props['evolution_chain'][i]}"
            if i != len(props['evolution_chain']) - 1:
                evolution_text += ' ⏩ '
                
        detailsFrame_h2_evolution.config(text=evolution_text)
        # print(props)
        
        
    def onCanvasHoverHandler(event, poke):
        info = f"#{poke['id']} {poke['name']}"
        pokeNameLabel.config(text=info)


    for i in range(len(pokemonList)): # i = 0 -> 30
        # imgFrame = tk.Frame(pokeFrame)

        canvas = tk.Canvas(pokeFrame, width=150, height=150, bg="pink", cursor="heart")
        canvas.create_image(0, 0, anchor=NW, image=pokemonList[i]['image']) 
        # tk.Label(pokeFrame, text=pokemonObjects[i]['name']).grid(row=rowCounter, column=colCounter)
        canvas.grid(row=rowCounter, column=colCounter)
        
        # binding actions
        # canvas.bind('<Enter>', motion)
        canvas.bind('<Button-1>', lambda event, props=pokemonList[i]: on_mouse_down(event, props))
        # canvas.bind('<Button-1>', switchFrame)
        
        canvas.bind('<Enter>', lambda event, poke=pokemonList[i]: onCanvasHoverHandler(event, poke))
        # canvas.bind('<Button-1>', sayHello("HIIII")) 
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


    # TODO: REFACTOR THE CODE!!! (USING OOP)

    def closeApp(event):
        if info.activeFrame == 'main':
            sys.exit()
        elif info.activeFrame == 'details':
            switchFrame(event)
        
    app.bind('<Escape>', closeApp)
    app.mainloop()
    
    
if __name__ == '__main__':
    main()