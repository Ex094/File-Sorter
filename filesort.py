import os, shutil

###Path where the script is located
###Do not change anything
path = os.path.dirname(os.path.abspath("filesort.py"))
files = os.listdir(path)


###Extensions and their respective folder
###names
extension = {'Text': '.txt', 'Executables': '.exe', 'Python Executable': '.py'}

###Check if folder is not empty
if (files == 0):
    print "No files found in this directory"
    
else:

    ###Create Folders
    for name in extension:
        try:
            os.makedirs(name)

    ###If Folder already exists then ignore
        except:
            pass
        
    for ex in extension:
            for item in files:
                if item.endswith(extension[ex]):
                    try:

                        ###If Folder exists then move file
                        if os.path.isdir(ex):
                            shutil.move(item, ex)

                        ###Else create folder then move file
                        else:
                            os.makedirs(ex)
                            shutil.move(item, ex)

                    ###Error handler in case if files already exist
                    except:
                        print "Files And Folders have been sorted already!"
                        break
