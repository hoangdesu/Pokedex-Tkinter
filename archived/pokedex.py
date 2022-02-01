import tkinter as tk
from tkinter import ttk
from tkinter.constants import *
from PIL import Image, ImageTk

import requests
import io


def main():
    
    # root = tk.Tk()

    # # raw_data = requests.get("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png")
    # im = Image.open(io.BytesIO(raw_data.content))
    # image = ImageTk.PhotoImage(im)
    # label1 = tk.Label(root, image=image)
    # label1.pack()
    
    # root.mainloop()
    
    root = tk.Tk()
    # root.wm_attributes('-alpha', 0.9)
    root.geometry("1920x1080")

    
    frame = ttk.Frame(root)
    frame.pack()
    
    mainCanvas = tk.Canvas(frame)
    mainCanvas.pack(side=LEFT)
    
    imagesObj = []
    
    scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=mainCanvas.yview)
    scrollbar.pack(side=RIGHT, fill="y")
    
    mainCanvas.configure(yscrollcommand=scrollbar.set)

    mainCanvas.bind('<Configure>', lambda e: mainCanvas.configure(scrollregion=mainCanvas.bbox('all')))
    
    imgFrame = tk.Frame(mainCanvas)
    mainCanvas.create_window((0, 0), window=imgFrame, anchor="nw")
    imgFrame.pack(fill="both", expand="yes")

    
    for i in range(1, 10):
        response = requests.get(f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{i}.png') # give back response code. 200 means success!
        if response.status_code != 200:
            print("Download error")
        # when we send a request to an IMAGE file, we get back the BYTECODE encryption for that image
        # BYTECODE: text representation of an image
        
        
        content = response.content # returns a JSON in form of STRING
        bytecode_from_string = io.BytesIO(content) # convert string to bytecode so the computer can understand
        image_from_bytecode = Image.open(bytecode_from_string).resize((150, 150)) # make an image from bytecode
        image = ImageTk.PhotoImage(image_from_bytecode)   # make TK's image object to display
        imagesObj.append(image)
        # label = tk.Label(root, image=image)
        # label.grid(column=1, row=1)
        print(f'Download pokemon {i} successfully!')
    
    # print(image_from_bytecode.mode)
    rowCounter = 0
    colCounter = 0
    for i in range(len(imagesObj)): # i = 0 -> 30
        canvas = tk.Canvas(imgFrame, width=150, height=150, bg="pink")
        canvas.create_image(0, 0, anchor=NW, image=imagesObj[i]) 
        canvas.grid(row=rowCounter, column=colCounter)
        colCounter += 1
        if colCounter > 8:
            rowCounter += 1
            colCounter = 0

    for i in range(30):
        tk.Button(imgFrame, text=f"Button {i}").grid(row=i*2)
    # for i in range(100):
    #     tk.Button(frame, text=f"Button {i}").pack(side=BOTTOM)
        
        
        # for col in range(12):        
        #     label = tk.Label(root, image=imagesObj[i])

        #     label.grid(column=col, row=i)
    
#     canvas = Canvas(root, width = 300, height = 300)  
# canvas.pack()  
# img = ImageTk.PhotoImage(Image.open("ball.png"))  
# canvas.create_image(20, 20, anchor=NW, image=img) 
    
    root.mainloop()
        
        
        
        














if __name__ == '__main__':
    main()
    
    
    
    
    
# IDE = Integrated Development Environment
#     - Heavy
#     - Provides more functionalities
#     - Truck
# Code editor:
#     - Light weight, fast
#     - Less functions
#     - Lambo

