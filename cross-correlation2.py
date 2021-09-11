import numpy as np
import sys
import matplotlib.pyplot as plt

m=np.loadtxt(sys.argv[1],delimiter=',')  # convert a csv file to a matrix from file sys.argv[1]

mt=m.T #transpose matrix

#computing cross-correlation
v1=mt[1][12000:15000];v2=mt[2][12000:15000]
na=len(v1)  #length of data
na2=1/(na*na)  # adjust factor -- groundless
corr=np.empty(0)   #make nd.array of length zero
corr=np.append(corr,np.dot(v1,v2)*na2)
for i in range(len(v1)):
  v2=np.roll(v2,-1)
  corr=np.append(corr,np.dot(v1,v2)*na2)

# find index of maximum element of corr
mx=np.amax(corr)
print(mx)
for i in range(len(corr)):
  if corr[i]==mx:
    print(i)

#output the result to file sys.argv[2]
f = open(sys.argv[2], 'w') 
st=str(corr[0])
for i in range(1,len(corr)):
  if i!=(len(corr)-1):
    st=st+","+str(corr[i])
  else:
    st=st+str(corr[i])
f.write(st)
f.close()

# plot the result
x=range(len(corr)) #plot array
plt.plot(x,corr)
plt.show()
