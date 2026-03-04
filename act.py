import re
import random
from colorama import Fore, init


# Initialize colorama
init(autoreset=True)


# Travel destinations database
destinations = {
   "beaches": ["Baga beach", "cherai beach", "dhanushkoti","arjuna beach"],
   "mountains": ["andes mountains", "Rocky Mountains", "Himalayas"],
   "cities": ["lucknow", "amritsar", "jhansi","gwalior","kochi","kanyakumari"]
}


# Collection of travel-related jokes
jokes = [
   "Why don't programmers like nature? Too many bugs!",
   "Why did the computer go to the doctor? Because it had a virus!",
   "Why do travelers always feel warm? Because of all their hot spots!"
   "what do you call a paper aeroplane that can't  fly, a stationary"
   "why do employees stay in shape, they run out of work"
   "I tried to make a pun about a vaccum, it sucked"
]


def normalize_input(text):
   """Clean and standardize user input by removing extra spaces and converting to lowercase"""
   return re.sub(r"\s+", " ", text.strip().lower())


def recommend():
   """Recommend a travel destination based on user preference"""
   print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
   preference = input(Fore.YELLOW + "You: ")
   preference = normalize_input(preference)
  
   if preference in destinations:
       suggestion = random.choice(destinations[preference])
       print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
       print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
       answer = input(Fore.YELLOW + "You: ").lower()
      
       if answer == "yes":
           print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
       elif answer == "no":
           print(Fore.RED + "TravelBot: Let's try another.")
           recommend()  # Recursive call if the user rejects the suggestion
       else:
           print(Fore.RED + "TravelBot: I'll suggest again.")
           recommend()  # Recursive call on unrecognized answer
   else:
       print(Fore.RED + "TravelBot: Sorry, I don't have that type of destination.")
  
   show_help()


def packing_tips():
   """Provide packing tips based on destination and duration"""
   print(Fore.CYAN + "TravelBot: Where to?")
   location = normalize_input(input(Fore.YELLOW + "You: "))
   print(Fore.CYAN + "TravelBot: How many days?")
   days = input(Fore.YELLOW + "You: ")
  
   print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
   print(Fore.GREEN + "- Pack versatile clothes.")
   print(Fore.GREEN + "- Bring chargers/adapters.")
   print(Fore.GREEN + "- Check the weather forecast.")


def tell_joke():
   """Tell a random travel-related joke"""
   print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")


def show_help():
   """Display available commands and features"""
   print(Fore.MAGENTA + "\nI can:")
   print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")
   print(Fore.GREEN + "- Offer packing tips (say 'packing')")
   print(Fore.GREEN + "- Tell a joke (say 'joke')")
   print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")
    

def chat():
   """Main chat function that handles user interaction"""
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


if __name__ == "__main__":
   chat()

