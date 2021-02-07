# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())
for i in range(T):
    S=input()
    res1=''
    res2=''
    for i in range(len(S)):
        if (i%2==0):
            res1+=S[i]
        else:
            res2+=S[i]
    print(res1+' '+res2)

    
