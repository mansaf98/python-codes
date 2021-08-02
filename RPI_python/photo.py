import pygame
import pygame.camera
import boto3
from botocore.exceptions import ClientError
from secret import access_key, secret_access_key
from boto3.session import Session

pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
img = cam.get_image()
pygame.image.save(img,"test.jpg")
print("done taking snapshot" + "\n")
