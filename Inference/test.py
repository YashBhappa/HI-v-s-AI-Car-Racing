# import gym

# env = gym.make("CarRacing-v0")
# state = env.reset()
# for _ in range(100):
#     env.render()
#     action = env.action_space.sample()  # Random action
#     state, reward, done, _ = env.step(action)
#     if done:
#         state = env.reset()
# env.close()


from OpenGL.GL import *
from OpenGL.GLUT import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE)
glutInitWindowSize(640, 480)
glutCreateWindow("OpenGL Test")
glutDisplayFunc(display)
glutMainLoop()

import gym

env = gym.make("CarRacing-v0")
state = env.reset()

for _ in range(100):
    env.render()  # Ensure rendering happens after resetting
    action = env.action_space.sample()  # Take a random action
    state, reward, done, _ = env.step(action)
    if done:
        state = env.reset()
env.close()
