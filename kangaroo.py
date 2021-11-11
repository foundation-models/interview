def X(s, t, k):
    #
    # Write your code here.
    #
    i = 0
    while i < len(s) and i < len(t) and s[i] == t[i]:
        i += 1
    
    if i < len(s):
        x = len(s) - i
        if k >= x + len(t):
            return 'Yes'
    start = 0
    ind = 0
    to_del = 0
    to_app = 0
    
    while ind < len(s) and ind < len(t) and s[ind] == t[ind]:
        ind += 1
    start = ind
    
    if start < len(s):
        to_del = len(s[start:])
        if to_del == len(s) and k - to_del >= len(t):
            return 'Yes'
    if start < len(t):
        to_app = len(t[start:])
    k -= to_del + to_app
    
    #print("start = {} to_del = {} to_app = {} k = {}".format(start, to_del, to_app, k))
    if k == 0 or (k > 0 and k % 2 == 0) or k >= 2*len(t):
        return 'Yes'
    else:
        return 'No'
            

print(X('hackerhappy', 'hackerrank', 9))
print(X(2))
print(X(3))
print(X(5))

