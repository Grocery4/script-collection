import os
from datetime import datetime

def main():
    rootdir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(rootdir)
    
    print(f"Root directory: {rootdir}")

    try:
        # Collect directories to rename
        rename_list = []
        for rootdir, dirs, files in os.walk(rootdir):
            for subdir in dirs:
                try:
                    # Check if the directory is already in the correct format
                    datetime.strptime(subdir, "%Y-%m-%d")
                except ValueError:
                    # Add to rename list if not in the correct format
                    rename_list.append((rootdir, subdir))

        # Rename directories after collecting them
        for root, subdir in rename_list:
            try:
                # Attempt to parse the directory name in d-m-y format
                try:
                    new_name = datetime.strptime(subdir, '%d-%m-%Y').strftime('%Y-%m-%d')
                except ValueError:
                    # If d-m-y fails, try m-d-y format
                    new_name = datetime.strptime(subdir, '%m-%d-%Y').strftime('%Y-%m-%d')
                
                os.rename(os.path.join(root, subdir), os.path.join(root, new_name))
                print(f"Wrong format detected! Renaming {subdir} to {new_name}.\n")
            except ValueError:
                print(f"Skipping {subdir}: Incorrect format for conversion.")
            except Exception as e:
                print(f"Error renaming {subdir}: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")
    
    finally:
        input('Press any key to stop..')
    
main()
