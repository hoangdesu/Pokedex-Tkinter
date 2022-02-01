import tkinter as tk

class Info:
    activeFrame = 1

def main():
    info = Info()
    info.activeFrame
    app = tk.Tk()

    frame1 = tk.Frame(app, bg="pink")
    frame2 = tk.Frame(app, bg="yellow")

    def switchFrameHandler():
        print(frame2)
        if info.activeFrame == 1:
            frame1.pack_forget()
            frame2.pack()
            info.activeFrame = 2
        elif info.activeFrame == 2:
            frame2.forget()
            frame1.pack()
            info.activeFrame = 1

    tk.Label(frame1, text="Frame 1", fg="red").pack()
    tk.Button(frame1, text="Go to Frame 2", command=lambda: switchFrameHandler()).pack()

    tk.Label(frame2, text="Frame 2", fg="purple").pack()
    tk.Button(frame2, text="Go back to Frame 1", command=lambda: switchFrameHandler()).pack()

    frame1.pack()

    app.mainloop()
    
if __name__ == '__main__':
    main()