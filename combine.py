import motion
import imagemanip
from PIL import Image, ImageDraw

#calls the motion function and the color picking function and draws on the image
def drawbrown(im,size=512,first=(150,0,0),start=(256,256),D=1,dt=.05):
    '''
    function that will call the motion function, color function, and starting
    function. while the particle is still on the image it will continue to move
    the particle and update the color.
    '''
    #since we want to start at the center if  not given a start position and start is dependant on size, we use this if else statement to initialize start to be at the center
    #if start ==(256,256) and size !=512:
    #    start = (256,256)
    #else:
    #    start = (size/2,size/2)
    #count is just to decide when to change a pixel's color, when to print stuff and when to show the current image
    
    count =1
    brown =brownian(start,D,dt)
    if (0,0)>=brown or brown>=(512,512):
        return im.show()
    starting(im,start)
    state = 'up'
    
    #counters for the color generating function and cross marking function
    a=0
    b=50
    c=0
    d=50
    filler = (0,0,0)
    
    while (0,0)<=brown<=(size-1,size-1):
        #parses the state,color, and two counters
        temp = colorupdown(state,first,a,b)
        state = temp[0]
        first = temp[1]
        a = temp[2]
        b = temp[3]
        brown = brownian(brown,D,dt)
        
        #checks that the particle is still on the image        
        if  (brown[0] or brown[1]) >(size-1) or (brown[0] or brown[1])<=1:
            break
        
        count+=1
        if count%50==0:
            #since I'm using the round function rather than floor or ceil, I need logic statements to deal with the boundary cases
            #I'm using round because it creates a faster moving function that using ceil or floor
            if brown[0]>size-1:
                brown = (size-1,int(round(brown[1])))
            elif brown[1]>size-1:
                brown = (brown[0],size-1)
            elif brown[0]<0:
                brown = (0,brown[1])
            elif brown[1]<0:
                brown = (brown[0],0)
            else:
                brown = (brown[0],brown[1])
                
        
        if count%200==0: 
            #prints out current iteration and position
            print '-'*24            
            print count,"     ",(int(round(brown[0])),int(round(brown[1]))) 
            
            #draws on the image
            im.putpixel((int(round(brown[0])),int(round(brown[1]))),first)
        if count%10000 ==0:
            temp2 = cross(im,(int(round(brown[0])),int(round(brown[1]))),filler, c,d)
            cross(im,(int(round(brown[0])),int(round(brown[1]))))
            
            #shows that image
        if count%50000==0:
            im.show()
    return im.show()
