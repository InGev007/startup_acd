class TextProcessor(object):
    def __init__(self):
        self.__punct_promt = ".,?!;:()'\"*/\\[]{}#@%&`"

    def __is_punctuation(self, char):
        return char in self.__punct_promt

    def get_clean_string(self, promt):
        text = ''
        for char in promt:
            if not self.__is_punctuation(char):
                text += char
        return text

# tp = TextProcessor()
# print(tp.get_clean_string("Hello World!!!!"))


class TextLoader:
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = ""

    def set_clean_text(self, promt):
        self.__clean_string = self.__text_processor.get_clean_string(promt)

    @property
    def clean_string(self):
        print(f"Очищенная строка: {self.__clean_string}")
        return self.__clean_string

# tl=TextLoader()
# tl.set_clean_text("Hello world!!")
# tl.clean_string()

class DataInterface:
    __text_loader = TextLoader()

    def process_texts(self, text):
        clean_text = []
        for line in text:
            self.__text_loader.set_clean_text(line)
            clean_line = self.__text_loader.clean_string
            clean_text.append(clean_line)
        return clean_text


# di = DataInterface()
# text = ["Hello World!!!!", "M@y Fr!end`s!!!"]
# di.process_texts(text)