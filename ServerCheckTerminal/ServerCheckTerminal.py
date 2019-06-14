while True: #allows for the restart of the program without exiting and manually executing again
#-----------------------------------------------------------------------------------------------
    import os #to navigate the file system
    import sys #to save output as txt
    from pathlib import Path #to show the file path
#------------------------------------------------------------------------------------------------
    #goes through the machine's entire directory and prints it in a hierarchy layout
    def list_files(startpath):
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            print('{}{}/'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print('{}{}'.format(subindent, f))

    #compares the captured logs of the 2 systems
    def compare(File1,File2):
        with open(File1,'r') as f:
            d=set(f.readlines())
        with open(File2,'r') as f:
            e=set(f.readlines())
        open('results.txt','w').close() #Create the file
        with open('results.txt','a') as f:
            for line in list(d-e):
               f.write(line)

    #captures the system
    def redirect_to_file1(text):
        original = sys.stdout
        sys.stdout = open('output1.txt', 'w')
        list_files('C:\\')
        sys.stdout = original

    #captures the system
    def redirect_to_file2(text):
        original = sys.stdout
        sys.stdout = open('output2.txt', 'w')
        list_files('C:\\')
        sys.stdout = original

    def pathFinder(filename):
        script_location = Path(__file__).absolute().parent
        my_file = script_location / 'filename'
        print(my_file)
    
    #main method------------------------------------------------------------------------------------------------------------------
    def main():
        choice = input("What do you want to run?\nc - capture\nl - list files\ns - check two servers directory logs\nx - quit\n")
        if choice == 'c':
            server = input("Enter 1 for the original server or 2 for the new server:\n")
            if server == '1':
                redirect_to_file1(list_files('C:\\'))
            if server == '2':
                redirect_to_file2(list_files('C:\\'))
        if choice == 'l':
            list_files("C:\\")
        if choice == 's':
            compare('output1.txt', 'output2.txt')
            answer = input('Would you like to view the missing files and directories? (y/n): ')
            if answer == 'y':
                file = open('results.txt', 'r')
                print(file.read())
            if answer == 'n':
                print("The file can be found at" + pathFinder('results.txt') + "for later viewing.")
        if choice == 'x':
            exit
    #initialize the program
    main()
#-------------------------------------------------------------------------------------------------------
    while True:
        answer = input('Would you like to return to the menu? (y/n): \n')
        if answer in ('y', 'n'):
            break
        print('Invalid input. Enter y to continue or n to terminate.')
    if answer == 'y':
        continue
    else:
        print('Have a great day.')
        break