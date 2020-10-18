import csv
import openpyxl

from consts import FIELD_NAMES

def format_multiline_string(bs4_string):
    lines = []
    for line in bs4_string.split("\n"):
        line = line.strip();
        if (line != ""):
            lines.append(line)
    multiline_string = "\r\n".join(lines)
    return multiline_string


def format_string_list(string_list):
    lines = []
    for line in string_list:
        line = line.strip()
        if (line != ""):
            lines.append(line)
    multiline_string = "\r\n".join(lines)
    return multiline_string

def csv_to_xlsx(csv_path, xlsx_path):
    wb = openpyxl.Workbook()
    ws = wb.active

    with open(csv_path) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            ws.append(row)

    wb.save(xlsx_path)