import os
import subprocess



subprocess.


def isRunning(process_name):
    try:
        process = len(os.popen('ps aux | grep "' + process_name + '" | grep -v grep').readlines())
        if process >= 1:
            return True
        else:
            return False
    except:
        print("Check process ERROR!!!")
        return False


def startProcess(process_script):
    try:
        result_code = os.system(process_script)
        if result_code == 0:
            return True
        else:
            return False
    except:
        print("Process start Error!!!")
        return False


