from random import randint
import motion
import imagemanip
import combine
from PIL import Image

def main():
    if raw_input("Enter your own options? y/n: ") =='y':
        ownoptions = True
    else:
        ownoptions = False
    if ownoptions ==True:
        size = int(raw_input("Enter an image size: "))
        D = float(raw_input("Enter a delta to use: "))
        dt = float(raw_input("Enter a time step size: "))
        first = tuple(raw_input("Enter an rbg color: "))
    else:
        size = 512
        D = 1.5
        dt = 0.05
        first = (0,0,0)
    if raw_input("Save? y/n: ") == 'y':
        save = raw_input("Enter a filename: ")
    else:
        save =False
        
        
    #creates and image with 512 pixels by default or whatever size specified, hence it is indexed 0->511
    im = Image.new('RGB',(size,size),(100,100,100))
    #calls the seed function in the motion file and creates a seed for the brownian function
    start = motion.seeds(size)
    #calls the drawbrown function from combine that combines all the other functions in the other files
    combine.drawbrown(im,int(size),first,start,D,dt)
    if save!= False:
        im.Save(save)
    

if __name__ == '__main__':
    main()