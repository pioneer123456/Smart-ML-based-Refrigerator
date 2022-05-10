import csv
f = open('Data/train_data.csv', 'w')
csv_w = csv.writer(f)

header = ["filename", "label"]

csv_w.writerow(header)
for i in range(1,41):
    temp = []
    temp.append("Image_"+str(i)+".jpg")
    temp.append("looks_good")
    csv_w.writerow(temp)
for i in range(41,81):
    temp = []
    temp.append("Image_"+str(i)+".jpg")
    temp.append("looks_defected")
    csv_w.writerow(temp)
f.close()
