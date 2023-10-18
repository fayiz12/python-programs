""" Write a program to check if two strings are anagrams of each other """


def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)
