from googletrans import Translator

class Simple_Translator(object):
    def __init__(self, word, language):
        self.word = word
        self.language = language
        self.cursor = Translator(service_urls=["translate.google.com"])

    def __repr__(self):
        translation = self.cursor.translate(self.word, dest=self.language)
        translation = str(f"Translation:\n -- {translation.text}")
        return translation

if __name__ == '__main__':
    print("Enter a string to translate: ")
    sentence = input(" -- ")
    translation = Simple_Translator(sentence, "fr")
    print(translation)
