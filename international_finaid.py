from helper_methods import format_string_list

"/html/body/table[15]/tbody/tr[3]/td/h2"

FINAID_SECTION_XPATH_TEMPLATE = "/html/body/table[17]/tbody/tr[3]/td"

def scrape_finaid_info(tree):
    # Financial aid section may move around quite a lot
    # Check for h2:
    table_index = 0
    for table_index in range(11, 20):
        header_xpath = f"/html/body/table[{table_index}]/tbody/tr[3]/td/h2"
        header = tree.xpath(header_xpath + "//text()")
        if len(header) > 0 and header[0] == "Financial Aid":
            break;

    finaid_section_xpath = f"/html/body/table[{table_index}]/tbody/tr[3]/td"
    finaid = tree.xpath(finaid_section_xpath + "//text()")
    finaid = format_string_list(finaid)
    # Check if what we get is what we want
    if finaid[:13] != "Financial Aid":
        finaid = ""
    return finaid
