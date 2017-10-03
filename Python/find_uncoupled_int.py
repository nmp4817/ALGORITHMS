# Enter your code here. Read input from STDIN. Print output to STDOUT
def find_uncoupled(L):
    ans = 0
    for i in L:
        ans ^= int(i)
    return ans
    
if __name__ == '__main__':
    L = raw_input()
    nums = L.split(",")
    print find_uncoupled(nums)