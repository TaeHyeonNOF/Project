import os


def path():
    p = '/'.join(os.getcwd().split("\\"))
    return p

# 테스트