from .core import get_git_diff, generate_commit_message, update_api_key
import subprocess
from colorama import Fore, Style
import sys

def main():

    # command calls function update_api_key for users to update open ai key
    if "--update-key" in sys.argv:
        update_api_key()
        return  

    diff_text = get_git_diff()

    # condition to decide if there has been changes to commit
    if not diff_text:
        print("\nNothing has changed")
    else:
        commit_message = generate_commit_message(diff_text)
        if commit_message:
            print(f'{Fore.GREEN}\n---- GENERATED COMMIT MESSAGE ----\n{Style.RESET_ALL}"{commit_message}"\n')
        else:
            print(f"{Fore.RED}Failed to generate message{Style.RESET_ALL}")

        # gives option for users to automatically commit message
        while True:
            user_commit = input(f"Do you want to commit using this message? (y/n/c): ").strip().lower()
        
            if user_commit == "y":
                # auto commits using ai generated message
                subprocess.run(["git", "commit", "-m", f"{commit_message}"])
                break
            # users can enter custom commit if not happy with ai one
            elif user_commit == "c":
                user_input = input("Enter custom commit message: ")
                subprocess.run(["git", "commit", "-m", user_input])
                break
            elif user_commit == "n":
                print("message not commited")
                break
            

            else:
                print(f"{Fore.RED}Invalid answer: type 'y' or 'n'{Style.RESET_ALL}")
                continue