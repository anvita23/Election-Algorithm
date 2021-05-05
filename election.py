k= int(input("Enter the number of site: "))
votes=[]

for i in range(k):
    votes.append(int(input(f"Enter the number of votes for site {i+1} site= ")))
    
rq=int(input("Enter the RQ= "))
wq= int(input("Enter the WQ= "))
    
#To Determine Consistency 
if (rq+wq >=sum(votes)) and (wq>sum(votes)/2):
    print("The System is Consistent")
else:
    print("The system is Inconsistent")
