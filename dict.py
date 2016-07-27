        
''' Sample Input

3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
Sample Output

sam=99912222
Not found
harry=12299933
Explanation

        '''
N = int(raw_input())
d = {}
for i in range(N):
    arr = raw_input()
    key = arr.split(" ")[0]
    value = arr.split(" ")[1]
    d[key] = value

for i in range(N):
    inp = raw_input()
    if inp in d.keys():
        print inp + "=" + d[inp]
    else:
        print "Not found"
