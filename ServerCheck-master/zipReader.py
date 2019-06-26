from zipfile import ZipFile #to manage the zip file
import datetime #for date modified
import sys

def main():
    # specifying the zip file name, getting input from user
    file_name = input("Enter the filename: \n")
    redirect_to_file(zipRead(file_name))
        

def zipRead(file_name):
    # opening the zip file in READ mode to gather data
    with ZipFile(file_name, 'r') as zip: 
        for info in zip.infolist(): 
                print(info.filename) 
                print('\tModified:\t' + str(datetime.datetime(*info.date_time))) 
                print('\tCompressed:\t' + str(info.compress_size) + ' bytes') 
                print('\tUncompressed:\t' + str(info.file_size) + ' bytes') 

def redirect_to_file(text):
        original = sys.stdout
        sys.stdout = open('zipProperties.txt', 'w')
        sys.stdout = original

main()