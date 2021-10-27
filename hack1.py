'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

def start(courses, start_course, N, M):
    # possible next courses
    next_course = courses[start_course]
    visited = [start_course]
    number_of_course = 2 if next_course is not None else 1
    while number_of_course < N and next_course is not None:
        next_course = courses[next_course]
        if next_course in visited:
            return False
        visited.append(next_course)
        number_of_course += 1
    return number_of_course == N


def pass_courses(courses, N, M):
    for course in courses.keys():
        if course in courses.values():
            pass
        else:
            # no requirements so we can start
            if start(courses, course, N, M):
                return True
    return False

test_number = input()  
for _ in range(int(test_number)):
    s1, s2 = input().split(' ')
    N = int(s1)
    M = int(s2)
    u = {}
    for i in range(M):
        a, b = input().split(' ')
        u[int(a)] = int(b)
    print('1' if pass_courses(u, N, M) else '0')
