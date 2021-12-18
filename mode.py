import csv
from collections import Counter
with open("heightweight.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)
#print(file_data)

new_data=[]
for i in range(len(file_data)):
    m_num=file_data[i][1]
    new_data.append(float(m_num))

data=Counter(new_data)
mode_data={
    '50-60':0,
    '60-70':0,
    '70-80':0
}
for height,occurence in data.items():
    