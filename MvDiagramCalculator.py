#This program is to calculate the MV diagram on a beam.
#Reminder for Atom: To run the code use Ctrl+Shift+B

import tkinter as tk  #This is the library for the GUI

root = tk.Tk()  #This is the main window that we want to place things in

# This is the Main canvas that we draw on
Main_Canvas = tk.Canvas(root, width=1000, height=900, bg="black")

Main_Canvas.pack(pady=20)  #This pushes it a bit down


class Force:
    def __init__(self):
        self.arrayamount = []
        self.arraypos = []
    def addforce(self,amount,positon):
        self.arrayamount.append(amount)
        self.arraypos.append(positon)
    def getTotal(self):
        SigmaForcesOnPoint = 0
        for i in range(len(self.arrayamount)):
           SigmaForcesOnPoint += self.arrayamount[i]
           print("i am in teh finc")
        return(SigmaForcesOnPoint) 

#This is the logic for create_rectangle
#TL = TopLeft BR=BottomRight H=Height C=Column
StartingPointOfColumn = 100  #This is to make the future easier to work with for other drawings
Length = 900  # One of our inputs
TLofC = StartingPointOfColumn
BRofC = Length - TLofC  #We calculate the correct Length of the rectangle to draw
HofC = 50  #This is not a needed input but we can make it so
ForceArray = []
CircleSupportArray = []
TriangleSupportArray = []
MomentArray=[]
TriangleSupportReaction = 0
CircleSupportReaction = 0
NumberOfElements=0
TotMom = 0


def initialize():  #This creates the column and the MV lines
    #This is to create our Column
    Main_Canvas.create_rectangle(TLofC, -HofC, BRofC, HofC, fill="white")
    #This is to create our MV Diagram base lines
    Main_Canvas.create_line(TLofC, -HofC, TLofC, HofC + 900, fill="white")
    Main_Canvas.create_line(BRofC, -HofC, BRofC, HofC + 900, fill="white")
    Main_Canvas.create_line(TLofC, HofC + 300, BRofC, HofC + 300, fill="white")
    Main_Canvas.create_text(TLofC - 20, HofC + 300, text="V", fill="white")
    Main_Canvas.create_line(TLofC, -HofC, TLofC, HofC + 900, fill="white")
    Main_Canvas.create_line(BRofC, -HofC, BRofC, HofC + 900, fill="white")
    Main_Canvas.create_line(TLofC, HofC + 600, BRofC, HofC + 600, fill="white")
    Main_Canvas.create_text(TLofC - 20, HofC + 600, text="M", fill="white")


def TriangleSupport(InitialPlace):  #Two Force Support, InitialPlace is the location of it
    if (InitialPlace < StartingPointOfColumn or InitialPlace > BRofC):
        Main_Canvas.create_text("Invalid input")
        return
    NumberOfElements+1
    global TriangleSupportLocation
    TriangleSupportLocation = InitialPlace
    Main_Canvas.create_line(InitialPlace, HofC, InitialPlace - 30, HofC + 30, fill="red")
    Main_Canvas.create_line(InitialPlace - 30, HofC + 30, InitialPlace + 30, HofC + 30, fill="red")
    Main_Canvas.create_line(InitialPlace + 30, HofC + 30, InitialPlace, HofC, fill="red")
    # Vertical
    Main_Canvas.create_line(InitialPlace - 30, HofC + 40, InitialPlace - 30, HofC + 10, fill="cyan", width=5)
    Main_Canvas.create_line(InitialPlace - 30, HofC + 10, InitialPlace - 20, HofC + 30, fill="cyan", width=5)
    Main_Canvas.create_line(InitialPlace - 30, HofC + 10, InitialPlace - 40, HofC + 30, fill="cyan", width=5)
    TriangleSupportArray.append(InitialPlace)

    # Horizontal
    Main_Canvas.create_line(InitialPlace - 30, HofC + 40, InitialPlace, HofC + 40, fill="cyan", width=5)
    Main_Canvas.create_line(InitialPlace, HofC + 40, InitialPlace - 20, HofC + 30, fill="cyan", width=5)
    Main_Canvas.create_line(InitialPlace, HofC + 40, InitialPlace - 20, HofC + 50, fill="cyan", width=5)
    Main_Canvas.create_text(InitialPlace+10, HofC + 50, text=str(0)+"N", fill="cyan")


def CircleSupport(InitialPlace):   #One Force Support, InitialPlace is the location of it
    if (InitialPlace < StartingPointOfColumn or InitialPlace > BRofC):
        Main_Canvas.create_text("Invalid input")
        return
    global CircleSupportLocation
    CircleSupportLocation = InitialPlace
    NumberOfElements+1
    Main_Canvas.create_oval(InitialPlace - 15, HofC, InitialPlace + 15, HofC + 30, fill="red")
    Main_Canvas.create_line(InitialPlace + 20, HofC + 40, InitialPlace + 20, HofC + 10, fill="cyan", width=5)
    Main_Canvas.create_line(InitialPlace + 20, HofC + 10, InitialPlace + 10, HofC + 30, fill="cyan", width=5)
    Main_Canvas.create_line(InitialPlace + 20, HofC + 10, InitialPlace + 30, HofC + 30, fill="cyan", width=5)
    CircleSupportArray.append(InitialPlace)


def ForceOnPoint(PointOfForce, amount, force):  #Force on a point, PointOfForce is the location of it
    if (PointOfForce < StartingPointOfColumn or PointOfForce > BRofC):
        Main_Canvas.create_text("Invalid input")
        return
    NumberOfElements+1
    Main_Canvas.create_line(PointOfForce, HofC, PointOfForce, HofC - 30, fill="green", width=5)
    Main_Canvas.create_line(PointOfForce, HofC, PointOfForce - 10, HofC - 10, fill="green", width=5)
    Main_Canvas.create_line(PointOfForce, HofC, PointOfForce + 10, HofC - 10, fill="green", width=5)
    Main_Canvas.create_text(PointOfForce - 10, HofC - 35, text=str(amount) + "N")
    force.addforce(amount,PointOfForce) #we pass the force object to handle everything everywhere


def Moment(InitialPlace, MomentForce):  #Moment, InitialPlace is the location of it
    if (InitialPlace < StartingPointOfColumn or InitialPlace > BRofC):
        Main_Canvas.create_text("Invalid input")
        return
    NumberOfElements+1
    coord = [InitialPlace, HofC+40, InitialPlace-30, HofC-10]
    Main_Canvas.create_arc(coord, start=30, extent=120, style=tk.ARC, width=3, fill="pink", outline="pink")
    Main_Canvas.create_line(InitialPlace-30, HofC, InitialPlace - 15, HofC, fill="pink", width=5)
    Main_Canvas.create_line(InitialPlace-30, HofC, InitialPlace -35, HofC - 10, fill="pink", width=5)
    Main_Canvas.create_text(InitialPlace - 10, HofC - 20, text=str(MomentForce) + "N*M")
    MomentArray.append(MomentForce)


def SigmaMa(): #pass force dont make it public
    global CircleSupportReaction
    global TriangleSupportReaction
    global TotMom
    SigmaForcesOnPoint = force.getTotal()
    for i in range(len(force.arrayamount)): #force.ForceArray ! the other array is empty!
        x = 0
        x = force.arrayamount[i] * ( force.arraypos[i]- TriangleSupportLocation)
        x= x/1000
        MomentArray.append(x)
    for j in range(len(MomentArray)):
        TotMom += MomentArray[j]
    CircleSupportReaction = -(TotMom/CircleSupportLocation)
    TriangleSupportReaction = SigmaForcesOnPoint - abs(CircleSupportReaction)


def ReactionsAtSupportsText():  # Makes the text for the reactions, specifies the forces
    Main_Canvas.create_text(CircleSupportLocation + 20, HofC + 50, text=str(CircleSupportReaction)+"N", fill="cyan")
    Main_Canvas.create_text(TriangleSupportLocation - 60, HofC + 20, text=str(TriangleSupportReaction)+"N", fill="cyan")



initialize()  # DO NOT DELETE ME I DO EVERYTHING!
force = Force() 
ForceOnPoint(450,10,force)
CircleSupport(BRofC)
TriangleSupport(TLofC)
##Moment(300, 20)
SigmaMa()
ReactionsAtSupportsText()
print(TotMom)
root.mainloop()  #We use this to run the application, this has to be at the bottom of the program

#NOTE: Add the StartingPointOfColumn to whatever input
#TODO: MATH! lets actually start calculating stuff, Calculate Ma, then using basic formula of Ay + By = SigmaForcesOnPoint
