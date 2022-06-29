# Getting the national id and making sure it's exactly 10 digits long.
def input_check(id):
    if len(id) < 10:
        print("Invalid length. Try again")
        return False

# Splitting the digits and convert them to integers.
def id_split(id):
    nums = []
    for i in id:
        nums.append(int(i))
    return nums

# Making a list of ID digit places and reversing them 
# For ease of use when multiplying.
def digit_places():
    digit_places = []
    for digit in range(10,1,-1):
        digit_places.append(digit)
    return digit_places

# Calculating the sum of each ID digit multiplied to its place.
def id_evaluation(splitted_nums, digits, ctrl_num):
    sum = 0
    for i in splitted_nums:
        for j in digits:
            sum += i*j
            digits.pop(0)
            break
    # Getting the remaining of "sum" divided by 11.        
    remain = sum % 11
    if (remain < 2 and ctrl_num == remain) or (remain >= 2 and ctrl_num == (11 - remain)):
        return True
    else:
        return False