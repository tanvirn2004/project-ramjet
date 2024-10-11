import mysql.connector
from geopy.distance import geodesic

# Connect to MariaDB
conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='airport_db',
    user='root',
    password='2004',
    autocommit=True,
    charset="utf8mb4",
    collation="utf8mb4_general_ci"
)
cursor = conn.cursor()


# Function to calculate distance between two airports
def calculate_distance(airport1, airport2):
    cursor.execute("SELECT Latitude, Longitude FROM Airports WHERE AirportID = %s", (airport1,))
    lat1, lon1 = cursor.fetchone()
    cursor.execute("SELECT Latitude, Longitude FROM Airports WHERE AirportID = %s", (airport2,))
    lat2, lon2 = cursor.fetchone()
    return geodesic((lat1, lon1), (lat2, lon2)).kilometers


# Function to get available airport codes
def get_airport_codes():
    cursor.execute("SELECT AirportID, AirportName FROM Airports")
    airports = cursor.fetchall()
    return {airport[0]: airport[1] for airport in airports}


# Function to get airport name by ID
def get_airport_name(airport_id):
    cursor.execute("SELECT AirportName FROM Airports WHERE AirportID = %s", (airport_id,))
    return cursor.fetchone()[0]


# Function to buy a frigate
def buy_frigate(concords):
    frigates = {
        1: ("EtherBus", 300)
    }
    print("Available frigates for purchase:")
    for id, (name, cost) in frigates.items():
        print(f"{id}. {name} - {cost} Concords")

    choice = int(input("Enter the number of the frigate you want to buy: "))
    if choice in frigates:
        name, cost = frigates[choice]
        if concords >= cost:
            concords -= cost
            print(f"You have purchased {name}.\n")
            return name, concords
        else:
            print("You do not have enough Concords.")
    else:
        print("Invalid choice.")
    return None, concords


# Function to start the game
def start_game():
    print("Welcome to RamJet. [Early Demo Version.] \n")
    print("Choose your starting frigate:")
    print("[1] Suedebird")
    print("[2] SoaringV \n")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        frigate = "Suedebird"
    else:
        frigate = "SoaringV"

    print(f"You have chosen {frigate}.")
    current_location = 1  # Assuming starting at airport with ID 1
    concords = 0

    # Quests
    quests = [
        {"npc": "Timur", "location": 103, "reward": 150,
         "dialogue": "Welcome, traveler! I am Timur. Your journey has just begun. I hope the landing wasn't all bumpy when you arrived here in Chisinau Airport. Can you do something for me? I have these top secret files I'd like to send to my colleague Tanvir. You should find him in Bangladesh. Best of luck on your journey!\n"},
        # Moldova
        {"npc": "Tanvir", "location": 102, "reward": 100,
         "dialogue": "Greetings! I am Tanvir. Oh, you have something for me? How did you get these? If you got these from who I think you got them from, that means you can be trusted. Our world is in danger, and we need a new teammate to fix it. I know this guy Nadim, from what I remember he should be in Amsterdam. Please find him! \n"},
        # Bangladesh
        {"npc": "Nadim", "location": 104, "reward": 100,
         "dialogue": "Hello! I am Nadim. You've made it to Amsterdam. I have expected you.. You are him, The Traveler! You're the one who will help us build the RamJet. It is a frigate never heard of before, between the common Sedentars. I heard there are fragments of its existence only in Iran. Please go find them, I depend on you. \n"},
        # Amsterdam
        {"npc": "Kiavash", "location": 101, "reward": 200,
         "dialogue": "Salutations! I am Kiavash. Oh wow, I haven't heard that name in ages! It was supposed to be a secret project.. I can't even think of who would be so irresponsible to leak that information! Or you must be.. The Traveler? No, it can't be. Alright, only one way to find out. If I show you the remainings of the RamJet! But I need something in return. To prove your worthiness, show me you can aquire a more respectable frigate. Come back in an EtherBus, I always loved those. \n"}
        # Iran
    ]
    active_quest = quests.pop(0)

    while True:
        print(f"Current location: [ID NUMBER: {current_location}] \n")
        print("[1] Travel to a new location")
        print("[2] View quests")
        print("[3] Buy a new frigate")
        print("[4] Exit\n")
        choice = input("Enter your choice: ")

        if choice == "1":
            airport_codes = get_airport_codes()
            print("Available destinations:")
            for code, name in airport_codes.items():
                print(f"{code}: {name}")
            destination = int(input("Enter the AirportID of your destination: "))
            if destination in airport_codes:
                distance = calculate_distance(current_location, destination)
                print(f"Distance to destination: {distance} km")
                current_location = destination
                concords += distance
                print(f"Concords earned: {concords}\n")

                # Check if the quest is completed
                if active_quest and current_location == active_quest["location"]:
                    print(
                        f"Quest completed! You have met {active_quest['npc']} at {get_airport_name(active_quest['location'])}.")
                    print(f"{active_quest['npc']}: {active_quest['dialogue']}")
                    concords += active_quest["reward"]
                    print(f"Quest reward: {active_quest['reward']} Concords")
                    if quests:
                        active_quest = quests.pop(0)
                    else:
                        active_quest = None
            else:
                print("Invalid AirportID. Please try again.")
        elif choice == "2":
            if active_quest:
                quest_destination_name = get_airport_name(active_quest["location"])
                print(f"Active quest: Meet {active_quest['npc']} at {quest_destination_name}")
            else:
                print("No active quests.")
        elif choice == "3":
            new_frigate, concords = buy_frigate(concords)
            if new_frigate:
                frigate = new_frigate
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


# Start the game
start_game()

# Close the database connection
cursor.close()
conn.close()

