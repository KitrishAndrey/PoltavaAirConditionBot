from speech_recognition import (Recognizer, AudioFile)
from subprocess import Popen
from speech_recognition import (UnknownValueError, RequestError)


class SpeechOggAudioFileToText:

    def __init__(self):
        self.recognizer = Recognizer()

    def ogg_to_wav(self, file):
        args = ["ffmpeg", "-i", file, "test.wav"]
        process = Popen(args)
        process.wait()

    @property
    def text(self):
        AUDIO_FILE = "test.wav"
        with AudioFile(AUDIO_FILE) as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.record(source)
        try:
            text = self.recognizer.recognize_google(audio, language="RU")
            return text
        except UnknownValueError:
            print("Не удаеться распознать аудио файл")
        except RequestError as error:
            print("Не удалось запросить результаты {}".format(error))


def main(file_ogg):
    speech_ogg = SpeechOggAudioFileToText()
    speech_ogg.ogg_to_wav(file_ogg)
    return speech_ogg.text