from PIL import Image, ImageDraw
from random import randint,random
from scipy.stats import norm
from math import sqrt
import numpy as np

#initializes a seed for the brownian function
def seeds(size=512):
    seeds = []
    seeds.append((randint(0,size),randint(0,size)))
    return seeds[0]


#function that takes an input position, position step size, and time step size and outputs a position
def brownian(seed=(256,256) ,delt =1.5,deetee=0.05): 
    x0 = np.asarray(seed)
    delta = float(delt)
    dt = float(deetee)
    x0 = x0 + (norm.rvs(scale=delta**2*dt),norm.rvs(scale=delta**2*dt))
    return tuple(x0)


#calls the motion function and the color picking function and draws on the image
def drawbrown(im,size=512,first=(150,0,0),start=None,D=1.5,dt=.05):
    '''
    function that will call the motion function, color function, and starting
    function. while the particle is still on the image it will continue to move
    the particle and update the color.
    '''
    #since we want to start at the center if  not given a start position and start is dependant on size, we use this if else statement to initialize start to be at the center
    start = (256,5)
    if start ==None:
        start = (size/2,size/2)
        
    #count is used to decide when to change a pixel's color, print stuff, and show the current image
    count =2
    starting(im,start)
    brown =brownian(start,D,dt)
    if (brown[0] or brown[1])<=0 or size<=(brown[0] or brown[1]):
        return im.show()

    
    #counters for the color generating function and cross marking function
    state = 'up'
    a=0
    b=50
    c=0
    filler = (0,0,0)
    crossstate = 'up'
    
    while (0,0)<=brown<=(size-1,size-1):
        #parses the state,color, and two counters
        temp = colorupdown(state,first,a,b)
        state = temp[0]
        first = temp[1]
        a = temp[2]
        b = temp[3]
        brown = brownian(brown,D,dt)
        
        #checks that the particle is still on the image        
        if  (brown[0] or brown[1]) >(size-1) or (brown[0] or brown[1])<=0:
            break
        
        count+=1
        if count%50==0:
            #since I'm using the round function rather than floor or ceil, I need logic statements to deal with the boundary cases
            #I'm using round because it creates a faster moving function that using ceil or floor
            if brown[0]>size-1:
                brown = (size-1,int(ceil(brown[1])))
            elif brown[1]>size-1:
                brown = (brown[0],size-1)
            elif brown[0]<0:
                brown = (0,brown[1])
            elif brown[1]<0:
                brown = (brown[0],0)
            else:
                brown = (brown[0],brown[1])
                
        
        if count%1000==0: 
            #prints out current iteration and position
            print '-'*24            
            print count,"     ",(int(round(brown[0])),int(round(brown[1]))) 
            
            #draws on the image
            im.putpixel((int(round(brown[0])),int(round(brown[1]))),first)
        if count%50000 ==0:
            temp2 = cross(im,(int(round(brown[0])),int(round(brown[1]))),filler,c)
            filler = temp2[0]
            c = temp2[1]
            state = temp2[2]
        #shows that image
        if count%50000==0:
            im.show()
    return im.show()


#walks the color for the brownian motion up and down the color spectrum
def colorupdown(state='up',first=(0,0,0),i=0,j=50):
    '''
    state determines if the particle color is going up or down the color
    spectrum from black(low) to white(high). First is the initial color, set to 
    (0,0,0) by default. i and j are counters for the color function to decide
    whether to increment color or not depending on their relation to two 
    different random integers. it first iterates through r, then g, then b
    then once it has reached which, it will decrement in the same order (r>g>b)
    it then returns the state, color, and counters(for the next call) in a tuple
    '''
    if state =='up':
        #increment randomly, but eventually guaranteed to increment
        if first[0]>=255 and first[1]>=255 and first[2]>=255: 
            return ('down',first,i,j)      
        if first[0]<=255:
            if i<randint(1,50) and j>randint(1,10):
                first = (first[0],first[1],first[2])
                i+=30
                j-=5
            else:
                first = (first[0]+int(round(2*random())),first[1],first[2])
                i=0
                j=50
            return ('up',first,i,j)
        elif first[1]<=255:
            if i<randint(1,50) and j>randint(1,10):
                first = (first[0],first[1],first[2])
                i+=30
                j-=5
            else:   
                first = (first[0],first[1]+int(round(2*random())),first[2])
                i,j=0,50
            return ('up',first,i,j)
        
        elif first[2]<=255:
            if i<randint(1,50) and j>randint(1,10):
                first = (first[0],first[1],first[2])
                i+=30
                j-=5
            else:
                first = (first[0],first[1],first[2]+int(round(2*random())))
                i,j = 0,50            
            return ('up',first,i,j)
        
    elif state=='down':
        #decrement r,g,b won't always decrement but will decrement by 0,1,or 2
        if first[0]<=20 and first[1]<=20 and first[2]<=20:
            return ('up', first,i,j) 
        if first[0]>=20:
            first = (first[0]-int(round(2*random())),first[1],first[2])
            return ('down', first,i,j)
        elif first[1]>=20:
            first = (first[0],first[1]-int(round(2*random())),first[2])
            return ('down', first,i,j)
        elif first[2]>=20:
            first = (first[0],first[1],first[2]-int(round(2*random())))
            return ('down', first,i,j) 
        
    return (state,first,i,j)


def starting(im,start=(256,256)):
    '''
    places a white circle with a radius of 5 at the starting point.
    '''
    draw = ImageDraw.Draw(im)
    draw.ellipse(((start[0]-5,start[1]-5),(start[0]+5,start[1]+5)),(256,256,256))
    del draw
    return 


def cross(im,pos,filler = (0,0,0),c=0,state = 'up'):
    '''
    places a small x mark at every nth iteration just to show the direction that
    the motion is progressing in. color gradually changes from black to green and back over the course of 450,000 iterations. 
    ''' 
    
    if filler[1]>=255 and c >=9:
        filler = (0,filler[1]-30,0)
        c-=1
        state = 'down'
    elif filler[1]<=0 and c<=0:
        filler = (0,filler[1]+30,0)
        c+=1
        state = 'up'
    elif state == 'up':
        filler = (0,filler[1]+30,0)
        c+=1
    elif state =='down':
        filler = (0,filler[1]-30,0)
        c-=1    
    draw = ImageDraw.Draw(im)
    draw.line((pos[0]-2,pos[1]-2) + (pos[0]+2,pos[1]+2),fill=filler)
    draw.line((pos[0]-2,pos[1]+2) + (pos[0]+2,pos[1]-2),fill=filler)
    del draw
    return (filler,c,state)


if __name__ == '__main__':
    size = 512
    D =1.75
    dt =.05
    first =(0,0,0)
    n=50
     
    '''
    size = int(raw_input("Enter an image size: "))
    D = float(raw_input("Enter a delta to use: "))
    dt = float(raw_input("Enter a time step size: "))
    first = tuple(raw_input("Enter a rbg color: "))
    second = tuple(raw_input("Enter a rbg color: "))
    n = int(raw_input("Enter the number of iterations to run: "))
    '''
    #creates and image with 512 pixels, hence it is indexed 0->511
    im = Image.new('RGB',((size,size)),(100,100,100))
    start = seeds(size) 
    drawbrown(im,int(size),first,start,D,dt)