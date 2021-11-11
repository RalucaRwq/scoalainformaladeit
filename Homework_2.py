# exercise 1
def sum_function(*args, **kwargs):
    my_sum = 0
    for x in args:
        if type(x) == int:
            my_sum = my_sum + x
    return my_sum


print(sum_function(1, 5, -3, "abc", [12, 56, "cad"]))
print(sum_function())
print(sum_function(2, 4, "abc", param_1=2))


# exercise 2

def recursive_sum(n):
    if n <= 1:
        return n
    else:
        return n + recursive_sum(n-1)

def recursive_sum_even(n):
    if n <= 1:
        return n
    elif n % 2 != 0:
        return n-1 + recursive_sum_even((n-1)-2)
    return n + recursive_sum_even(n-2)

def recursive_sum_odd(n):
    if n <= 1:
        return n
    elif n == 2:
        return n-1
    elif n % 2 == 0:
        return n-1 + recursive_sum_odd((n-1)-2)
    return n + recursive_sum_odd(n-2)


print("The sum of all numbers from 0 to n is:", recursive_sum(10))
print("The sum of all even numbers from 0 to n is:", recursive_sum_even(8))
print("The sum of all odd numbers from 0 to n is:", recursive_sum_odd(6))

# exercise 3
def my_input(user):
    if type(user) == int:
        return user
    else:
        return 0


print(my_input(10.5))
print(my_input(10))
