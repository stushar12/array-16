n=int(input("Enter number of elements "))
arr=[]
print("Enter elements :")
for i in range(0,n):
    z=int(input())
    arr.append(z)


low=0
medium=0
high=n-1

while(medium<=high):
    if(arr[medium]==0):

        temp=arr[low]
        arr[low]=arr[medium]
        arr[medium]=temp
 
        low=low+1
        medium=medium+1

    elif(arr[medium]==1):
        medium=medium+1

    elif(arr[medium]==2):

        temp=arr[medium]
        arr[medium]=arr[high]
        arr[high]=temp

        high=high-1

print(f"Sorted array is {arr}")

