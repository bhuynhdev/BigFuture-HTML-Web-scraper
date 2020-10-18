ADDRESS_SECTION_XPATH = "/html/body/table[2]/tbody/tr[1]/td[1]"
SETTING_SECTION_XPATH = "/html/body/table[2]/tbody/tr[4]/td"
QUICK_FACTS_SECTION_XPATH = "/html/body/table[2]/tbody/tr[2]/td[2]"

from helper_methods import format_string_list

def scrape_general_info(tree):
	resultList = []
	for path in (ADDRESS_SECTION_XPATH, SETTING_SECTION_XPATH, QUICK_FACTS_SECTION_XPATH):
		section = tree.xpath(path + "//text()")
		resultList.append(format_string_list(section))
	return resultList
