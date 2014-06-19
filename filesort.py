import os, shutil, sys

###Extensions and their respective folder names
extension = {'Text': '.txt', 'Executables': '.exe', 'Python Executable': '.py'}


def file_sort(path):
    ###Path where the script is located
    files = os.listdir(path)

    ###Check if folder is not empty
    if (files == 0):
        print "No files found in this directory"

    else:
        for ex in extension:
            for item in files:
                if item.endswith(extension[ex]):
                    try:

                        ###If Folder exists then move file
                        if os.path.isdir(path + ex):
                            shutil.move(path + item, path + ex)

                        ###Else create folder then move file
                        else:
                            os.makedirs(path + ex)
                            shutil.move(path + item, path + ex)

                    ###Error handler in case if files already exist
                    except:
                        print "Files And Folders have been sorted already!"
                        break


try:
    if(sys.argv[1]):
        if(os.path.isdir(sys.argv[1])):
           print "Sorting files in defined path: " + sys.argv[1]
           file_sort(sys.argv[1])
           
        else:
           print "Directory does not exist"
except:
    print "No Directory or Path Defined!"
    print "Command: filesort.py C:/folder/folder"
