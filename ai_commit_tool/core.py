import subprocess
import os
from openai import OpenAI
import keyring
from dotenv import load_dotenv
from colorama import Fore, Style

load_dotenv()  # load environment variables from .env file

# function to load open ai key from either .env file or users can input one 
def load_api_key():
    
    # try to get the API key from the environment variable
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        return api_key

    # try to get the API key from the keyring
    try:
        api_key = keyring.get_password("ai_commit_tool", "OPENAI_API_KEY")
        if api_key:
            return api_key
    except keyring.errors.KeyringError as e:
        print(f"{Fore.RED}Keyring error: {e}{Style.RESET_ALL}")

    # If not found, prompt the user to enter the API key
    print("OpenAI API key not found.")
    api_key = input("Enter your OpenAI API key: ").strip()

    # Ask if the user wants to store the API key securely
    save_key = input("Would you like to save the API key securely for future use? (y/n): ").strip().lower()
    if save_key == 'y':
        try:
            keyring.set_password("ai_commit_tool", "OPENAI_API_KEY", api_key)
            print("API key saved securely.")
        except keyring.errors.KeyringError as e:
            print(f"{Fore.RED}Failed to save API key to keyring: {e}{Style.RESET_ALL}")
            print("The API key will not be stored and must be entered each time.")

    return api_key

# Load the API key and create the OpenAI client
api_key = load_api_key()
client = OpenAI(api_key=api_key)

# function to allow users to update api key
def update_api_key():
    from getpass import getpass

    api_key = input("Enter your new OpenAI API key: ").strip()
    if not api_key:
        print("No API key entered. Exiting.")
        return

    try:
        # Remove any existing API key entry before updating
        keyring.delete_password("ai_commit_tool", "OPENAI_API_KEY")
    except keyring.errors.PasswordDeleteError:
        pass  
    try:
        # sets the new API key
        keyring.set_password("ai_commit_tool", "OPENAI_API_KEY", api_key)
        print("API key updated successfully.")
    except keyring.errors.KeyringError as e:
        print(f"{Fore.RED}Failed to update API key in keyring: {e}{Style.RESET_ALL}")





# filters git diff so it only runs code changes through AI
def filter_file_type():
    # common code file types. add your own as needed
    file_types = [".py", ".html", ".css", ".js",".ts", ".java", ".php", ".cs", ".md"]

    # get the names of all staged files
    result = subprocess.run(["git", "diff", "--cached", "--name-only"], capture_output=True, text=True)
    files = result.stdout.splitlines()

    # filter files to include only those with code file extensions
    code_files = [f for f in files if any(f.endswith(ext) for ext in file_types)]
    return code_files
    
# function to get the git diff output
def get_git_diff():

    # gets only staged code files
    code_files = filter_file_type()
    if not code_files:
        print("No code files changed.")
        return None
    
    # captures the output of the git message
    result = subprocess.run(["git", "diff", "--cached", "-b", "--"] + code_files, capture_output=True, text=True)
    diff_output = result.stdout

    # lists to store git diff changes
    added_line = []
    removed_lines = []
    

    # checks to make sure file has active Git or not
    if result.returncode == 0:
        print("Git status command ran successfully.")
        #print(result.stdout)
    else:
        print("Error running git status command.")
        print(result.stderr)  # to see the error message
    

    for line in diff_output.splitlines():

        #print(f"here are the lines: {line}")
        if line.startswith("+") and not line.startswith ("+++"):
            added_line.append(line[1:])
        if line.startswith("-") and not line.startswith ("---"):
            removed_lines.append(line[1:])
        # removes any metadata not related to the commit
        if line.startswith("+++") or line.startswith("---") or line.startswith("@@"):
            continue
          
    # checks if anything has been changed
    if len(added_line) == 0 and len(removed_lines) == 0:
        return None
    else:
        # formats the output of added and removed lines
        whats_changed = f"\n---- SUMMARY OF CHANGES ----\nAdded: {added_line} \n" + f"\nRemoved: {removed_lines}"

        # displays whats been added and removed
        print(whats_changed)
        return whats_changed


# function to generate commit message using gpt-3.5-turbo
def generate_commit_message(diff_text):
    prompt = f"Generate a concise, specific, easily understandable Git commit message describing these exact changes:\n{diff_text}"
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        # extract and return the generated message text
        commit_message = response.choices[0].message.content.strip()
        return commit_message
    
    except Exception as e:
        print(f"{Fore.RED}Error generating commit message: {e}{Style.RESET_ALL}")
        return None


# to start virtual enviroment --- venv\Scripts\activate
