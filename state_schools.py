from bs4 import BeautifulSoup
import os
import requests

def generate_school_list_by_state(state_list_file):
    with open(state_list_file, 'r') as file:
        state_list = file.readlines()
        for state in state_list:
            state = state.strip()
            state_format = "-".join(state.split(" ")).lower()
            url = f"https://www.4icu.org/us/{state_format}/a-z/"
            print(url)
            res = requests.get(url)
            soup = BeautifulSoup(res.text, 'lxml')
            tbody = soup.find("tbody")

            a = tbody.find_all("a")
            state_file = f"states/{state}/{state}.txt"
            # Create folder
            os.makedirs(os.path.dirname(state_file), exist_ok=True)

            with open(state_file, 'w') as out:
                for tag in a[:-1]:
                    out.write(tag.text + "\n")
