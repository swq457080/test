import os
import thread
import threading
import time
import threading
threading._DummyThread._Thread__stop = lambda x: 42

def t():
    threading.currentThread() # Populate threading._active with a DummyThread
    time.sleep(3)

thread.start_new_thread(t, ())

time.sleep(1)

pid = os.fork()
if pid == 0:
    os._exit(0)

os.waitpid(pid, 0)
