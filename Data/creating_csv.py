import csv
f = open('Data/test_data.csv', 'w')
csv_w = csv.writer(f)

header = ["filename", "label"]

csv_w.writerow(header)
for i in range(1,11):
    temp = []
    temp.append("Image_"+str(i)+".jpg")
    temp.append("looks_good")
    csv_w.writerow(temp)
for i in range(11,21):
    temp = []
    temp.append("Image_"+str(i)+".jpg")
    temp.append("looks_defected")
    csv_w.writerow(temp)
f.close()
