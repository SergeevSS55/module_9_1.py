'''функция apply_all_func, которая принимает параметры:
int_list - список из чисел (int, float)
*functions - неограниченное кол-во функций
(которые применимы к спискам, состоящим из чисел)'''
def apply_all_func(int_list, *functions):
    result = {}
    for func in functions:
        result[func.__name__] = func(int_list)
    return result

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))