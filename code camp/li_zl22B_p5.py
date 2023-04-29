# ==============================================================================
# PROGRAM   Simple DNA Sequences
#
# AUTHOR: Ziluo Li
# FSU MAIL NAME: zl22b
# RECITATION SECTION NUMBER: 0001
# RECITATION INSTRUCTOR NAME: Maitry Kamleshkumar Chauhan
# CGS 3465 - Fall 2022
# PROJECT NUMBER: 5
# DUE DATE: Thursday 11/12/2022
# PLATFORM: Windows OS / Python 3
# 
# SUMMARY
#First, read in a DNA sequence from a file, and store it in a Python string or list. Note: we will keep our 
#sequences very short, in comparison to DNA sequences in real life, to make programming and grading this 
#project simpler. Print the sequence you read in, to show the contents read in from the file. This is your 
#original DNA sequence. 
#Provide the user with a menu. The menu must allow the user to choose among four operations: 
#(1) Determine the complement of the original DNA sequence read in, and print both the original and the 
#complement in a parallel output format, for ease of comparison. 
#(2) Create 5 random simulated simple mutations in the DNA sequence. That is, in 5 positions your 
#program selects pseudo-randomly, insert an "M" into the position to replace the A, T, G or C that was 
#previously there. Then print both the original and the mutated sequence in parallel output format, again, for 
#ease of comparison.

## 
# INPUT 
# 
#The input files provided are named dna1.txt, dna2.txt and dna3.txt and are available from the course web 
#site. You may also make up your own text files to test. 
#You may assume that data files are not empty, do contain one DNA sequence, and do not contain any data 
#errors. 
#You must ask the user to input the filename they wish to use. If the file does not open with the filename 
#they entered, keep asking them for a filename until the file does open successfully.
# 
#   
# OUTPUT 
# 
#The input files provided are named dna1.txt, dna2.txt and dna3.txt and are available from the course web 
#site. You may also make up your own text files to test. 
#You may assume that data files are not empty, do contain one DNA sequence, and do not contain any data 
#errors. 
#You must ask the user to input the filename they wish to use. If the file does not open with the filename 
#they entered, keep asking them for a filename until the file does open successfully.
# 


import random
MUTATIONSNUMBER=5

#Output header and game rule.
def fileexist(name):
    try:
        f=open(name,'r')
        return 1
    except:
        return 0

def inputfromfile():
    filename=input('Please enter a file name:')
    while fileexist(filename)==0:
        filename=input('Cannot open file. Enter new a file name:')
    f=open(filename,'r')
    ff=f.read()
    print("Original Sequence Read from File: %s" %ff )
    f.close()
    return ff



def complement(dna):
    #We use a dictionary to index the corresponding complementary letters.
    COMPLEMEN_TTABLE={'T':'A','A':'T' , 'G' :'C' ,'C' : 'G'}
    print('Complement: ',end='')
    for i in range(len(dna)):
        print( COMPLEMEN_TTABLE[dna[i]],end='' )

def Mutate(dna):
#random.sample function generates five random numbers that are not repeated and returns them as a list
    newdna=list(dna)
    list1=random.sample(range(1,len1), MUTATIONSNUMBER)
    for i in list1:
        newdna[i]='M'
    print("Mutation: ",end='')
    for i in range(len1):
        print(newdna[i],end='')
        
    
    

def substrand(dna):
    string=input("Please enter substring:")
    try:
        number=dna.find(string)
        print('Found At Index:  %d'%number)
    except:
        print('do not find it')

    
    
    

def every():
    dna=inputfromfile()
    userinput=0
    input1=0
    while(userinput!=1 and userinput!=2 and userinput!=3 and userinput!=4):
        print('''\nEnter a number 1-4 \n1. Find the complement of the strand\n2. Mutate the DNA strand\n3. Find substrand within the strand\n4. Quit\n-=-=-=-=-=-\n''')
        userinput=int(input('Enter your choice: '))
        input1=1
        if input1:
            print('Invalid Selection/n')
    if userinput==4:
    #The only exit condition is flag==1, which is met when the user enters 4        
        return 1
    print("Original  : %s" %dna)
    if(userinput==1):
        complement(dna)
    elif(userinput==2):
        Mutate(dna)
    elif(userinput==3):
        substrand(dna)
        
        

    return 0

def main():
    flag=0
    #The only exit condition is flag=1, which is met when the user enters 4
    while flag!=0:
        flag=every()
    print('/nFinished')
        
    

main()
    

    
    

