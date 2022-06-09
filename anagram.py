s1=input("enter the first string")
s2=input("enter the second string")
t1=sorted(s1)
t2=sorted(s2)
if(len(s1)==len(s2)):
     if (t1==t2):
        print("two strings are anagram")
     else:
        print("two strings are not anagram")
