"""
Imports:
- the tkinter library
- the SmartPlug, SmartSpeaker and the SmartHome classes from the backend
"""
from tkinter import * 
from backend import SmartPlug
from backend import SmartSpeaker
from backend import SmartHome

"""
Defines the smart home class and tkinter library as a global variable
"""
mainWin = Tk()
home = SmartHome()


def setupHome():
    """
    Creates 5 Smart Devices for the Smart Home, in the order of: SP,C,SP,C,C
    Then adds them to the Smart Home
    """
    plug1 = SmartPlug()
    home.addDevice(plug1)
    speaker1 = SmartSpeaker()
    home.addDevice(speaker1)
    plug2 = SmartPlug()
    home.addDevice(plug2)
    speaker2 = SmartSpeaker()
    home.addDevice(speaker2)
    speaker3 = SmartSpeaker()
    home.addDevice(speaker3)

def createMainWin():
    """
    Creates the Main window where the devices made in setupHome() are made.
    Divivdes the window into 2 columns, with one taking up 2/3 of the window and the other the remaining first.

    """
    mainWin.title("UP2111454")
    numberOfSmartDevices = home.getDeviceLength()
    height = 50 * (numberOfSmartDevices + 2)
    mainWin.geometry("350x{}".format(height))
    mainWin.resizable(False, False)

    mainWin.columnconfigure(index = 0, weight =2)
    mainWin.columnconfigure(index = 1, weight =1)

    """ creating the buttons:"""
    """ Universal toggles"""
    toggleAllOn = Button(mainWin, text="Toggle All ON", command=lambda:toggleAllOn())
    toggleAllOn.grid(row=0, column=0,padx = 15, pady = 5, sticky= "nw")

    toggleAllOff = Button(mainWin, text="Toggle All OFF", command=lambda:toggleAllOff())
    toggleAllOff.grid(row=1, column=0,padx = 15, pady = 5, sticky= "nw")

    deviceButtons = []

    def toggleAllOn():
        for deviceIndex in range(numberOfSmartDevices):
            home.turnOnAll()
            updateDeviceText(deviceIndex)

    def toggleAllOff():
        for deviceIndex in range(numberOfSmartDevices):
            home.turnOffAll()
            updateDeviceText(deviceIndex)

    def toggleDevice(deviceIndex):
        home.toggleSwitch(deviceIndex)
        updateDeviceText(deviceIndex)

    def updateDeviceText(deviceIndex):
        device = home.getDeviceAt(deviceIndex)
        deviceText = deviceButtons[deviceIndex]
        deviceText.delete("1.0", END)
        deviceText.insert("1.0", str(device))
        totalLabel = Label(mainWin, text="Total number of On devices is: {}".format(home.getTrueDevices()))
        totalLabel.grid(row=8, column=0, padx=15, pady=10, sticky="nw")


    for deviceIndex in range(numberOfSmartDevices):
        device = home.getDeviceAt(deviceIndex)
        deviceText = Text(mainWin, height = 2, width= 30)
        deviceText.insert("1.0", str(device))
        deviceText.grid(row = deviceIndex + 2, column = 0, padx = 15, pady = 5, sticky="nw")
        deviceButtons.append(deviceText)
    
        toggleBtn=Button(mainWin,text="Toggle", command=lambda deviceIndex=deviceIndex: toggleDevice(deviceIndex)) 
        toggleBtn.grid(row=deviceIndex +2,column = 1,padx = 15,pady = 5, sticky= "nw")
        
        updateDeviceText(deviceIndex)
        



    mainWin.mainloop()



def main():
    setupHome()
    createMainWin()

main()