#Data processing 
import os
import glob
import pandas as pd
import numpy as np

os.chdir('C:/Users/Dell/Documents/Residencia/')
FileList = glob.glob('*.txt')
tmp = []
for file in FileList:
    df = pd.read_csv(file,header=None, delimiter=',' , names=('x', 'y', 'u', 'v'), skiprows = False) #vorticity
    #df = pd.read_csv(file,header=None, delimiter=',', names=('d','y','x','v'), skiprows=1) #v_speed
    #df = pd.read_csv(file,header=None, delimiter=',', names=('d','x','y','u'), skiprows=1) #u_speed
    df = df.replace(np.nan,0)
    tmp.append(df)

tmp = pd.concat(tmp)
df = pd.DataFrame(tmp)
tmp = df.mean()
#tmp

pd.set_option("display.precision", 4)

#### vorticity average
data = df.groupby(['x','y'], as_index=False)[df.columns[1:]].mean() #vorticity

#### v speed average / standard deviation
#data = df.groupby(['x'], as_index=False)[df.columns[2:]].mean() #v_speed
#data = df.groupby(['x'], as_index=False)[["v"]].std() #v_speed std sigma


#### u speed average / standard deviation
#data = df.groupby(['y'], as_index=False)[df.columns[2:]].mean() #u_speed
#data = df.groupby(['y'], as_index=False)[["u"]].std() #u_speed std sigma

print(data.to_string()) #prints out everything
#print(data) #will print data with less rows


np.savetxt('velfield_average.dat',data, delimiter='\t')#vorticity file
#np.savetxt('v_speed_average.dat',data, delimiter='\t')#v_speed file
#np.savetxt('u_speed_average.dat',data, delimiter='\t')#u_speed file
#np.savetxt('u_speed_std.dat',data, delimiter='\t')#u_speed std sigma file

## Max and Min

max_vals = data.max()
min_vals = data.min()

print('Max values')
print(max_vals)
print('Min values')
print(min_vals)