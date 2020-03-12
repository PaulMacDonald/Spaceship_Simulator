class Spaceship:

    # CONSTRUCTOR
    # (takes in crew, as well as numbers for phaser charge and fuel, all fed from main)
    def __init__ (self, theCrew, thePhaserCharge, theFuel):
        self.crew = theCrew # assign the crew fed in from main() as the ship's crew element
        self.phaserCharge = int(thePhaserCharge) # [default phaser charge is 3 (full)]
        self.fuel = int(theFuel) # [default fuel level is 10 (full)]

    # GETTERS



    # SETTERS



    # OTHER FUNCTIONS (damage, fire, repair, update)

    # Runs when ship takes on damage
    def damage(self, severityIndex):
        # TODO

    # Runs when ship fires on enemy
    def fire(self):
        # TODO

    # Runs when crew (of specific number) are sent to repair damage done by enemy
    def repair(self, numberOfCrewSent):
        # TODO

    # Update function

    # Calls crew update(), lowers fuel by one, and increases phaserCharge by 1
    def update(self):
        self.crew.update()
        self.fuel = int(self.fuel - 1) 
        self.phaserCharge = int(self.phaserCharge - 1)