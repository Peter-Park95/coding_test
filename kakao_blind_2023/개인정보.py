from datetime import datetime
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
t = dict()
for term in terms: 
    key, value = term.split()
    t[key] = value
for idx, privacy in enumerate(privacies):
    p_date, p_type = privacy.split()
    print(datetime.strptime(p_date, "%Y.%m.%d"))