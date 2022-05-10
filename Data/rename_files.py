# file to rename files in a directory
import os
for i in range(1,11):
    old_name = r"data/rotten_banana_fruit/Image_"+str(i)+".jpg"
    new_name = r"data/rotten_banana_fruit/Image_"+str(i+10)+".jpg"
    os.rename(old_name, new_name)

