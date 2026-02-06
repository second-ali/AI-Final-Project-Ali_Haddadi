# Binary Sentiment Classification (Persian)

This repository contains an implementation of **binary sentiment analysis** for Persian text using deep learning.  
The workflow and experiments are implemented in the `BinaryClassification.ipynb` notebook.

---

## Overview

The goal of this project is to classify Persian sentences into **positive** or **negative** sentiment classes.  
Neutral samples (label = 0) are removed, and the remaining labels are mapped as:

- **Positive sentiment** → `1`
- **Negative sentiment** → `0`

The model is trained and evaluated on preprocessed Persian text using Keras and TensorFlow.

---

## Requirements

Install the required libraries before running the notebook:

```bash
pip install hazm
pip install stopwords_guilannlp
pip install pandas
pip install tensorflow
```

---

## Libraries Used

- **TensorFlow / Keras** – Deep learning framework
- **Hazm** – Persian text normalization, tokenization, and lemmatization
- **Pandas / NumPy** – Data handling
- **Scikit-learn** – Evaluation metrics
- **Matplotlib** – Data visualization

---

## Dataset

Multiple datasets are loaded, but one is selected for training at a time:

- `original.csv`
- `balanced.csv`
- `translation.csv` (used by default)

Each dataset contains:
- Column 0: Persian sentence
- Column 1: Sentiment label (`-1`, `0`, `+1`, etc.)

### Dataset Statistics

- **Training samples:** 14,046  
- **Testing samples:** 1,854  

After filtering neutral samples:
- Labels are converted to binary classes (positive / negative).

A pie chart is used to visualize class distribution in the training set.

---

## Preprocessing Pipeline

Text preprocessing is performed using Hazm and includes:

1. Normalization
2. Tokenization
3. Punctuation removal
4. Removal of short tokens and digits
5. Lemmatization

```python
Normalizer → Tokenizer → Cleaning → Lemmatization
```

---

## Tokenization & Padding

- A Keras `Tokenizer` is fitted on training data
- Maximum sentence length is computed from training samples
- Sequences are padded using `post` padding
- The tokenizer is saved for later inference

```python
tokenizer.pkl
```

---

## Emotion Analysis (Multi-class)

In addition to binary sentiment classification, this repository also includes a **multi-class emotion analysis** approach for Persian text, implemented in the `EmotionAnalysis.ipynb` notebook.

### Task Description

The goal of this method is to classify Persian sentences into **fine-grained emotion categories** rather than only positive/negative sentiment.  
Samples labeled as `OTHER` are removed to focus on explicit emotional expressions.

### Emotion Labels

The dataset contains multiple discrete emotion classes (e.g. joy, anger, sadness, fear, etc.), provided in TSV format:

- `train.tsv`
- `test.tsv`

Each file contains:
- Column 0: Persian text
- Column 1: Emotion label

---

## Preprocessing Pipeline (Emotion Analysis)

A more advanced preprocessing pipeline is applied compared to binary sentiment classification:

1. Stop-word removal
2. Emoji normalization (Persian demojization)
3. URL, mention, and punctuation removal
4. Removal of English tokens
5. Formalization of informal Persian text (Hazm InformalNormalizer)
6. Text normalization and cleaning
7. Removal of empty samples

This pipeline is designed to handle **informal Persian social media text** effectively.

---