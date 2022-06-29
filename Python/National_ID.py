# Getting the national id and making sure it's exactly 10 digits long.
national_id = input("Enter code:")
while len(national_id) < 10:
    print("Invalid length. Try again")
    national_id = input("Enter code:")

# Splitting the digits and convert them to integers.
nums = []
for i in national_id:
    nums.append(int(i))
ctrl_num = nums[9] # This is the controlling digit in ID.

# Making a list of ID digit places and reversing them 
# For ease of use when multiplying.
places = []
for i in range(2,11):
    places.append(i)
places.reverse()

# Calculating the sum of each ID digit multiplied to its place.
sum = 0
for i in nums:
    for j in places:
        sum += i*j
        places.pop(0)
        break

# Getting the remaining of "sum" divided by 11.        
remain = sum % 11
if (remain < 2 and nums[9] == remain) or (remain >= 2 and nums[9] == (11 - remain)):
    print("%s\nVALID." % national_id)
else:
    print("%s\nINVALID." % national_id)

    

