def enlarge_vocab():
    # suppose we have a list of words to add
    new_words = ["新增词语1", "新增词语2", "新增词语3"]
    with open("../vocab/simplified_chinese_vocab.txt", "a") as f:
        for word in new_words:
            f.write(f"{word}\n")
    print("Vocab enlarged with new words.")

if __name__ == "__main__":
    enlarge_vocab()