import_string = \
'''
from pathlib import Path
from tqdm import tqdm
import mmap
import os
'''

### LINK START! (https://github.com/evnchn/linkstart.py)
for line in import_string.splitlines():
    if "import" in line:
        print(line)
        try:
            exec(line)
        except:
            if "#" in line:
                package_name = line.split("#")[-1]
            else:
                splits = line.split("import")
                if "from" in line:
                    package_name = splits[0].replace("from","")
                else:
                    package_name = splits[1]
            package_name = package_name.strip()
            print("Installing {}...".format(package_name))    
            import subprocess
            import sys
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            try:
                exec(line)
            except:
                print("Failed to install {}".format(package_name))
### DONE

target_string = b'Use the fact given above to evaluate the integral' ### EDIT THIS!

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear') # https://stackoverflow.com/a/2084628

matches = []
print("Generating file list...")
file_list = []
while not file_list:
    file_list = list(Path('recollection').glob('**/*.*'))
    if file_list:
        break
    clear_console()
    try:
        os.mkdir("recollection")
    except:
        pass
    print("1. Download zip from https://github.com/openwebwork/webwork-open-problem-library")
    print("2. Extract the 'OpenProblemLibrary' folder, ")
    print("3. Place said folder into 'recollection' folder which has been generated for you")
    input()

print("Looking for", strtarget_string)
for file_path in tqdm(file_list):
    try:
        with open(file_path, 'rb', 0) as file, mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s: 
            # https://stackoverflow.com/a/4944929
            if s.find(target_string) != -1: 
                file_path = os.path.abspath(file_path)
                print(file_path)
                matches.append(file_path)
    except Exception as e:
        #print(e)
        pass
        
clear_console()
print("---RESULTS---")
for match in matches:
    print(match)
