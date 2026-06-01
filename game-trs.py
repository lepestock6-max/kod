import sounddevice as sd
import scipy.io.wavfile as wav
import speech_recognition as sr
import random
from deep_translator import GoogleTranslator

def speech_translate(duration=5, sample_rate=44100, source_lang="eng-ENG", target_lang="ru"):
    print("Говори...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype="int16")
    sd.wait()
    wav.write("output.wav", sample_rate, recording)
    print("Распознаю речь...")
    recognizer = sr.Recognizer()
    with sr.AudioFile("output.wav") as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language=source_lang)
        print("Ты сказал:", text)
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        print("Перевод:", translated)
        return translated
    except sr.UnknownValueError:
        print("Не удалось распознать речь")
    except sr.RequestError as e:
        print(f"Ошибка API Google: {e}")

def play():
    words_1 = {
    "кот": "cat",
    "собака": "dog",
    "дом": "house",
    "машина": "car",
    "солнце": "sun"
}

    words_2 = {
        "радость": "joy",
        "путешествие": "travel",
        "решение": "solution",
        "знание": "knowledge",
        "дружба": "friendship"
    }

    words_3 = {
        "обстоятельство": "circumstance",
        "достопримечательность": "landmark",
        "благодарность": "gratitude",
        "предприятие": "enterprise",
        "воображение": "imagination"
    }

    print("Привет Это тренажёр английского.")
    print("1 - лёгкий")
    print("2 - средний")
    print("3 - сложный")
    level = int(input("Выбери уровень: "))

    if level == 1:
        words = words_1
    elif level == 2:
        words = words_2
    else:
        words = words_3

    rusian_list = list(words.keys())

    for i in range(3):
        rusian_word = random.choice(rusian_list)
        correct_english = words[rusian_word]  
        print("Раунд", i+1, "- переведи:", rusian_word)  
        speech_translate()

    print("Игра окончена")
if __name__ == '__main__':
    play()
