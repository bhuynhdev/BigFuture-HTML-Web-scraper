from scraper import scrape_routine, get_id
from state_schools import generate_school_list_by_state
from consts import FIELD_NAMES
from helper_methods import csv_to_xlsx
import csv
import os
import openpyxl

def generate_path(state_name):
    folder_path = f"states/{state_name}"
    csv_path = os.path.join(folder_path, f"{state_name}.csv")
    xlsx_path = os.path.join(folder_path, f"{state_name}.xlsx")
    school_list_path = os.path.join(folder_path, f"{state_name}.txt")
    return (folder_path, csv_path, xlsx_path, school_list_path)

def generate_csv_single_state(state):
    csv_path = generate_path(state)[1]

    with open(csv_path, 'w', encoding='utf-8-sig', newline='') as result_file:
        writer = csv.DictWriter(result_file, fieldnames=FIELD_NAMES)
        writer.writeheader()
        school_list_path = generate_path(state)[3]
        with open(f"states/{state}/{state}.txt") as names:
            for index, line in enumerate(names):
                print(f"{index + 1}. {line.strip()}")
                school_info = scrape_routine(line.strip(), f"File {school_list_path}, Line {index + 1}")
                writer.writerow(school_info)

def generate_csv_many_states(state_list_file):
    with open(state_list_file) as file:
        state_list = file.readlines()
        for state in state_list:
            print(state)
            state = state.strip()
            generate_csv_single_state(state)
            print("-" * 10)

def generate_xlsx_single_state(state):
    csv_path = generate_path(state)[1]
    xlsx_path = generate_path(state)[2]
    csv_to_xlsx(csv_path, xlsx_path)

def generate_xlsx_many_states(state_list_file):
    with open(state_list_file) as file:
        state_list = file.readlines()
        for state in state_list:
            state = state.strip()
            generate_xlsx_single_state(state)

def id_validation(state):
    school_list_path = generate_path(state)[3]
    with open(school_list_path) as file:
        school_list = file.readlines()
        for school in school_list:
            state = school.strip()
            get_id(state)

if __name__ == "__main__":
    # test_state = "Delaware"
    # id_validation(test_state)
    # generate_csv_single_state(test_state)
    # generate_xlsx_single_state(test_state)

    # generate_csv_many_states("stateList2.txt")
    # generate_xlsx_many_states("stateList.txt")