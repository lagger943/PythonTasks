list_one = ['six', 'three', 'two', 'one']
list_two = ['four', 'seven', 'five']
final_list = list_two + list_one
print(final_list[-1:-4:-1] + final_list[0:3:2] + final_list[-4:-7:-2])