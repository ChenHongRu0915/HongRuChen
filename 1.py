'''180021106282 陈泓儒 18软工1班'''
sum=0 
count=0 
moredata="yes" 
while(moredata="yes"):
    x=eval(input())
    count+=1
    sum+=x
    if(moredata="no"):
        break
    moredata=input("")
print(sum/count)
