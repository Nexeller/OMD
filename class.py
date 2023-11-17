class CountVectorizer:
    def __init__(self):
        self.vocab = {}  # словарь для подсчета частоты каждого слова
        self.features = []  # список для хранения уникальных слов.

    def fit_transform(self, corpus):
        for text in corpus:
            for word in text.lower().split():  # преобразуется в нижний регистр и разбивается на слова
                if word not in self.vocab:
                    self.vocab[word] = 1
                    self.features.append(word)
                else:
                    self.vocab[word] += 1
        matrix = [[text.lower().split().count(word) for word in self.features] for text in corpus]

        return matrix

    # метод возвращает список уникальных слов
    def get_feature_names(self):
        return self.features

if __name__ == "__main__":
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste"
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
