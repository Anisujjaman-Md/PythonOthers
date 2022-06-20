def max_depth(s):
 
    count = 0
    st = []
    for i in range(len(s)):
        if (s[i] == '<'):
            st.append(i) # pushing the bracket in the stack
        elif s[i] == '>':
            count = max(count, len(st))
            st.pop() # popping the bracket from the stack

    return count
 
# Driver program
 
s = "<<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<<<<<<<<<>>>>>><<<<<<<<<"
print(max_depth(s) // 2)