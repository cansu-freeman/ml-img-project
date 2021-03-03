import numpy as np 
import pandas as pd


def create_file_list(dir):
    """
    Function will create a list of files according to my file naming convention.
    Not suitable for general use bc parts are hardcoded, (but feel free to take 
    use as needed).
    """
    i = 1
    files = []

    while i <= 3111: #3111 image folders
        x = dir+"/photo"+str(i)+"/info"+str(i)+".txt"
        files.append(x)
        #print('created file '+str(i)) 
        i+=1

    return files


# Creating list of the files to parse through
dir = "enter/directory/here"
files = create_file_list(dir)

# Creating the empty df 
df = pd.DataFrame(columns=['man','ypr','lat_e','long_e','elvt_e','fov_e', 'lat', 'long', 'elvt', 'fov'])

for file in files:
     with open(file, 'r') as f:
         data=f.read().strip().split('\n\n')
         data=[i.split('\n') for i in data if i!=''] #get the rows
        
         s = pd.DataFrame(data, columns=df.columns)  
         df =pd.concat([df, s], ignore_index=True)

df['id'] = list(range(1, 3112))
df = df[['id','man','ypr','lat_e','long_e','elvt_e','fov_e', 'lat', 'long', 'elvt', 'fov']] #reordering df

# Seperating the yaw, pitch, roll
l = []
for i in df['ypr']:
    x = i.split(' ', 2)
    l.append(x)

yaw = []
pitch = []
roll = []
for i in l:
    yaw.append(i[0])
    pitch.append(i[1])
    roll.append(i[2])

df['yaw'] = yaw
df['ptch'] = pitch
df['roll'] = roll

# Turning 'man' a dummy variable, if manual then 1, otherwise 0
df['man'] = df['man'].map({'MANUAL': 1, "AUTO": 0})



##### Adding 'path' variable
path_df = pd.read_csv('/enter/directory/here/imagelist.txt', names=['path'], header = None)
path_df['ext'] = path_df['path'].str.split('.').str[-1]
path_df['npath'] = path_df['path'].str.split('.').str[0]
path_df['photo_id'] = path_df['path'].str.split('/photo').str[-1]
path_df['id'] = path_df['photo_id'].str.split('.').str[0]
path_df[['id']] = path_df[['id']].apply(pd.to_numeric)

path_df.sort_values(by ='id')
path_df = path_df[['path', 'id']]
new = df.merge(path_df, on='id')

new.to_csv("enter/directoy/here/df_gh.csv")

