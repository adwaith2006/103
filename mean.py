import csv
with open("heightweight.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)
#print(file_data)

new_data=[]
for i in range(len(file_data)):
    m_num=file_data[i][1]
    new_data.append(float(m_num))

n=len(new_data)
total=0
for i in new_data:
    total+=i

mean=total/n

print('Mean of data is:'+ str(mean))
