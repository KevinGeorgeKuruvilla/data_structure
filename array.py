# array
# Traversal of array
arr=[10,20,30,40,50]
for i in range(len(arr)):	
	print(arr[i],end=" ")

# insert
arr.insert(2,25)
print("\nAfter insertion:",arr)
print(arr)

# deletion
arr.remove(30)
print("After deletion:",arr)

# Linear search

target=int(input("Enter the element to be searched:"))
def linear_seasrch(arr,target):
	for i in range(len(arr)):
		if arr[i]==target:
			return i
	return -1

# result=linear_seasrch(arr,target)
print(linear_seasrch(arr,target));