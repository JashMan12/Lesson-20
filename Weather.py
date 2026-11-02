weather=(1,0,1,0,1,1,0)
sunny=0
rainy=0
for i in range (0,7):
    if weather [i]==0:
        rainy+=1
    else:
        sunny+=1
if (sunny>rainy):
    print("It will have good weather")
else:
    print("It will have bad weather")