#Импорт модуля sounddevice
import sounddevice
from scipy.io.wavfile import write
#Функция записи
def voice_recorder(seconds, file):
    print('Запись началась')
    recording = sounddevice.rec((seconds * 44100), samplerate=44100, channels=2)
    sounddevice.wait()
    write(file, 44100, recording)
    print('Запись завершена')



voice_recorder(10, 'Запись.wav')