#short hand way to create  list
#alz need at least one for loop to create a lisr
#[expression for i in sequence ]
s=[i for i in range(10)]
print (s)

s1=[i*i for i in range(10)]
print(s1)
s2=[i for i in range(10) if i%2==0]
print(s2)
s3=[i for i in range(5) if i >2]
print(s3)

s4=["even" if i%2 ==0 else "odd" for i in range(10)]
print (s4)