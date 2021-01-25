import csv
with open("finds.csv") as find:
    reader = csv.reader(find)
    data = list(reader)
data
len(data)
h = ['0', '0', '0', '0', '0', '0']
for row in data:
    if row[-1] == "Yes":
        j = 0
        for col in row:
            if col != 'Yes':
                if col != h[j] and h[j] == '0':
                    h[j] = col
                if col != h[j] and h[j] != '0':
                    h[j] = '?'        
            j = j+1
    print(h)       
print(" the Maximal specific :", h)
