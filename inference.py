import numpy as np
import cv2
import subprocess
import time

cap = cv2.VideoCapture(0)
print("Running The Model ..... ")
print("Please click below .. ")

print("http://localhost:8000/view_results.html")

def process_image(img):
    stime= time.time()
    msg = subprocess.check_output("th run_model.lua -input_image imgs/frame.jpg -gpu -1",shell=True)
    print(msg)
    inferrence_time = str(time.time()-stime)
    print("Total Inference time: %s"%inferrence_time)

    try:
        msg = subprocess.check_output("cd vis;python3 -m http.server",shell=True)
    except KeyboardInterrupt:
        pass
    print("press n: next image")
    print("press q: quit")


while(cap.isOpened()):
    t = input()
    if t == 'n':
        # Capture frame-by-frame
        ret, frame = cap.read()
        rgb_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imwrite("imgs/frame.jpg",frame)
        process_image(rgb_img)
        time.sleep(5)
        subprocess.check_output("cd ..;",shell=True)
    
    if t == 'q':
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()