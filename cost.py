from io import StringIO
from helper_methods import format_string_list
import csv
COST_TABLE_XPATH_TEMPLATE = "/html/body/table[14]/tbody"
DELIMITER = "|"

def pretty_cost_string(csv_string, delimiter):
    ans = []
    for line in csv_string.split("\r\n"):
        if (line == ""): continue
        (category, onCam, offCam, home) = line.split(delimiter)
        ans.append(f"{category:<34}|{onCam:^12}|{offCam:^12}|{home:^12}")
    return "\r\n".join(ans)

def scrape_cost_info(tree):
    csv_string = StringIO()
    w = csv.writer(csv_string, delimiter=DELIMITER)
    # Cost Table Xpath may slips around
    table = ""
    for table_index in range(10, 20):
        cost_table_xpath = f"/html/body/table[{table_index}]/tbody"
        table = tree.xpath(cost_table_xpath + "//text()")
        table = format_string_list(table)
        if len(table) > 20 and table[:13] == "Cost Category":
            break

    temp = []
    for i, line in enumerate(table.split("\r\n")):
      temp.append(line)
      if (i % 4 == 3):
          w.writerow(temp)
          temp = []
    table_string = pretty_cost_string(csv_string.getvalue(), DELIMITER)
    # print(table_string)
    return table_string
