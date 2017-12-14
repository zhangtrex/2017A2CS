# zhang chenyang Rex S3C3 OP1
# Solution of Codingbat Recursion 2

def groupSum(s,nums,t):
    if t == 0:
        return True
    if s == len(nums):
        return False
    return groupSum(s+1, nums, t-nums[s]) or groupSum(s+1, nums, t)

def groupSum6(s,n,t):
    if t == 0 and s == len(n):
        return True
    elif t != 0 and s == len(n):
        return False
    if n[s] == 6:
        return groupSum6(s+1,n,t-n[s])
    elif t == 0 and s != len(n):
        return groupSum6(s+1,n,t)
    else:
        return groupSum6(s+1,n,t-n[s]) or groupSum6(s+1,n,t)

def groupNoAdj(s,n,t):
    if t == 0:
        return True
    if s >= len(n):
        return False
    return groupNoAdj(s+2,n,t-n[s]) or groupNoAdj(s+1,n,t)

def groupSum5(s,n,t):
    if s >= len(n):
        return t == 0
    if n[s] % 5 == 0 and s < len(n)-1:
        if n[s+1] == 1:
            return groupSum5(s+2,n,t-n[s])
        else:
            return groupSum5(s+1,n,t-n[s])
    elif n[s] % 5 == 0:
        return groupSum5(s+1,n,t-n[s])
    else:
        return groupSum5(s+1,n,t-n[s]) or groupSum5(s+1,n,t)
    
def groupSumClump(s,n,t):
    if s >= len(n):
        return t == 0
    ind = s;
    while ind < len(n)-1:
        if n[ind] == n[ind+1]:
            ind = ind + 1;
        else:
            break
    return groupSumClump(ind+1,n,t-(ind-s+1)*n[s]) or groupSumClump(ind+1,n,t)

def splitArray(n):
    if len(n) == 1 and n[0] == 0:
        return True
    elif len(n) == 1 and n[0] != 0:
        return False
    return splitArray(n[:-2] + [n[-2] - n[-1]]) or splitArray(n[:-2] + [n[-2] + n[-1]])

def splitOdd10(n):
    if len(n) == 1 and n[0] % 2 == 1:
        return True
    elif len(n) == 1 and n[0] % 2 == 0:
        return False
    if len(n) == 2 and n[0] % 10 == 0 and n[1] % 2 == 1:
        return True
    elif len(n) == 2 and n[1] % 10 == 0 and n[0] % 2 == 1:
        return True
    elif len(n) == 2:
        return False
    else:
        return (splitOdd10(n[:-2]+[n[-2]+n[-1]]) or splitOdd10([n[0]+n[1]]+n[2:])) or splitOdd10([n[0]+n[-1]]+n[1:-1]) or splitOdd10(n[1:-1]+[n[0]+n[-1]])

def _53helper(s,n,s1,s2):
    if s >= len(n):
        return s1 == s2
    if n[s] % 5 == 0:
        return _53helper(s+1,n,s1+n[s],s2)
    elif n[s] % 3 ==0:
        return _53helper(s+1,n,s1,s2+n[s])
    else:
        return _53helper(s+1,n,s1+n[s],s2) or _53helper(s+1,n,s1,s2+n[s]);

def split53(n):
    return _53helper(0,n,0,0);

print(split53([1,2,3,3,15,6]))
print(split53([10,3,2,3,5,11]))





