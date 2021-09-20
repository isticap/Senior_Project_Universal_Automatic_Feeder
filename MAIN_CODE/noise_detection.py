#ridding window of warnings
from ctypes import *

# From alsa-lib Git 3fd4ab9be0db7c7430ebd258f2717a976381715d
# $ grep -rn snd_lib_error_handler_t
# include/error.h:59:typedef void (*snd_lib_error_handler_t)(const char *file, int line, const char *function, int err, const char *fmt, ...) /* __attribute__ ((format (printf, 5, 6))) */;

# Define our error handler type
ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

def py_error_handler(filename, line, function, err, fmt):

  return 0

c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

asound = cdll.LoadLibrary('libasound.so')

# Set error handler
asound.snd_lib_error_set_handler(c_error_handler)

import pyaudio
import math
import struct
import wave
from subprocess import call
import subprocess
import time

# assuming Energy threshold upper than 30 dB
Threshold = 30

SHORT_NORMALIZE = (1.0/32768.0)
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
swidth = 2
Max_Seconds = 10
TimeoutSignal=((RATE / chunk * Max_Seconds) + 2)
silence = True
Time=0
all =[]
p = pyaudio.PyAudio()

def GetStream(chunk):
    return stream.read(chunk)
def rms(frame):
    count = len(frame)/swidth
    format = "%dh"%(count)
    # short is 16 bit int
    shorts = struct.unpack( format, frame )

    sum_squares = 0.0
    for sample in shorts:
        n = sample * SHORT_NORMALIZE
        sum_squares += n*n
    # compute the rms 
    rms = math.pow(sum_squares/count,0.5)
    return rms * 1000

def listen(silence,Time):
    print ("waiting for Speech")
    while silence:
        try:
            input = GetStream(chunk)
        except:
            continue
        rms_value = rms(input)
        if (rms_value > Threshold):
            silence=False
            LastBlock=input
            print("noise detected")
            return 105
#            p.terminate()
#            call(["python3", "picam.py"])
            #KeepRecord(TimeoutSignal, LastBlock)
#        Time = Time + 1
#         if (Time > TimeoutSignal):
#             print "Time Out No Speech Detected"
#             sys.exit()


stream = p.open(format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True,
    frames_per_buffer = chunk)

if listen(silence,Time) == 105:
    stream.stop_stream()
    stream.close()
    p.terminate()
    subprocess.run("pkill -9 -f motion_detection.py", shell=True)
    time.sleep(5)
    call(["python3", "picam.py"])

