from helper_methods import format_string_list

SCORE_SECTION_XPATH_TEMPLATE = "/html/body/table[10]/tbody"
"/html/body/table[10]/tbody/tr[1]/td[1]/h2"

def generate_score_range(SAT_Math, SAT_Reading, ACT):
    SAT_range = ""
    if (len(SAT_Math) == 9 and len(SAT_Reading) == 9):
        SAT_range = str(int(SAT_Math[:3]) + int(SAT_Reading[:3])) \
                    + " - " \
                    + str(int(SAT_Math[-3:]) + int(SAT_Reading[-3:]))
    else:
        SAT_range = "No information"

    if len(ACT) != 7:
        ACT = "No information"

    return (SAT_range, ACT)

def scrape_testscore_info(tree):
    resultList = []
    table_index = 0
    for table_index in range(8, 18):
        table_xpath = f"/html/body/table[{table_index}]/tbody"
        test_subject_header_xpath = table_xpath + "/tr[1]/td[1]/h2//text()"
        header = tree.xpath(test_subject_header_xpath)
        if len(header) > 0 and header[0] == "Test Subjects":
            break;


    for i in range(3):
        # i = 0 ==> Getting SAT Math range
        # i = 1 ==> Getting SAT Reading range
        # i = 2 ==> Getting ACT range
        score_section_xpath = f"/html/body/table[{table_index}]/tbody"
        score_detail_xpath = score_section_xpath + f"/tr[{i + 2}]/td[2]/p"
        score_detail = tree.xpath(score_detail_xpath)[0].text.strip()
        resultList.append(score_detail)
        # print(score_detail)

    scores = generate_score_range(*resultList)
    return scores