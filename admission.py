from helper_methods import format_string_list

ADMISSION_SECTION_XPATH = "/html/body/table[8]/tbody/tr[1]/td[1]"

def scrape_admission_info(tree):
    admission = tree.xpath(ADMISSION_SECTION_XPATH + "//text()")
    admission = format_string_list(admission)
    # print(admission)
    return admission
