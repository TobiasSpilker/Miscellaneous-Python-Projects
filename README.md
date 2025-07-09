# 🧠 Natural-Language-Processing-Various-Projects

This repository is a curated collection of NLP and ML experiments, tools, and assignments developed by **Tobias Spilker** as part of academic coursework and personal learning. It covers a variety of topics, from named entity recognition and language identification to string manipulation and early machine learning models.

---

## 📂 Contents

| Category | Project |
|---------|---------|
| 🧠 NLP Models | [NER Chunker with NLTK Classifier](#ner-chunker-with-nltk-classifier) |
| 📊 NLP Scripts | [Alice Word Frequency](#alice-word-frequency)<br>[POS Tag Frequency](#pos-tag-frequency)<br>[Nth Word/Char Utilities](#nth-wordchar-utilities) |
| 🌍 Language ID | [N-Gram-Based Language Identifier](#n-gram-based-language-identifier) |
| 🧪 ML Experiment | [Perceptron Learning Algorithm (Incomplete)](#perceptron-learning-algorithm-incomplete) |

---

## 🧠 NER Chunker with NLTK Classifier

Implements a Named Entity Recognition (NER) chunker using NLTK’s classifier framework. Models are trained on the Dutch **CoNLL-2002** dataset using a variety of feature maps and algorithms.

**📁 Files:**
- `custom_chunker.py` – NLTK-based chunker and tagger implementation
- `features.py` – Multiple feature map configurations (POS, word shape, context)
- `build_models.py` – CLI-based training and model pickling tool
- `evaluate_models.py` – CLI-based model evaluation (pirate-themed!)
- `model_test (2).py` – Load and evaluate model on CoNLL data

**📌 Features:**
- Classifiers: Naive Bayes, Decision Tree, MaxEnt (IIS/GIS)
- Train and evaluate models interactively
- Supports multiple feature engineering options
- Uses standard CoNLL-2002 corpus from `nltk`

**💻 Example:**
```bash
python build_models.py
python evaluate_models.py
