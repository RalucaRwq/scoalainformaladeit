def my_function(param1, param2, param3, *args):
    my_sum = []
    if isinstance(param1, int):
        my_sum.append(param1)
    if isinstance(param2, int):
        my_sum.append(param2)
    if isinstance(param3, int):
        my_sum.append(param2)
    my_sum = sum(my_sum)
    print(my_sum)
    return 0

my_function()