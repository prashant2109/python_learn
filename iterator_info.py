class myRange:
    def __init__(self, start, end):
        self.start = start
        self.end   = end

    def __iter__(self):
        return self

    def __next__(self):
        current_value = self.start
        if self.start >= self.end:
            raise StopIteration
        self.start += 1
        return current_value

class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.words = self.sentence.split()
        self.cnt = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.cnt >= len(self.words):
            raise StopIteration
        val = self.words[self.cnt]
        self.cnt += 1
        return val
        

if __name__ == '__main__':
    # s_Obj = Sentence('Hey! Howz going?')    
    # for j in s_Obj:
    #     print(j)
    #########################################################
    # mr_Obj = myRange(0, 5)
    # for i in mr_Obj:
    #     print(i)