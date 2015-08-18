import motion
import imagemanip as imanip
from PIL import Image, ImageDraw

#calls the motion function and the color picking function and draws on the image
def drawbrown(im,size=512,first=(150,0,0),start=None,D=1.5,dt=.05):
    '''
    function that will call the motion function, color function, and starting
    function. while the particle is still on the image it will continue to move
    the particle and update the color.
    '''
    #since we want to start at the center if  not given a start position and center is dependant on size, we use this if else statement to initialize start to be at the center
    if start ==None:
        start = (size/2,size/2)
        
    #count is used to decide when to change a pixel's color, print stuff, and show the current image
    count =2
    imanip.starting(im,start)
    brown =motion.brownian(start,D,dt)
    
    if 0>=(brown[0] or brown[1]) or size<=(brown[0] or brown[1]):
        return im.show()

    
    #counters for the color generating function and cross marking function
    state = 'up'
    filler = (0,0,0)
    crossstate = 'up'
    
    
    while 0<(brown[0] or brown[1])< size-1:
        brown = motion.brownian(brown,D,dt)       
        if  brown[0]>size-1 or brown[1] >(size-1) or brown[0]<=0 or brown[1]<=0:
            return im.show()
        count+=1 
        if count%1000==0: 
            #prints out current iteration and position
            print '-'*24            
            print count,"     ",(int(round(brown[0])),int(round(brown[1]))) 
            
            #parses the state,color, and two counters
            temp = imanip.colorupdown(state,first)
            state = temp[0]
            first = temp[1]
            
            #draws on the image
            if brown[0]>=size-1:
                brown = (size-1,int(ceil(brown[1])))
            elif brown[1]>=size-1:
                brown = (brown[0],size-1)
            elif brown[0]<=0:
                brown = (0,brown[1])
            elif brown[1]<=0:
                brown = (brown[0],0)
            else:
                brown = (brown[0],brown[1])            
            im.putpixel((int(round(brown[0])+1),int(round(brown[1]))+1),first)
        if count%50000 ==0:
            temp2 = imanip.cross(im,(int(round(brown[0])),int(round(brown[1]))),filler)
            filler = temp2[0]
            state = temp2[2]
        #shows that image
        if count%50000==0:
            im.show()
    return im.show()