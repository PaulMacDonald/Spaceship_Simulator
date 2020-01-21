from Crew import Crew


def main():
    # TESTING CRAP
    myCrew = Crew(5) # construct a crew of size 5

    myCrew.startRepairing()

    print(myCrew.getBusyRepairing()) # TRUE
    print(myCrew.getRepairTimeLeft()) # 2
    print(myCrew.getSize()) # 5

    myCrew.update()

    print(myCrew.getBusyRepairing()) # TRUE
    print(myCrew.getRepairTimeLeft()) # 1
    print(myCrew.getSize()) # 5



    # TODO create spaceship and MAKE SURE TO TEST EVERY INTERACTION WITH CREW!!!
    # TODO simulator loops through clock cycles but first asks crew size, and each time gives certain amount of choices (fire, repair, etc.)
    # think of everything the simulator should show each iteration!!!

# main() function call (to start da program)
if __name__ == "__main__":
    main()