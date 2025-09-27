import re, random
from colorama import Fore, init

init(autoreset=True)

destinations = {'beaches': ['Bali', 'maldive', 'phuket'],
                'mountains': ['swiss alps', 'rock mountains', 'himalayas'],
                'cities': ['tokyo', 'paris', 'newyork']
}

jokes = ['why dont the poragramers like nature? too many bugs!', 'why did the computer go to the docter? because it had a virus', 'why di travelers always feel warm? because of all their hot spots!']

def normalize_input(text):
    return re.sub(r'/s+', '', text.strip().lower())

def recommend():
    print(Fore.CYAN + 'travelbot: beaches, mountains, or cities?')
    preference = input(Fore.YELLOW + 'you: ')
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f'travelbot: how about {suggestion}')
        print(Fore.CYAN +'travelbot: do u like it (yes or no)')
        answer = input(Fore.YELLOW + 'You: ').lower()

        if answer == 'yes':
            print(Fore.GREEN + f'travel bot: do youj like it? (yes no)')
        elif answer == 'no':
            print(Fore.RED + 'Travelbot: lets tyry another')
        else:
            print(Fore.RED+ 'travel bot: ill suiggest again')

    else:
        print(Fore.RED + 'travel bot : sorry, i dont havwe that type of destiantion')

    show_help()
# Offer packing tips based on user’s destination and duration
def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")
    
    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile clothes.")
    print(Fore.GREEN + "- Bring chargers/adapters.")
    print(Fore.GREEN + "- Check the weather forecast.")

# Tell a random joke
def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

# Display help menu
def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

# Main chat loop
def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")
    
    show_help()
    
    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)
        
        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")

# Run the chatbot
if __name__ == "__main__":
    chat()

