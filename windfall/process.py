from unittest import main, TestCase 
import pandas as pd



def split_plus(st):
    numbers = st.split('+')
    sum = 0
    for number in numbers:
        sum += minus(number)
    return sum


def minus(y):
    numbers = y.split('-')
    if len(numbers) == 1:
        return int(numbers[0])
    sum = int(numbers[0])
    for index, number in enumerate(numbers):
        if index == 0:
            continue
        sum -= int(number) 
    return sum












# def split_it(y, operator):

#     sum = 0
#     result = []
#     for xxx in numbers:
#         try:
#             xx = int(xxx)
#             result.append(xx)
#         except ValueError:
            
    
    
    
#     if len(numbers) == 2:
#         if operator == '+':
#             sum = int(numbers[0]) + int(numbers[1])
#         else:
#             sum = int(numbers[0]) - int(numbers[1])
#     elif len(numbers) == 1:
#             return numbers[0]
#     else:
#         for xx in numbers:
#             split_it(xx, operator)
            
#     return sum
#     result.append(sum)

def procees_it(x):
    result = []
    for y in x:
        if '+' not in y and '-' not in y:
            result.append(y)
        else:
            xx = split_plus(y)
            # numbers = y.split('+')
            # sum = 0
            # for number in numbers:
            #     sum += int(number) 
            result.append(xx)
           
    return result

class TestSolution(TestCase):
    

    
    def test_solution(self):
        df = pd.read_csv("/Users/hossein.akhlaghpour/src/home/interview/input.csv", header=None)
        df1 = df.apply(procees_it)
        print(df1.shape)

if __name__ == "__main__":
    main()