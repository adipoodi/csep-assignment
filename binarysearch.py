def binarysearch(array,low,high,x):
      if high>=low:
         mid=(high+low)//2
         if array[mid]==x:
            return mid
         elif array[mid]>x:
            return binarysearch(array,low,mid-1,x)
         else:
            return binarysearch(array,mid+1,high,x)
      else:
          return -1

array=[2,5,7,9,10]
x=int(input("enter the element"))
result=binarysearch(array,0,len(array)-1,x)
if result!=-1:
   print("element is present")
else:
   print("element is not present")
            
