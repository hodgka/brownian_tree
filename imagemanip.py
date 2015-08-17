from PIL import Image,ImageDraw
import motion
from random import randint,random

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


def cross(im,pos,filler = (0,0,0),i=0,j=50):
    '''
    places a small x mark at every nth iteration just to show the direction that
    the motion is progressing in.
    '''
    if i<randint(1,50) and j>randint(1,10):
        i+=30
        j-=30
    else:
        filler = (0,filler[1]+int(round(255*random())),0)
    
    draw = ImageDraw.Draw(im)
    draw.line((pos[0]-2,pos[1]-2) + (pos[0]+2,pos[1]+2),fill=filler)
    draw.line((pos[0]-2,pos[1]+2) + (pos[0]+2,pos[1]-2),fill=filler)
    del draw
    return (filler,i,j)