class Crew:

    #Constructor
    # (takes in number of crew members [theSize])
    def __init__(self, theSize):
        self.size = int(theSize)
        self.busyRepairing = bool(False) # defaults to false until they actually start on a repair)
        self.repairTimeLeft = int(0) # also default value

    # GETTERS
    def getSize(self):
        return self.size # returns number of members in crew

    def getBusyRepairing(self):
        if self.repairTimeLeft != 0:
            self.busyRepairing = True # sets bool to true, indicating the crew is busy repairing currently and cannot complete requested action
        else:
            self.busyRepairing = False # crew is not busy — what is your wish, master?

        return self.busyRepairing # returns previously mentioned bool

    def getRepairTimeLeft(self):
        return self.repairTimeLeft # returns repair time left (calculated by function calculateRepairTime())

    # SETTERS

    def setRepairTimeLeft(self, theTimeLeft):
        self.repairTimeLeft = theTimeLeft # sets repairTimeLeft to parameter fed into function

    # OTHER FUNCTIONS

    def startRepairing(self): # called when repair is begun
        self.repairTimeLeft = round(10 / self.size) # the bigger the crew, the smaller the repair time required

    # Update function
    def update(self):
        if self.repairTimeLeft != 0: 
            self.repairTimeLeft -= 1 # decrease repair time left by one time unit
