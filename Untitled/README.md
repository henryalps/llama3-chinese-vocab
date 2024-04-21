<h1 align="center">

llama3-chinese-vocab

</h1>
<p align="center">
  <a href="https://img.shields.io/github/issues-pr/henryalps/llama3-chinese-vocab">
    <img src="https://img.shields.io/github/issues-pr/henryalps/llama3-chinese-vocab">
  </a>
  <a href="https://github.com/meta-llama/llama3/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/henryalps/llama3-chinese-vocab">
  </a>
</p>

本项目从llama3的`tokenizer.model`中导出全部中文词汇库，并进一步处理和训练。

## 目录结构

项目的目录结构如下：

- `src/`：这个目录包含所有的源代码文件。
- `extract_vocab.py`：这个脚本负责从llama3的tokenizer model中提取全部中文词汇，并将其输出为一个txt文件。
- `count_chinese.py`：这个脚本负责统计当前词汇库中的简体中文和繁体中文的数量。
- `enlarge_vocab.py`：这个脚本用于向当前的词汇库中添加额外的词语。
- `train_model.py`：这个脚本用于使用新的词汇库来训练一个新的模型。

- `vocab/`：这个目录中包含从模型中导出的词汇库的txt文件。
- `vocab.txt`：这里是从llama3的tokenizer model中导出的全部词汇库。
- `chinese_vocab.txt`：这里是从llama3的tokenizer model中导出的全部中文词汇库。
- `simplified_chinese_vocab.txt`：这里是统计后的简体中文词汇库。

- `models/`：这个目录用于存放模型。
- `tokenizer_model/`：这里是原始的llama3的tokenizer模型。
- `trained_model/`：这里是我们使用新的词汇库训练的模型。

- `README.md`：这里是项目的说明文件。

| 项目                        |   数量   |
|----------------------------|---------|
| 总词表大小（含特殊符号）      |  128256 |
| 总词表大小（不含特殊符号）    |  128000 |
| 中文词表大小                |   4132  |
| 简体中文词表大小            |   3543  |

## 使用方法

1. 首先运行 `extract_vocab.py` 从llama3的tokenizer model中提取全部中文词汇。

```python
python src/extract_vocab.py
```

2. 然后，运行 `count_chinese.py` 统计简体中文和繁体中文的数量，并导出简体中文词汇库。

```python
python src/count_chinese.py
```

3. 接下来，运行 `enlarge_vocab.py` 向词汇库中添加更多的词语。

```python
python src/enlarge_vocab.py
```

4. 最后，运行 `train_model.py` 使用新的词汇库训练一个新的模型。

```python
python src/train_model.py
```

然后，可以在 `models/trained_model/` 目录中找到训练过的模型。

## Liscense
![Meta Llama 3 Community License Agreement](https://github.com/meta-llama/llama3/blob/main/LICENSE)