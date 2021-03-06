# ODD NUMBERS

# count the odd numbers in a range
# range is low, high (inclusive)
def countOdds(low, high):
    return (high + 1) // 2 - low // 2

# return minimum number of operations needed for n to become 1
# if n is even, replace with n / 2
# if n is odd, replace with n + 1 or n - 1
# input: n = 65535
# output: 17
def integerReplacement(n):
        count = 0
        while n > 1:
            if n % 2 == 0:
                n /= 2
                count += 1
            else:
                # when n is odd, you would assume that n - 1 is the best choice, as the next step (n / 2) leads to a smaller number
                # but when its binary representation ends with 11, n + 1 applicable. 
                # this happens because n + 1 will create a multiple of 4 or even higher (8, 16 ... 2^x ). So afterwards, we will get at least 2 consecutive divisions instead of one. If we subtracted one, we can prove that that we would waste at least one step.
                if int(n) & 2 and n > 3:
                    n += 1
                else:
                    n -= 1
                count += 1
        return count