# https://leetcode.com/discuss/interview-question/376019/twitter-oa-2019-autoscale-policy
def autoScale(ins, A):
    lim_l, lim_h, th_l, th_h, idle = 1, int(1e8), 25, 60, 10
    i, n, ans = 0, len(A), ins
    while i < n:
        print(f'{i}-th second, utility is {A[i]}, instance number before action is {ans}')
        if A[i] < th_l and ans > lim_l:
            ans, i = (ans + 1) // 2, i + idle
        elif A[i] > th_h and ans <= lim_h:
            ans, i = ans * 2, i + idle
        i += 1
    return ans
                
ins, A = 1, [5, 10, 80]
print(autoScale(ins, A))

ins, A = 2, [25,23,1,2,3,4,5,6,7,8,9,10,76,80]
print(autoScale(ins, A))
