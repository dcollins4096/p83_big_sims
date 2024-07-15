from dtools.starter1 import *

class lg():
    def __init__(self,fname):
        self.fname=fname
        self.grid_id=[]
        self.left=[]
        self.right=[]
        self.left_zone=[]
        self.right_zone=[]
    def parse(self):
        fptr = open(self.fname,'r')
        lines = fptr.readlines()
        fptr.close()
        
        grid_id = None
        for line in lines:
            san = line.strip()
            if len(san) == 0:
                continue
            pair = line.split('=')
            if pair[0]=='Grid':
                grid_id = int(pair[1])
            print(grid_id)




