import cv2
import numpy as np
from controller import Robot,Camera


class imagetransform:
    @staticmethod
    def convert(image):    #prepare camera input for use
        result=np.asarray(image, dtype=np.uint8)
        result= cv2.cvtColor(result,cv2.COLOR_BGRA2RGB)
        result= cv2.rotate(result,cv2.ROTATE_90_CLOCKWISE)
        return cv2.flip(result,1)

class image(Camera):
    def __init__(self,timestep):
        super().__init__('camera')
        self.enable(timestep)

    def convert(self):
        return imagetransform.convert(self.getImageArray())

robot = Robot()
timestep = int(robot.getBasicTimeStep())
camera = image(timestep)

#initialize motors and velocities
motor_left = robot.getDevice('left wheel motor')
motor_right = robot.getDevice('right wheel motor')
motor_left.setPosition(float('inf'))
motor_right.setPosition(float('inf'))
motor_left.setVelocity(0)
motor_right.setVelocity(0)


while robot.step(timestep) != -1:
    img = camera.convert()
    img=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
    #finding mask based on values determined through experimental means for the color of the ball (check detectcolor.py)
    ll=np.array([25,41,0])
    ul=np.array([173,255,255])
    mask=cv2.inRange(img,ll,ul)

    #find x-center of contour
    (cnts,hierarchy)=cv2.findContours(mask.astype(np.uint8).copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)[-2:]
    contour=max(cnts, key=cv2.contourArea)
    M=cv2.moments(contour)
    x=int(M["m10"] / M["m00"])

    #calculate error or difference between positions
    distance=camera.getWidth()/2 - x
    print(x)
    #print(camera.getWidth())
    
    #turn left or right with a proportional coefficient
    motor_left.setVelocity(-distance*0.1)
    motor_right.setVelocity(distance*0.1)
    


   
    