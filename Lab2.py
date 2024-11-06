


def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input(): 
    print("get_user_input")
    user_input = input()

    print("Raw Input: "+ user_input)
    #split the input string to segments of strings using comma as splitter
    split_list = user_input.split(",")

    print("After Splitting: " , split_list)
    #Convert each short string to float
    floatlist = [] #defining an empty list
    
    for x in split_list: 
        float_number = float(x) # will give a float number
        floatlist.append(float_number)
    print("Float List: " , floatlist)
    return floatlist

def calc_average(input_list):
    print("calc_average") 
    total = sum(input_list)
    average = total/len(input_list)
    print("Average is: " , average)
    return average

def find_min_max(input_list):
    print("find_max_min")
    input_list.sort() #help to sort the numbers in increasing
    result_list = [input_list[0],input_list[-1]]
    print("Max: ", result_list[0])
    print("Min: ", result_list[1])
    return result_list

def sort_temp(input_list):
    print("sort_temperature")
    input_list.sort()

def calc_median_tempterature(input_list): 
    print("calc_median_temperature")
    count = len(input_list)
    if count % 2 is 1:
        median = input_list[(count -1)//2]#// - forcing the output to be integers
    else: 
        median = (input_list[count//2] + input_list[(count//2)-1])/2

    return median
    print("Median: ", median)

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    floatlist = get_user_input()
    calc_average(floatlist)
    find_min_max(floatlist)
    sort_temp(floatlist)
    print("After Sorting: ", floatlist)
    calc_median_tempterature(floatlist)


if __name__ == "__main__":
    main()   