# #!/usr/bin/env python3
# import os

# def getListOfFiles(dirName):
#     listOfFile = os.listdir(dirName)
#     allFiles = list()
#     for entry in listOfFile:
#         if os.path.isdir(fullPath):
#             allFiles = allFiles + getListOfFiles(fullPath)
#         else:
#             allFiles.append(fullPath)
                
#     return allFiles        
 
 
# def test_scaffolded_directories_and_files():
#     dirName = './';

#     expectedList = ["./requirements.txt",
#         "./sample.py",
#         "./.pytest_cache/CACHEDIR.TAG",
#         "./.pytest_cache/README.md",
#         "./.pytest_cache/.gitignore",
#         "./.pytest_cache/v/cache/nodeids",
#         "./.pytest_cache/v/cache/lastfailed",
#         "./.pytest_cache/v/cache/stepwise",
#         "./__pycache__/sample.cpython-37-pytest-5.3.2.pyc"]
    
#     listOfFiles = list()
#     for (dirpath, dirnames, filenames) in os.walk(dirName):
#         listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    
#     assert listOfFiles == expectedList    
#     

def test_sample():
    assert False