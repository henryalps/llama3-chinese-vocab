from transformers import BertTokenizer, BertForMaskedLM
from torch.optim import Adam
import torch

def train_model(pretrained_model):
    tokenizer = BertTokenizer.from_pretrained("../vocab", max_len=512)
    model = BertForMaskedLM.from_pretrained(pretrained_model)

    # suppose we have some data to use
    data = ["这是一个训练样例。", "这是另一个训练样例。"]

    optimizer = Adam(model.parameters(), lr=1e-5)
    model.train()

    for epoch in range(1, 3):  # loop over the dataset multiple times
        for sentence in data:
            inputs = tokenizer(sentence, return_tensors="pt")
            outputs = model(**inputs)
            loss = outputs.loss
            loss.backward()  # calculate the grdients
            optimizer.step()  # update the weights
            optimizer.zero_grad()  # clear the gradients for the next step

    model.save_pretrained("../models/trained_model")
    print("Model trained and saved.")

if __name__ == "__main__":
    train_model()