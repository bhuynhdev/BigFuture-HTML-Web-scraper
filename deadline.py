DEADLINE_SECTION_XPATH = "/html/body/table[3]/tbody"

"/html/body/table[3]/tbody/tr[1]/td/h2"
"/html/body/table[3]/tbody/tr[1]/td"

from helper_methods import format_string_list

def scrape_deadline_info(tree):
    resultList = []
    for i in range(2):
        # i = 0 --> Getting RD deadlines
        # i = 1 --> Getting EA/ED deadlines
        subsection_xpath = DEADLINE_SECTION_XPATH + f"/tr[{i + 1}]/td"
        subsection_header_xpath = subsection_xpath + "/h2"
        subsection_header = tree.xpath(subsection_header_xpath + "//text()")[0]

        if subsection_header in ("Admission", "Early Decision And Action"):
            subsection = tree.xpath(subsection_xpath + "//text()")
            resultList.append(format_string_list(subsection))
    if len(resultList) == 1:
        resultList.append("")
    return resultList