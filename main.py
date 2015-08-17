import motion
import imagemanip
import combine
from PIL import Image

def main():
   
    size = int(raw_input("Enter an image size: "))
    D = float(raw_input("Enter a delta to use: "))
    dt = float(raw_input("Enter a time step size: "))
    first = tuple(raw_input("Enter a rbg color: "))
    second = tuple(raw_input("Enter a rbg color: "))
    n = int(raw_input("Enter the number of iterations to run: "))
    
    #creates and image with 512 pixels by default or whatever size specified, hence it is indexed 0->511
    im = Image.new('RGB',((size,size)),(100,100,100))
    #calls the seed function in the motion file and creates a seed for the brownian function
    start = seeds(size)
    #calls the drawbrown function from combine that combines all the other functions in the other files
    drawbrown(im,int(size),first,start,D,dt)
    

if __name__ == '__main__':
    main()