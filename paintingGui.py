import tkinter as tk
import SimsPaintingProgram as SPP
import makedict as md
def getOptions():
    options = md.getDict()
    optionList = []
    for i in options:
        optionList.append(i)
    return optionList
window = tk.Tk()
def changeWindowAddPainting():
    makeAddFrame()
    addFrame.pack(fill='both',expand=1)
    menuFrame.pack_forget()
window.geometry("500x300")

def countBtn():
    makeCountFrame()
    countFrame.pack(fill='both',expand=1)
    menuFrame.pack_forget()
    return

menuFrame = tk.Frame(window)
addFrame = tk.Frame(window)
countFrame = tk.Frame(window)


options = getOptions()
paintType = tk.StringVar()
paintType.set("Figure Painting")
menuLabel = tk.Label(menuFrame,text="Main Menu")
AddButton = tk.Button(menuFrame,text="Add Paintings",command=changeWindowAddPainting)
typeButton = tk.Button(menuFrame,text="Type Counts",command=countBtn)
costButton = tk.Button(menuFrame,text="Total Costs")
saleButton = tk.Button(menuFrame,text="Total Sales")
gainButton = tk.Button(menuFrame,text="Net Gain")
bestButton = tk.Button(menuFrame,text="Best Selling")

drop = tk.OptionMenu(addFrame,paintType,*options)

cost = tk.Entry(addFrame)


def startChoice():
    print("run")
    print(cost.get())
    print(paintType.get())
    SPP.choice(cost.get(),paintType.get())

def addDropShow():
    pass
def makeAddFrame():
    addLabel = tk.Label(addFrame,text="Add Paintings")
    explainLabel = tk.Label(addFrame,text="Please Select The Chosen Painting from sims 4:")
    explainLabel2 = tk.Label(addFrame,text="Please type the sale value of the painting")
    addPaint = tk.Button(addFrame,text="Add Painting",command= startChoice)
    addLabel.pack()
    explainLabel.pack()
    drop.pack()

    explainLabel.pack()
    cost.pack()
    
    addPaint.pack()


    
def makeCountFrame():
    
    FigureCount,SmallCount,MedCount,LrgCount,MoodCount = SPP.getCounts()
    
  
   
     
    label1 = tk.Label(countFrame,text="{}{}".format("Figure Paintings: ",FigureCount))
    label2 = tk.Label(countFrame,text="{}{}".format("Small Paintings: ",SmallCount))
    label3 = tk.Label(countFrame,text="{}{}".format("Medium Painting: ",MedCount))
    label4 = tk.Label(countFrame,text="{}{}".format("Large Painting: ",LrgCount))
    label5 = tk.Label(countFrame,text="{}{}".format("Mood Paintings: ",MoodCount))

    label1.pack()
    label2.pack()
    label3.pack()
    label4.pack()
    label5.pack()
    



    
        
    






menuLabel.pack()
AddButton.pack()
typeButton.pack()
costButton.pack()
saleButton.pack()
gainButton.pack()
bestButton.pack()
menuFrame.pack()

window.mainloop()