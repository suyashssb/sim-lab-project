import image
import numpy as np

def load_image('ict.jpg'):
    img=Image.open('ict.jpg')
    img.load()
    data=np.asarray(img,dtype,"int32")
    return data
    
def save_image(npdata,'xyz'):
    img=Image.fromarray(np.asarray(np.clip(npdata,0,255),dtype='uint8),"L")
    img.save(xyz)
    
