# file to rename files in a directory
import os
for i in range(41,51):
    old_name = r"Data/Test_data/Image_"+str(i)+".jpg"
    new_name = r"Data/Test_data/Image_"+str(i-40)+".jpg"
    os.rename(old_name, new_name)

