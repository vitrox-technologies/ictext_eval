from flask import Flask, request
import time
import os
from multiprocessing import Process, Value
from pynvml import *


app = Flask(__name__)
start = time.time()
stop = Value('i', False)

def getUtilization(handle):
    try:
        util = nvmlDeviceGetMemoryInfo(handle)
        mem = util.used
    except NVMLError as error:
        print(error)
        mem = -1
    return mem


def monitor_utilization(target):
    nvmlInit()
    with open(target, 'w') as f:
        f.write("mem_util\n")
        while not stop.value:
            handle = nvmlDeviceGetHandleByIndex(0)
            mem_util = getUtilization(handle)
            f.write("%s\n" % (mem_util / 1024 / 1024))
            f.flush()
            time.sleep(1)
    nvmlShutdown()


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/time')
def timer():
    return str(time.time() - start)


@app.route('/exit')
def exit():
    shutdown_server()
    return 'done'


if __name__ == '__main__':

    p = Process(target=monitor_utilization, args=('/utilization/log.csv',))
    p.start()

    app.run(debug=False, host="0.0.0.0", port=5000)
    stop.value = True
    p.join()
