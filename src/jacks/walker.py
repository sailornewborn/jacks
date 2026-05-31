from . import *

class GetWalker:
    def __init__(self,start:int,stop:int):
        self.start = start
        self.stop = stop
    
    def get_walking(self) -> list[int]:
        holder = []
        for item in range(self.start,self.stop):
            holder.append(item)
        holder.append(self.stop)
        return holder
    