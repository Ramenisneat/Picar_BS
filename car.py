import pygame
from picar import front_wheels, back_wheels
from picar.SunFounder_PCA9685 import Servo
import picar



picar.setup()

PAN_ANGLE_MAX   = 120
PAN_ANGLE_MIN   = 0
TILT_ANGLE_MAX  = 120
TILT_ANGLE_MIN  = 60
FW_ANGLE_MAX    = 120
FW_ANGLE_MIN    = 60

bw = back_wheels.Back_Wheels()
fw = front_wheels.Front_Wheels()
pan_servo = Servo.Servo(1)
tilt_servo = Servo.Servo(2)

#picar.setup() ??? I don't know if it should be before or after

fw.offset = 0
pan_servo.offset = 10
tilt_servo.offset = 0


pan_angle = 90
tilt_angle = 90
fw_angle = 90

fw.turn(fw_angle)
pan_servo.write(pan_angle)
tilt_servo.write(tilt_angle)

motor_speed = 100

pygame.init()
screen = pygame.display.set_mode((400,400))
done = False
while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                tilt_angle = TILT_ANGLE_MAX
            if event.key == pygame.K_RIGHT:
                tilt_angle = TILT_ANGLE_MIN
            if event.key == pygame.K_DOWN:
                pan_angle = PAN_ANGLE_MIN
            if event.key == pygame.K_UP:
                pan_angle = PAN_ANGLE_MAX

            if event.key == pygame.K_a:
                fw.turn_left()

            if event.key == pygame.K_d:
                fw.turn_right()

            pan_servo.write(pan_angle)
            tilt_servo.write(tilt_angle)

            tilt_angle = 90
            pan_angle = 90
            fw_angle = 90
        
            if event.key == pygame.K_s:
                bw.speed = motor_speed
                bw.backward()
            elif event.key == pygame.K_w:
                bw.speed = motor_speed
                bw.forward()
    
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                fw.turn_straight()

            if event.key == pygame.K_w or event.key == pygame.K_s:
                bw.stop()

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pan_servo.write(90)

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                tilt_servo.write(90)
            

           
