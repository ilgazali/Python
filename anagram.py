#MUHAMMET ALİ ILGAZ
#In this code block, I created 4 method to solve the problem.
import random

str1 = input("Enter the first string : ")
str2 = input("Enter the second string: ")

#first method is for converting a string to an integer list.
def str2chr2int(str):
    int_list = []
    for chr in str:
        int_list.append(ord(chr))
    return int_list

#Second method is for sorting the integer list.
def bubble_sort(list):
    temp = 0
    for i in range(1,len(list)): #0
        for j in range(len(list)-i):#0-5
            if list[j] > list[j+1]:
                temp = list[j]
                list[j]=list[j+1]
                list[j+1] = temp
    return list


#I created third method that generates a random string using the first string.
def create_anagram(str1): return "".join(random.sample(str1,k=len(str1))) #Third method.

#Fourth method is for comparing two string and return matching or not matching.
def compare2str(str1,str2):
    int_list_1 = str2chr2int(str1)
    int_list_2 = str2chr2int(str2)

    new_list_1 = bubble_sort(int_list_1)
    new_list_2 = bubble_sort(int_list_2)
    if (new_list_1 == new_list_2):
         return print("Anagram is matching.")
    else:
        if len(str1) != len(str2):
         return print("The size of the two strings is not equal.\nAnagram is not matching.")
        else:#They may not be anagrams even if their size is equal
         return print("Anagram is not matching.")

#Output
if str2 == "":
    new_str2 = create_anagram(str1)
    print("First string:",str1)
    print("Created string:",new_str2)
    compare2str(str1,new_str2)

else:
    print("First string : ",str1)
    print("Second string: ",str2)
    compare2str(str1,str2)




