import mysql.connector
from geopy.distance import geodesic

# Connect to MariaDB
conn = mysql.connector.connect(
     host='localhost',
        port=3306,
        database='airport_db',
        user='root',
        password='password',
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
            print(f"You have purchased {name}.")
            return name, concords
        else:
            print("You do not have enough Concords.")
    else:
        print("Invalid choice.")
    return None, concords

# Function to start the game
def start_game():
    print("Welcome to RamJet. Early Demo Version.")
    print("Choose your starting frigate:")
    print("1. Suedebird")
    print("2. SoaringV")
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
        {"npc": "Timur", "location": 103, "reward": 150, "dialogue": "Welcome, traveler! I am Timur. Your journey has just begun."},  # Moldova
        {"npc": "Tanvir", "location": 102, "reward": 100, "dialogue": "Greetings! I am Tanvir. Your adventure continues here."},  # Bangladesh
        {"npc": "Nadim", "location": 104, "reward": 100, "dialogue": "Hello! I am Nadim. You've made it to Amsterdam."},  # Amsterdam
        {"npc": "Kiavash", "location": 101, "reward": 200, "dialogue": "Salutations! I am Kiavash. Your quest is nearing its end."}  # Iran
    ]
    active_quest = quests.pop(0)

    while True:
        print(f"Current location: {current_location}")
        print("1. Travel to a new location")
        print("2. View quests")
        print("3. Buy a new frigate")
        print("4. Exit")
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
                print(f"Concords earned: {concords}")

                # Check if the quest is completed
                if active_quest and current_location == active_quest["location"]:
                    print(f"Quest completed! You have met {active_quest['npc']} at {get_airport_name(active_quest['location'])}.")
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
