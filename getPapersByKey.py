acl_key_path_2017 = "ACL\\KeyValue\\2017.txt"
acl_key_path_2018 = "ACL\\KeyValue\\2018.txt"
acl_key_path_2019 = "ACL\\KeyValue\\2019.txt"
acl_paper_path_2017 = "ACL\\txt\\paper_list_2017.txt"
acl_paper_path_2018 = "ACL\\txt\\paper_list_2018.txt"
acl_paper_path_2019 = "ACL\\txt\\paper_list_2019.txt"

icml_key_path_2017 = "ICML\\KeyValue\\2017.txt"
icml_key_path_2018 = "ICML\\KeyValue\\2018.txt"
icml_key_path_2019 = "ICML\\KeyValue\\2019.txt"
icml_paper_path_2017 = "ICML\\txt\\paper_list_2017.txt"
icml_paper_path_2018 = "ICML\\txt\\paper_list_2018.txt"
icml_paper_path_2019 = "ICML\\txt\\paper_list_2019.txt"



def getKeyPaperDict(key_txt_path, paper_txt_path):
    with open(key_txt_path, "r") as f:
        lines = f.read()[1:-2]
        lines = lines.replace("[", "").replace("]", "").replace("'", "")
        lines = lines.split(",")
        keys_arr = [item.strip() for i, item in enumerate(lines) if i % 2 == 0]
        f.close()

    with open(paper_txt_path, "r", encoding="utf-8") as f:
        lines = f.read()
        papers_arr = lines.split("\n")
        f.close()

    keyPaperDict = {}
    for key in keys_arr:
        paperArr = []
        for paper in papers_arr:
            if key.lower() in paper.lower() or key + "s" in paper.lower():
                paperArr.append(paper)
        keyPaperDict[key] = paperArr
    return keyPaperDict


acl_dict_2017 = getKeyPaperDict(acl_key_path_2017, acl_paper_path_2017)
acl_dict_2018 = getKeyPaperDict(acl_key_path_2018, acl_paper_path_2018)
acl_dict_2019 = getKeyPaperDict(acl_key_path_2019, acl_paper_path_2019)

icml_dict_2017 = getKeyPaperDict(icml_key_path_2017, icml_paper_path_2017)
icml_dict_2018 = getKeyPaperDict(icml_key_path_2018, icml_paper_path_2018)
icml_dict_2019 = getKeyPaperDict(icml_key_path_2019, icml_paper_path_2019)

print(acl_dict_2017)
print(acl_dict_2018)
print(acl_dict_2019)
print(icml_dict_2017)
print(icml_dict_2018)
print(icml_dict_2019)