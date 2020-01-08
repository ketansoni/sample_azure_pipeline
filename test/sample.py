from hamcrest import *
import os

def create_data_product(bash, command, *args):
	bash.run_script(command, *args)

def get_list_of_files(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        if os.path.isdir(fullPath):
            allFiles = allFiles + get_list_of_files(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles        
 
def expected_list_of_files():
	return ['../test/sample.py',
			'../test/test_api.py',
			'../build.yml']
	
def test_scaffolded_directories_and_files(bash):
	create_data_product(bash, '../sample.sh', ['testing'])
	dirName = '../';
	 
	actual_list_of_files = list()
	for (dirpath, dirnames, filenames) in os.walk(dirName):
		actual_list_of_files += [os.path.join(dirpath, file) for file in filenames]
	
	assert_that(actual_list_of_files, has_items(*expected_list_of_files()))