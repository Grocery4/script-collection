import os
from datetime import datetime

def main():

    rootdir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(rootdir)
    
    print(rootdir)

    try:
        for rootdir, dirs, files in os.walk(rootdir):
            for subdir in dirs:
                try:
                    datetime.strptime(subdir, "%Y-%m-%d")
                #incorrect format code
                except ValueError:
                    new_name = datetime.strptime(subdir,'%d-%m-%Y').strftime('%Y-%m-%d')
                    os.rename(subdir, new_name)
                    print("Wrong format detected! Renaming " + subdir + " to " + new_name + ".\n")
                #correct format
                else:
                    print(subdir + " already in correct format.")

    except Exception as e:
        print(e)
    
    finally:
        input('Press any key to stop..')
    
main()
