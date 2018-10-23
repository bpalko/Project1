import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


inFile2 = open("P1DataB.csv", "r")
outfile = open("outfile.csv", "w")


def getData(file):
	inFile1 = open(file,"r")
	lines = inFile1.readlines()
	inFile1.close()
	dict_list = []
	for line in lines:
		init_data = {}
		f_line_list = line.split(",")
		
		
		
		
		first = f_line_list[0]
		last = f_line_list[1]
		email = f_line_list[2]
		c_year = f_line_list[3]
		dob = f_line_list[4]

		init_data["First"] = first
		init_data["Last"] = last
		init_data["Email"] = email
		init_data["Class"] = c_year
		init_data["DOB"]= dob
		dict_list.append(init_data)
	dict_list.remove(dict_list[0])
	return dict_list
	
	
	
# get a list of dictionary objects from the file
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows

	pass

def mySort(data,col):
	sortedlist = sorted(data, key=lambda l: l[col])
	return(sortedlist[0]["First"] + " " + sortedlist[0]["Last"])



# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName

	pass


def classSizes(data):
	list_students = []
	list_students.append(["Senior", 0])
	list_students.append(["Junior", 0])
	list_students.append(["Sophomore", 0])
	list_students.append(["Freshman", 0])

	for student in data:
		if student ["Class"] == "Senior":
			list_students[0][1] = list_students[0][1] + 1
		elif student["Class"] == "Junior":
			list_students[1][1] = list_students[1][1] + 1
		elif student["Class"] == "Sophomore":
			list_students[2][1] = list_students[2][1] + 1
		elif student["Class"] == "Freshman":
			list_students[3][1] = list_students[3][1] + 1
	tuples_list = []
	for x in list_students:
		grade = x[0]
		size = x[1]
		tuples_list.append((grade,size))
	return sorted(tuples_list, key= lambda l: l[1], reverse = True)
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	pass


def findMonth(a):
	m_dict = {}
	for x in a:
		student_month = x['DOB'].split('/')[0]
		if student_month not in m_dict:
			m_dict[student_month] = 1
		else:
			m_dict[student_month] = m_dict[student_month] + 1
	common = sorted(m_dict, key=lambda l: m_dict[l], reverse=True)
	common_int = int(common[0])
	return common_int
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data

	pass

def mySortPrint(a,col,fileName):
	sorted_list = sorted(a, key=lambda l:l[col])
	with open('results.csv', 'w') as look_for:
		for x in sorted_list:
			first = x["First"]
			last = x["Last"]
			email = x["Email"]
			outfile.write(first + "," + "last" + "," + email + '\n')
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written

	pass

def findAge(a):
	current_date = 2018
	total = 0
	for x in a:
		date_of_birth = x["DOB"]
		split_dob = date_of_birth.split('/')
		total = total + int(split_dob[2])
	avg_year_born = total/len(a)
	return int(current_date - avg_year_born)
	
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score 


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB2.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()




