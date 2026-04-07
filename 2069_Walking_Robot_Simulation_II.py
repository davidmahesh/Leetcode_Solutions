class Robot:
    def __init__(self,width,height):
        self.w=width
        self.h=height
        self.perim=2*(width+height-2)
        self.pos=0
        self.moved=False
        self.dirs=["East","North","West","South"]
        self.track=[]
        for x in range(width):
            self.track.append((x,0,0))
        for y in range(1,height):
            self.track.append((width-1,y,1))
        for x in range(width-2,-1,-1):
            self.track.append((x,height-1,2))
        for y in range(height-2,0,-1):
            self.track.append((0,y,3))

    def step(self,num):
        if self.perim==0:
            return
        self.pos=(self.pos+num)%self.perim
        self.moved=True

    def getPos(self):
        x,y,_=self.track[self.pos]
        return [x,y]

    def getDir(self):
        if self.pos==0:
            if not self.moved:
                return "East"
            return "South"
        _,_,d=self.track[self.pos]
        return self.dirs[d]