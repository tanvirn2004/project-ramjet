class Frigate:
    def __init__(self, name, range, elementalprot):
        self.name = name
        self.range = range
        self.elementalprot = elementalprot

class Traveler:
    def __init__(self, name, frigate):
        self.name = name
        self.frigate = frigate
        self.concords = 0
        self.visited_locations = []

class Location:
    def __init__(self, name, distance, elements):
        self.name = name
        self.distance = distance
        self.elements = elements

class Quest:
    def __init__(self, description, reward):
        self.description = description
        self.reward = reward

frigates = [Frigate("SuedeBird", 560, 7), Frigate("GraceHunk", 650, 5)]
locations = [Location("Airport A", 300, "Zephyrs"), Location("Airport B", 450, "The Ether")]
quests = [Quest("Deliver cargo to Airport A", 100), Quest("Rescue mission at Airport B", 150)]


def main():
    print("Welcome, Traveler! Choose your starting frigate:")
    for i, frigate in enumerate(frigates):
        print(f"{i + 1}. {frigate.name} (Range: {frigate.range} km, Elemental Protection: {frigate.elementalprot}/11)")

    choice = int(input("Enter the number of your choice: ")) - 1
    traveler = Traveler("The Traveler", frigates[choice])

    while True:
        print("\nMain Menu:")
        print("1. Travel to a new location")
        print("2. View quests")
        print("3. View frigates")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            travel(traveler)
        elif choice == 2:
            view_quests(traveler)
        elif choice == 3:
            view_frigates(traveler)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")


def travel(traveler):
    print("\nAvailable Locations:")
    for i, location in enumerate(locations):
        print(f"{i + 1}. {location.name} (Distance: {location.distance} km, Elements: {location.elements})")

    choice = int(input("Enter the number of your choice: ")) - 1
    location = locations[choice]

    if traveler.frigate.range >= location.distance:
        print(f"Traveling to {location.name}...")
        traveler.visited_locations.append(location.name)
        traveler.concords += location.distance // 10  # Award Concords based on distance
        print(f"Arrived at {location.name}. You earned {location.distance // 10} Concords.")
    else:
        print("Your frigate cannot travel that far. Choose a closer location or upgrade your frigate.")


def view_quests(traveler):
    print("\nAvailable Quests:")
    for i, quest in enumerate(quests):
        print(f"{i + 1}. {quest.description} (Reward: {quest.reward} Concords)")

    choice = int(input("Enter the number of the quest to complete: ")) - 1
    quest = quests[choice]

    print(f"Completing quest: {quest.description}...")
    traveler.concords += quest.reward
    print(f"Quest completed! You earned {quest.reward} Concords.")


def view_frigates(traveler):
    print("\nYour Frigate:")
    print(f"Name: {traveler.frigate.name}, Range: {traveler.frigate.range} km")
    print(f"Concords: {traveler.concords}")


if __name__ == "__main__":
    main()