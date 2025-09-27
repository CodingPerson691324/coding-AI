import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initialize colorama
colorama.init()

# Welcome message
print(f"{Fore.CYAN}👾 Welcome to Sentiment Spy! 👾{Style.RESET_ALL}")

# Ask for user name (fallback if empty)
user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "Mystery Agent"

# Conversation history list
conversation_history = []

# Instructions
print(f"\n{Fore.CYAN}Hello, Agent {user_name}!")
print(f"Type a sentence and I will analyze your sentences with TextBlob 🤖")
print(f"Type {Fore.YELLOW}history{Fore.CYAN}, {Fore.YELLOW}reset{Fore.CYAN}, or {Fore.YELLOW}exit{Fore.CYAN} to quit.{Style.RESET_ALL}\n")

# Main loop
while True:

    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}please enter the some text or a vald command")
        continue

    # Commands
    if user_input.lower() == "exit":
        print(f'\n{Fore.BLUE}exiting  sentiment spy. farewell agent {user_name}! {Style.RESET_ALL}')
        break

    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f'{Fore.CYAN} all conversation history cleared!{Style.RESET_ALL}')
        continue

    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}📜 Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                # Choose color & emoji based on sentiment
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😞"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"

                print(f"{idx}. {color}{emoji} {text} "
                      f"(Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")
        continue

    # Analyze sentiment
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😞"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    # Store in history
    conversation_history.append((user_input, polarity, sentiment_type))

    # Print result with color, emojis, and polarity
    print(f"{color}{emoji} {sentiment_type} sentiment detected! "
          f"(Polarity: {polarity:.2f}){Style.RESET_ALL}")


