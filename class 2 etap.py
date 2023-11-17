import math
class CountVectorizer: # для подсчета частоты слов в корпусе текстов.
    def __init__(self):
        self.vocab = {} # словарь для подсчета частоты каждого слова
        self.features = []  # список для хранения уникальных слов.
    def fit_transform(self, corpus):
        for text in corpus:
            for word in text.lower().split(): # преобразуется в нижний регистр и разбивается на слова
                if word not in self.vocab:
                    self.vocab[word] = 1
                    self.features.append(word)
                else:
                    self.vocab[word] += 1
        matrix = [[text.lower().split().count(word) for word in self.features] for text in corpus]

        return matrix
    def get_feature_names(self):
        return self.features
    def get_feature_names(self):
        return self.features
class TfTransformer: # для преобразования матрицы частот слов в матрицу TF
    def tf_transform(self, count_matrix):
        return [[round(word / sum(doc), 3) for word in doc] for doc in count_matrix]
class IdfTransformer:
    def idf_transform(self, count_matrix):
        num_docs = len(count_matrix)
        word_presence = [sum(1 for doc in count_matrix if doc[i] > 0) for i in range(len(count_matrix[0]))]

        return [round(math.log((num_docs / presence) + 1), 3) for presence in word_presence]

class TfidfTransformer:
    def __init__(self):
        self.tf_transformer = TfTransformer()
        self.idf_transformer = IdfTransformer()

    def fit_transform(self, count_matrix):
        tf = self.tf_transformer.tf_transform(count_matrix) # вычисляем значения TF и IDF для создания матрицы TF*IDF.
        idf = self.idf_transformer.idf_transform(count_matrix)
        tfidf = [[round(tf_val * idf[i], 3) for i, tf_val in enumerate(doc)] for doc in tf]
        return tfidf

class TfidfVectorizer(CountVectorizer): # наследует от CountVectorizer
    def __init__(self):
        super().__init__()
        self.tfidf_transformer = TfidfTransformer()

    def fit_transform(self, corpus):
        count_matrix = super().fit_transform(corpus)
        return self.tfidf_transformer.fit_transform(count_matrix)

corpus = [
    "Crock Pot Pasta Never boil pasta again",
    "Pasta Pomodoro Fresh ingredients Parmesan to taste"
]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
print(tfidf_matrix)

