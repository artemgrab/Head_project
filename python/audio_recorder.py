import sounddevice as sd
from scipy.io.wavfile import write
import os

save_directory = r"C:\Users\Artem\OneDrive\Робочий стіл\Head_project\audio"
filename = "output.wav"
file_path = os.path.join(save_directory, filename)


class VoiceRecorder:
    def __init__(self):
        self.fs = 11025
        self.recordtime = 10
        self.channels = 1

    def record_voice(self):
        print('start recording')
        myrecording = sd.rec(int(self.recordtime * self.fs), samplerate=self.fs, channels=self.channels)
        sd.wait()
        print('ended recording')
        write(file_path, self.fs, myrecording)
