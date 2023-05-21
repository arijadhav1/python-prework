#Question 1
def hello_name(user_name):
    print('hello_' + user_name)
hello_name('USERNAME') #'hello_USERNAME'


#Question 2
def first_odds():
    active_polling = True
    val = 0
    while val <= 100:
        if val % 2 == 1:
            print(val)
        val += 1
first_odds() #Returns all odds 1-99


#Question 3
def max_num_in_list(a_list):
    return max(a_list)
print(max_num_in_list([1, 4, 5, 2, 3, ])) #5


#Question 4
def is_leap_year(a_year):
    if a_year % 4 == 0 and (a_year % 100 != 0 or  a_year % 400 == 0):
        return True
    else:
        return False
print(is_leap_year(2020)) #True
print(is_leap_year(2001)) #False
print(is_leap_year(1600)) #True
print(is_leap_year(1800)) #False


#Question 5
def is_consecutive(a_list):
    for num in range(0, len(a_list) - 1):
        if a_list[num] + 1 != a_list[num + 1]:
            return False
    return True  
print(is_consecutive([2, 3, 4, 5, 6, 7])) #True
print(is_consecutive([1, 2, 4, 5])) #False