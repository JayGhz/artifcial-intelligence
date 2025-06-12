import random
import time
from naoqi import ALProxy


IP = '127.0.0.1'
PORT = 56209
tts = ALProxy("ALTextToSpeech", IP, PORT)
postura = ALProxy("ALRobotPosture", IP, PORT)
motion = ALProxy("ALMotion", IP, PORT)

a = random.uniform(-0.5, 0.5)
b = random.uniform(0.1, 0.2)
names = ['HeadYaw', 'HeadPitch']
times = [[1], [1]]

postura.goToPosture("StandInit", 2.0)
motion.angleInterpolation(names, [a, 0.0], times, True)
motion.angleInterpolation(names, [0.0, b], times, True)