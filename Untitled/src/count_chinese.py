import re
import opencc
def is_traditional_chinese(text):
    cc = opencc.OpenCC('t2s')
    converted_text = cc.convert(text)
    if converted_text != text:
        return True
    return False
def count_chinese():
    with open("../vocab/chinese_vocab.txt", "r") as f:
        vocab = f.readlines()
    simplified = []
    for word in vocab:
        if not is_traditional_chinese(word.strip()):
            simplified.append(word)
    with open("../vocab/simplified_chinese_vocab.txt", "w") as f:
        for word in simplified:
            f.write(f"{word}\n")
    print("Finished counting Simplified Chinese vocab.")

if __name__ == "__main__":
    count_chinese()