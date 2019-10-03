def max_letter(s):
    #returns the largest letter that appears in both lowercase and uppercase
    try:
        union = set(s)
        upper = set([letter for letter in union if letter.isupper()])
        lower = union.difference(upper)
        lower = set([let.capitalize() for let in lower])
        intersect = upper.intersection(lower)
        return(max(intersect))
    except ValueError:
        return"No"


def consecutive_product(A, B):
    #returns the number of integers within a given range which is a product of f(y): y = x*(x+1)
    count = 0
    #li = [i for i in range(A,B+1) if i%2==0 ]
    for i in range(A,B+1):
        nums = get_divs(i)
        #print(i,nums)
        if has_consecutive(nums,i):
            count+=1
    return count
def get_divs(num):
    nums = [i for i in range(1,(num//2)+1) if i*(i+1)==num]
    return nums

def has_consecutive(li,target):
    for num in li:
        if (num*(num+1))== target:
            return True
    return False

def fixed(S):
    occurrences = [0] * 26

    for i in range(len(S)):
        occurrences[ord(S[i]) - ord('a')] += 1

    best_char = chr(ord('a') + occurrences.index(max(occurrences)))
    best_res = occurrences[occurrences.index(max(occurrences))]

    for i in range(1, 26):
        if occurrences[i] == best_res and best_char > chr(ord('a') + i):
            best_char = chr(ord('a') + i)
            best_res = occurrences[i]

    return best_char

