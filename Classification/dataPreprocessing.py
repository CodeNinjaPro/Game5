import csv
import epitran
epi = epitran.Epitran('sin-Sinh')

data = []
data2 = []

with open("data/final_a.csv", "r") as f:
    reader = csv.reader(f, delimiter="\t")
    for i, line in enumerate(reader):
        data.append('"' + epi.transliterate(line[0].replace('"', '')) + '"')
        # data.append(line[0].replace('"', ''))

with open("data/final_b.csv", "r") as f:
    reader = csv.reader(f, delimiter="\t")
    for i, line in enumerate(reader):
        data2.append(line[0] + '\n')
        # data.append(line[0].replace('"', ''))


#
f = open("data/final.dat", "a")
# f.write("Question,Category\n")
for i in range(len(data)):
    print(data[i])
    f.write(data[i]+','+data2[i])
f.close()
