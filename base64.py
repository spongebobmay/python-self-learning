import base64
def b6(str):
    C=str+'='*(4-len(str)%4)
    return base64.b64decode(C)
