from settings import *
from datetime import datetime

logAdd = lambda msg, x: msg + str(x) + "\n"

def saveLog(e): # For easy debug with breakpoints
    sysdatetime = datetime.now().isoformat().replace(":", ".")
    log = logAdd("Log ", sysdatetime)
    log += logAdd("Error:", e)
    log += logAdd("Width:", WIDTH)
    log += logAdd("Height: ", HEIGHT)
    log += logAdd("Viewport size: ", viewport_size)
    log += logAdd("Z projection: ", Z_PROJECTION)
    log += logAdd("FPS: ", FPS)
    log += logAdd("BG color: ", BACKGROUND_COLOR)
    log += logAdd("Scene:", '')
    for i in SCENE.objects:
        log += logAdd(str(type(i)) + " ", i)
    log += logAdd("Camera: ", camera)
    file = open("log_" + sysdatetime + ".log", "w")
    file.write(log)
    file.close()
