import os
import subprocess
import re

def find_files(dir,pattern):
    scriptDir = os.path.dirname(os.path.abspath(__file__))  # Directory of the script
    for filename in os.listdir(dir):
        if filename.endswith('.md'):  
            filePath = os.path.join(dir, filename)
            with open(filePath, 'r', encoding='utf-8') as file:
                content = file.read()
                file.seek(0)
            # Find all occurrences of the pattern
            matches = re.findall(pattern, content)
            if matches:
                relativePath = os.path.relpath(filePath, scriptDir)
                uniFiles.append(relativePath.replace("\\","/"))
                # make the page public
                if "public:: true" not in content:
                    content = "public:: true\n" + content
                    with open(filePath, 'w', encoding='utf-8') as file:
                        file.write(content)
                    
 
def find_missing():
    result = subprocess.run(["git", "uni", "ls-files", "--others", "--exclude-standard"], capture_output=True, text=True)
    if result.returncode == 0:
        untrackedFiles = result.stdout.splitlines()
    else:
        print("Command failed:", result.stderr.strip())
    
    untrackedFile_s = set(untrackedFiles)  # Convert one array to a set
    uniFiles_s = set(uniFiles)
    
    for untrackedFile in uniFiles_s & untrackedFile_s:   
        print(untrackedFile)
        result = subprocess.run(["git", "uni", "add", untrackedFile], capture_output=True, text=True)
        if result.returncode == 0:
            print("Command succeeded:", result.stdout.strip())
        else:
            print("Command failed:", result.stderr.strip())

pattern = r'tags::.*uni.*\nalias'
directory = "C:\\Users\\Matteo\\logseq\\pages"
uniFiles = []
find_files(directory, pattern)
find_missing()