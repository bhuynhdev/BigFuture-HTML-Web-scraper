import requests
import re
import csv
from bs4 import BeautifulSoup
import html5lib
from general import scrape_general_info
from admission import scrape_admission_info
from deadline import scrape_deadline_info
from testscore import scrape_testscore_info
from cost import scrape_cost_info
from international_finaid import scrape_finaid_info
from helper_methods import csv_to_xlsx

from consts import FIELD_NAMES, BIGFUTURE_URL, BIGFUTURE_PRINT_URL

def get_id(college_name):
    college_name_URL = "-".join(college_name.split(" ")).lower();
    scraper_URL = BIGFUTURE_URL + college_name_URL
    # Get the hidden college Id code
    res = requests.get(scraper_URL)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    pattern = re.compile(r'"org.collegeboard.pacollegeplan.shared.dto.content.PageBaseMetadataDto\/2239360936\\",\\"(\d+)', 
        re.MULTILINE | re.DOTALL)

    script = soup.find("script", text=pattern)
    id_okay = False
    id = 0
    if script:
        match = pattern.search(script.string)
        if match:
            id = match.group(1)
            id_okay = True
    if (id_okay):
        print(f"{college_name}, id = {id}")
    else:
        print(f"Incorrect school name '{college_name}'")

    return (id, id_okay)

def scrape_routine(college_name, additional_info):
    
    college_id, id_okay = get_id(college_name)
    school = dict()
    if (id_okay):
        print_URL = BIGFUTURE_PRINT_URL + "?id=" + college_id
        res = requests.get(print_URL)
        etree = html5lib.parse(res.text, treebuilder='lxml', namespaceHTMLElements=False)

        (SAT_range, ACT) = scrape_testscore_info(etree)

        admission = scrape_admission_info(etree)

        cost_table = scrape_cost_info(etree) # Table as a string
        
        (address, setting, facts) = scrape_general_info(etree)

        (general_deadline, ea_ed_deadline) = scrape_deadline_info(etree)

        finaid = scrape_finaid_info(etree)

        school['Name'] = college_name
        school['Address'] = address
        school['Setting'] = setting
        school['Quick facts'] = facts
        school['RD deadlines'] = general_deadline
        school['EA/ED deadlines'] = ea_ed_deadline
        school['SAT range'] = SAT_range
        school['ACT range'] = ACT
        school['Costs'] = cost_table
        school['International Fin Aid'] = finaid
        school['Admission'] = admission
    else:
        print(f"Incorrect school name '{college_name}'. {additional_info}")

    return school

if __name__ == "__main__":
    with open('custom_schools.csv', 'w', encoding='utf-8-sig', newline='') as result_file:
        writer = csv.DictWriter(result_file, fieldnames=FIELD_NAMES)
        writer.writeheader()
        with open('custom_names.txt') as names:
            for index, line in enumerate(names):
                print(f"{index + 1}.", end="")
                school_info = scrape_routine(line.strip(), f"Line {index + 1}")
                writer.writerow(school_info)

    csv_to_xlsx("custom_schools.csv", "custom_schools.xlsx")