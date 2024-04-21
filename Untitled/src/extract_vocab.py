from transformers import BertTokenizer

def extract_vocab():
    tokenizer = BertTokenizer.from_pretrained("cl-tohoku/bert-base-japanese")
    with open("../vocab/chinese_vocab.txt", "w") as f:
        for k, v in tokenizer.get_vocab().items():
            f.write(f"{k}\n")
    print("Chinese vocab extracted.")

if __name__ == "__main__":
    extract_vocab()