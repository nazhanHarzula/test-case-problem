import json
# Split data based on ascending part
def split_data_into_part(list_order):
    list_new = []
    my_list = []
    
    for i in range(len(list_order)):
        if i+1 < len(list_order):
            if list_order[i] < list_order[i+1]:
                my_list.append(list_order[i])
            else:
                my_list.append(list_order[i])
                list_new.append(my_list)
                my_list = []
    
    return list_new
    
# Do it some of math
def doing_some_math(list_part):
    dict_part = {}
    median = 0;
    number_data = len(list_part);
    list_part = sorted(list_part)
    mean = sum(list_part) / number_data;
    
    if number_data % 2 != 0:
        median = list_part[number_data // 2]
        return {
            'Our Data' : list_part,
            'Mean' : mean,
            'Median' : median
        }
    else:
        median = (list_part[int((number_data-1)/2)] + list_part[int(number_data / 2)]) / 2
        return {
            'Our Data' : list_part,
            'Mean' : mean,
            'Median' : median
        }

output_data = [] # output
list_order = [3,4,5,7,12,25,23,29,28,27,31,32] # Input

list_order_part = split_data_into_part(list_order)
for list_math in list_order_part:
    output_data.append(doing_some_math(list_math))
    
# beautify to be json
print(json.dumps(output_data, sort_keys=True, indent=4))
