import os

path = '/home/felicia/Documents/house_diffusion/datasets/rplan'

with open('/home/felicia/Documents/house_diffusion/datasets/list.txt', mode='w') as fp:
    for file in sorted(os.listdir(path)):
        fp.write(str(file)+'\n')

print("******Finished list generation******")