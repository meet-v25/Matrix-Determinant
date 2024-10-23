
# Printing the determminant of a matrix
print('Note:-','Your input is m by n matrix & forgetting det(A), press enter once more')

matrix=[]
while 1:
    x=input().split()
    if x!=[]:
        matrix.append(list(map(float,x)))
    else:
        break
# print('line13',matrix)

def det(a):
    n=len(a)
    if len(a)==1:
        return (a[0][0])
    else:
        sum=0
        i=0
        while i<n:

            b=[]
            j=0
            while j<n:

                # print('ij',i,j)
                if i==j:
                    # print('e1')
                    j+=1
                    continue
                else:
                    b.append((a[j][1:]))
                j+=1
            
            if len(b) != 0 and len(b[0]) != 0:
                # print('i',i,'b',b)
                # print("calling det()")

                x=det(b)
                if i%2 == 0.0:
                    sum+=(a[i][0])*(x)
                    # print('first','i',i,'x',x,'sum',sum)
                elif i%2 == 1.0:
                    sum-=(a[i][0])*(x)
                    # print('second','i',i,'x',x,'sum',sum)

            i+=1
        
        return sum

print(det(matrix))


print("")
print("Press Enter to Exit")
gjhgjjg=input()