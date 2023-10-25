streamingService = {
    "Amazon" : "Amazon",
    "Apple" : "Apple",
    "Spotify" : "Spotify",
}

class SmartPlug():
    """
    A class representing a Smart Plug. 
    The Plug can have two states: TRUE and FALSE.
    The Plug will have a consumption rate between the values of 0 and 150.
    The consumption rate is set automatically to 0.
    """
    def __init__(self):
        """
        Creates the Instance Variables for the Smart Plug
        """
        self.switchedOn = False
        self.consumptionRate = 0

    def toggleSwitch(self):
        """
        Changes the switch to the opposite state of the Smart Plug
        """
        self.switchedOn = not self.switchedOn
        
    def getSwitchedOn(self):
        """
        Return the current switch state of the Smart Plug.
        """
        return self.switchedOn

    def getConsumptionRate(self):
        """
        Returns the current consumption rate of the Smart Plug.
        """
        return self.consumptionRate

    def setConsumptionRate(self, newConsumptionRate):
        """
        Sets the current consumption rate of the Smart Plug.
        Checks whether the new consumption rate is within the alocated range.
        """
        self.consumptionRate = newConsumptionRate
        if newConsumptionRate > 150:
            self.consumptionRate = 0
            print("The consumption rate is to large. The consumption rate will therefore be set to 0")
        elif newConsumptionRate < 0:
            self.consumptionRate = 0
            print("The consumption rate is to small. The consumption rate will therefore be set to 0")
        
    def __str__(self):
        """
        Returns the string representation of the Smart Plug instance variables
        """
        output = "Plug Status: {}, {}".format(self.switchedOn, self.consumptionRate)
        return output

class SmartSpeaker():
    """
    Creates a class representing a Smart Speaker
    The Smart Speaker can have two states: True or False
    The Smart Speaker can have three streaming options: Amazon, Apple, Spotify
    The Smart Speaker's default streaming option is Amazon
    """
    def __init__(self):
        """
        Creates the Instance Variables for the Smart Speaker
        """
        self.switchedOn = False
        self.streaming = "Amazon"
    
    def toggleSwitch(self):
        """
        Changes the switch to the opposite state of the Smart Speaker
        """
        self.switchedOn = not self.switchedOn
    
    def getSwitchedOn(self):
        """
        Returns the current switch state of the Smart Speaker.
        """
        return self.switchedOn
    
    def getStreaming(self):
        """
        Returns the current streming service of the Smart Speaker.
        """
        return self.streaming
    
    def setStreaming(self, newStreaming):
        """
        Sets the Streaming service of the Smart Speaker, based upon a dictionary defined as a global variable
        """
        if newStreaming in streamingService:
            currentStream = streamingService[newStreaming]
            self.streaming = currentStream
         
    def __str__(self):
        """
        Returns the string representation of the Smart Plug instance variables
        """
        output = "Speaker Status: {}, {}".format(self.switchedOn, self.streaming)
        return output

class SmartHome():
    """
    Creates a class representing a Smart Home
    The Smart Home has an empty list which can have smart devices added to it
    The Smart Home is able to toggle all the Smart Devices within the list ON and OFF
    """
    def __init__(self):
        """
        Creates the Instace Variables for the Smart Home"""
        self.devices = []

    def getDevices(self):
        """
        Returns the  list of Smart Devices to the User
        """
        return self.devices
    
    def getTrueDevices(self):
        """
        retruns the number of devices that are set to true
        """
        count = 0
        for device in self.devices:
            if device.getSwitchedOn():
                count += 1
        return count

    def getDeviceAt(self, index):
        """
        Returns the Smart Device at a specific index within the list
        """
        return self.devices[index]

    def getDeviceLength(self):
        """Returns the length of the Smart devices list"""
        return len(self.devices)
    
    def addDevice(self, newDevice):
        """
        Adds a Smart Device to the list
        """
        self.devices.append(newDevice)

    def toggleSwitch(self, index):
        """
        Calls a specific Smart Device within the list to be toggled
        """
        deviceToToggle = self.devices[index]
        deviceToToggle.toggleSwitch()

    def turnOnAll(self):
        """
        Turns all devices in the list to ON
        """
        for i in range(len(self.devices)):
            deviceToToggle = self.devices[i]
            deviceToToggle.switchedOn = False
            deviceToToggle.toggleSwitch()

    def turnOffAll(self):
        """
        Turns all devices in the list to OFF
        """
        for i in range(len(self.devices)):
            deviceToToggle = self.devices[i]
            deviceToToggle.switchedOn = True
            deviceToToggle.toggleSwitch()


    def __str__(self):
        "Retruns the string representation of the Smart Home variables"
        output = "Smart Home contains:\n"
        for item in self.devices:
            output += "{}\n".format(item)
        return output
        

def testSmartPlug():
    """
    Tests to see whether Smart Plug works properly.
    -   Task 1: Creates an Instance of the Smart Plug
    -   Task 2: Toggles the switch to True
    -   Task 3: Prints the current status of the switch (True)
    -   Task 4: Prints the current consumption rate (0) and then sets the consumption rate to a new value (125) and prints again
    -   Task 5: Prints the entire Smart Plug
    """
    plug = SmartPlug()
    plug.toggleSwitch()
    print("Plug status: {}".format(plug.getSwitchedOn()))
    print("Consumption rate is currently: {}".format(plug.getConsumptionRate()))
    plug.setConsumptionRate(125)
    print("Consumption rate is currently: {}".format(plug.getConsumptionRate()))
    print(plug)
testSmartPlug()

def testDevice():
    """
    Tests to see whether Smart Speaker works properly.
    -   Task 1: Creates an Instance of the Smart Speaker class
    -   Task 2: Toggles the Speaker to True
    -   Task 3: Prints the current status of the Spepaker (True)
    -   Task 4: Prints the current streaming service (Amazon) and then changes the streaing service (Apple) and prints again
    -   Task 5: Prints the entire Smart Speaker
    """
    device = SmartSpeaker()
    device.toggleSwitch()
    print("Device status: {}".format(device.getSwitchedOn()))
    device.setStreaming("Apple")
    print("Current streaming service: {}".format(device.getStreaming()))
    print(device)
testDevice()

def testSmartHome():
    """Tests to see whether the SmartHome class works properly
    - Task 1: Creates an instance of the Smart Home
    - Task 2: Creates 2 instances of the Smart Plug called plug1 and plug2
    - Task 3: Creates an instance of the Smart Speaker 
    - Task 4: Turn plug2 on
    - Task 5: Sets the consumption rate of plug2 to 45
    - Task 6: Changes the Streaming Service to Spotify
    - Task 7: Adds plug1, plug2 abd the Smart Speaker to the Smart Home
    - Task 8: Prints the Smart Home
    - Task 9: Turns on all devices in the Smart Home
    - Task 10: Prints the Smart Home again
    """


    smartHouse = SmartHome()
    plug1 = SmartPlug()
    plug2 = SmartPlug()
    speaker1 = SmartSpeaker()
    plug2.toggleSwitch()
    plug2.setConsumptionRate(45)
    smartHouse.addDevice(plug1)
    smartHouse.addDevice(plug2)
    smartHouse.addDevice(speaker1)
    print(smartHouse)
    smartHouse.turnOnAll()
    print(smartHouse)
testSmartHome()
