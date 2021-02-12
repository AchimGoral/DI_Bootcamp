import string
# import nltk
# nltk.download('stopwords')
# from nltk.corpus import stopwords
# stopwords.words('english')

with open('the_stranger.txt', 'r') as f:
    data = f.readlines()
string = ''
string += ''.join(data)


class Text:

    def __init__(self, string):
        self.string = string

    def frequency(self, word):
        count_word = self.string.count(word)
        if count_word == 0:
            return "There are no words like this"
        else:
            return f"{count_word} words like {word} are in this text"

    def most_common(self):
        word_counter = dict()
        sentence_list = self.string.split()
        for word in sentence_list:
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1
        max_occ = max(word_counter.values())

        return [(word, occ) for word, occ in word_counter.items() if occ == max_occ]

    def unique(self):
        unique_words = dict()
        sentence_list = self.string.split()
        for word in sentence_list:
            if not word in unique_words:
                unique_words[word] = 1
            else:
                unique_words[word] = unique_words[word] + 1

        return [key for key, value in unique_words.items() if value == 1]

    @staticmethod
    def from_file(str_input):
        with open(str_input, 'r') as f:
            data = f.readlines()
        output_file = ''
        output_file += ''.join(data)

        return output_file


class TextModification(Text):

    def __init__(self, string):
        super().__init__(string)

    def punct(self):
        punctuations = '''?!()-[]{};:'",.'''
        no_punctuation = ''

        for letter in self.string:
            if letter not in punctuations:
                no_punctuation += letter

        return no_punctuation

    def stop_words(self):
        clean_text = self.punct()
        pass
        # nltk not working