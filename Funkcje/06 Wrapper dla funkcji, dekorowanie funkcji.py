import datetime
import functools

def CreateFunctionWithWrapper(func):
    def func_with_wrapper(*args, **kwargs):
        print('Function "{}" staret at {}'.format(func.__name__,datetime.datetime.now().isoformat()))
        print('Following arguments were used: ')
        print(args,kwargs)
        result = func(*args, **kwargs)
        print('Function returned {}'.format(result))
        return result

    return func_with_wrapper

@CreateFunctionWithWrapper # to znaczy, że funkcja jest udekorowana
def ChangerSalary(emp_name, new_salary, is_bonus = False):
    print('CHANGING SALARY FOR {} TO {} AS BONUS = {}'.format(emp_name,new_salary,is_bonus))
    return new_salary

print(ChangerSalary('Johnson', 20000, True))


#ChangeSalary = CreateFunctionWithWrapper(ChangerSalary)
print(ChangerSalary('Johnson', 20000, True))


