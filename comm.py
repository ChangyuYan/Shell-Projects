#!/usr/bin/python

'''
 Author: Changyu Yan
 Student ID: 304-566-451
'''
# Implements the POSIX comm command without the environmental variables 

import sys # So that we can feed this program parameters from the Linux shell

def comm_no_u(list1, list2):
    # The goal of this function is to output the result of 
    # $ comm file1 file2
    # list1 and list2 are just lists of lines from file1 and file2
    
    
    
    # We first put every element from list1 and list2 in total,
    # with duplicated elements only appear once
    total = list(sorted(set(list1 + list2)))
    # However, we need to consider duplicated elements
    toAdd = []
    for word in total:
        if list1.count(word) > 1 or list2.count(word) > 1:
            for i in range( max(list1.count(word), 
                                list2.count(word)) - 1 ):
                toAdd.append(word)
    total += toAdd
    total.sort()
    
    # Initialize the columns:
    result = [[], [], []]
    
    # Now we "compare" the words and put the results into 3 columns:
    for word in total:
        if word in list1:
            if word in list2:
                result[0].append('\t')
                result[1].append('\t')
                result[2].append(str(word))
                list1.remove(word)
                list2.remove(word)
            else:
                result[0].append(str(word))
                result[1].append("")
                result[2].append("")
                list1.remove(word)
        else:
            result[0].append('\t')
            result[1].append(str(word))
            result[2].append("")
            list2.remove(word)
    

    # Now we choose which columns to display based on input options
    display(result)
     

def display(result):
    # Input result should have 3 sub-lists/columns
    if '-1' in sys.argv:
        result[0] = None
    if '-2' in sys.argv:
        result[1] = None
    if '-3' in sys.argv:
        result[2] = None
    
    while None in result:
        result.remove(None)
    
    if len(result) == 0 or len(result[0]) == 0:
        sys.exit()
    
    for i in range(len(result[0])):
        if len(result) == 1:
            k = result[0][i]
        elif len(result) == 2:
            k = result[0][i] + result[1][i]
        elif len(result) == 3:
            k = result[0][i] + result[1][i] + result[2][i]
        if k!= '' and k!= '\t' and k!='\t\t' and k!= '\n':
            print k
    # Note: If one of the element was originally a new line or two tabs or an empty string, then this fails... 


def comm_u(list1, list2):
    result = [[],[],[]]
    list1_copy = list1[:]
    for word in list1_copy:
        if word in list2:
            result[0].append('\t')
            result[1].append('\t')
            result[2].append(str(word))
            list1.remove(word)
            list2.remove(word)
        else:
            result[0].append(str(word))
            result[1].append("")
            result[2].append("")
            list1.remove(word)

    list2_copy = list2[:]
    for word in list2_copy:
        result[0].append('\t')
        result[1].append(str(word))
        result[2].append("")
        list2.remove(word)
        
    display(result)    

def main():
    n = len(sys.argv)
    
    if sys.argv[n-2] == '-' and sys.argv[n-1] == '-':
        sys.exit("Error: Cannot have both files be input as '-' ")
    elif sys.argv[n-2] == '-':
        list1 = sys.stdin.read().splitlines()
        file2 = open(sys.argv[n-1], 'r')
        list2 = file2.read().splitlines()
    elif sys.argv[n-1] == '-':
        list2 = sys.stdin.read().splitlines()
        file1 = open(sys.argv[n-2], 'r')
        list1 = file1.read().splitlines()
    else:    
        file1 = open(sys.argv[n-2], 'r')
        file2 = open(sys.argv[n-1], 'r')
        list1 = file1.read().splitlines()
        list2 = file2.read().splitlines()

    if sys.argv[1] != '-u':
        comm_no_u(list1, list2)
        
    elif sys.argv[1] == '-u':
        comm_u(list1, list2)
    

if __name__ == "__main__":
    main()
