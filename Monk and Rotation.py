'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''


def rotate_one_elmeent(A, k , i, tmp):
    new_i = (i + k) % N
    new_tmp =  A[new_i]
    A[new_i] = tmp
    return A, new_i, new_tmp

def rotate(N, k, A):
    i = 0
    tmp = A[0]
    for _ in range(N):
        A, i, tmp = rotate_one_elmeent(A, k, i , tmp)
    return A


test_number = raw_input()  
for _ in range(int(test_number)):
    s1, s2 = raw_input().split(' ')
    N = int(s1)
    K = int(s2)
    st = raw_input().split(' ')
    A = []
    for c in st:
        A.append(int(c))
    B = rotate(N, K, A)
    for b in B:
       print(b),
