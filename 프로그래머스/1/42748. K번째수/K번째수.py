def solution(array, commands):
    ans = []
    for command in commands:
        i,j,k = command[0], command[1], command[2]
        temp_arr = array[i - 1:j]
        temp_arr.sort()
        ans.append(temp_arr[k - 1])
    return ans