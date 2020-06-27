import pandas as pd
import os
import csv
import shutil as sh

NUMS={
"Swiping Left":0,
"Swiping Right":0,
"Swiping Down":0,
"Swiping Up":0,
"Pushing Hand Away":0,
"Pulling Hand In":0,
"Sliding Two Fingers Left":0,
"Sliding Two Fingers Right":0,
"Sliding Two Fingers Down":0,
"Sliding Two Fingers Up":0,
"Pushing Two Fingers Away":0,
"Pulling Two Fingers In":0,
"Rolling Hand Forward":0,
"Rolling Hand Backward":0,
"Turning Hand Clockwise":0,
"Turning Hand Counterclockwise":0,
"Zooming In With Full Hand":0,
"Zooming Out With Full Hand":0,
"Zooming In With Two Fingers":0,
"Zooming Out With Two Fingers":0,
"Thumb Up":0,
"Thumb Down":0,
"Shaking Hand":0,
"Stop Sign":0,
"Drumming Fingers":0,
"No gesture":0,
"Doing other things":0
}

def read_csv(path):
    csv = pd.read_csv(path,header=None)
    return csv

def delete_odd_images():
    for i,sample_folder in enumerate(os.listdir("/media/erhan/ext/27Class/")):
        images=sorted(os.listdir("/media/erhan/ext/27Class/"+sample_folder))
        print(i)
        for i in range(len(images)):
           if(i%2!=0 or i>22):
                os.remove("/media/erhan/ext/27Class/"+sample_folder+"/"+images[i])

def count_under():
    count=0
    for i,sample_folder in enumerate(os.listdir("/media/erhan/ext/20bn-jester-v1/")):
        images=sorted(os.listdir("/media/erhan/ext/20bn-jester-v1/"+sample_folder))
        if len(images)<23:
            print(sample_folder)
            count+=1
    print(count)



def move_folders(csv_dir_names):
    min=0
    for sample_folder_name in csv_dir_names:
        sh.move("/media/erhan/ext/20bn-jester-v1/"+str(sample_folder_name),"/media/erhan/ext/27Class/"+str(sample_folder_name))
        min+=1
        print(min)


def csv_olustur(full_csv):
    counter=0
    with open('/media/erhan/ext/csv/27Class23BFrame/valid.csv', 'w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in full_csv.iterrows():
            dir=str(row[1].values[0])
            label=str(row[1].values[1])
            if len(os.listdir("/media/erhan/ext/20bn-jester-v1/" +dir))>=23:
                writer.writerow([dir,label])
                counter+=1
                print(counter)






#csv_train = read_csv("/media/erhan/ext/csv/jester-v1-validation.csv")
#csv_olustur(csv_train)

count_under()


csv_train = read_csv("/media/erhan/ext/csv/27Class23BFrame/train.csv")
csv_valid = read_csv("/media/erhan/ext/csv/27Class23BFrame/valid.csv")
delete_odd_images()


#move_folders(csv_f[0].values)

