from hamcrest import *
import unittest
import os

def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles        
 
def expected_list_of_files():
	return ['../test/sample.py',
			'../test/test_api.py',
			'../build.yml']
	
def test_scaffolded_directories_and_files():
	dirName = '../';
	 
	listOfFiles = list()
	for (dirpath, dirnames, filenames) in os.walk(dirName):
		listOfFiles += [os.path.join(dirpath, file) for file in filenames]
	
	for file in expected_list_of_files():
		assert_that(listOfFiles, has_item(file))		


# def test_compare_list_of_items():
# 	actual_list_of_items = ['a','b','c']
# 	expected_list_of_items = ['a']

# 	for item in ['b','d']:
# 		assert_that(actual_list_of_items, has_item(item)) 