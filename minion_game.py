score = {'stuart':0,'kevin':0}
def minion_game(s):
    s = s.casefold()
    vowels = 'aeiou'
    kev = set([c for c in s if c in vowels])
    stu = set(s).difference(kev)

    score['stuart'] = get_score(stu,s)
    score['kevin'] = get_score(kev,s)
    for k,v in score.items():
        print(k,v)

def get_score(letters,s):
    total = 0
    for letter in letters:
        ind = s.index(letter)
        for i in range(ind,len(s)):
            sub = s[ind:i+1]
            total += s.count(sub)
            print(sub,s.count(sub))
    return total
if __name__ == '__main__':
    s = "Banana"
    minion_game(s)