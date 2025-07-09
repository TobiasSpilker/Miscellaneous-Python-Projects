# 🧠 Natural-Language-Processing-Various-Projects

This repository is a curated collection of NLP and ML experiments, tools, and assignments developed by **Tobias Spilker** as part of academic coursework and personal learning. It covers a variety of topics, from named entity recognition and language identification to string manipulation and early machine learning models.

---

## 📂 Contents

| Category | Project |
| -------- | ------- |
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
~~~bash
python build_models.py
python evaluate_models.py
~~~

> 📦 Dependencies: `nltk`, `conll2002`

---

## 📊 Alice Word Frequency

**File**: `alice.py`

This script analyzes the *Alice in Wonderland* text from the Gutenberg corpus and prints the **five most common words** that follow the word `"Alice"`.

**🔍 Example Output:**
~~~text
alice said 35
alice was 28
alice had 19
...
~~~

> 📦 Dependencies: `nltk`, `gutenberg corpus`

---

## 📊 POS Tag Frequency

**File**: `categories.py`

Command-line utility that prints part-of-speech tag frequencies for one or more input words using the **Brown corpus** and the **Universal tagset**.

**💻 Example:**
~~~bash
python categories.py run fast happy
~~~

> 📦 Dependencies: `nltk`, `brown corpus`

---

## 📊 Nth Word/Char Utilities

**File**: `nth.py`

Simple string manipulation utilities:

* `nth_char(index, string)` – get the nth character  
* `nth_word(index, string)` – get the nth word  
* `nth_of_mth(char_index, word_index, string)` – get a character in a specific word  

> Used as a Python module, not a script.

---

## 🌍 N-Gram-Based Language Identifier

A basic language recognizer that uses **character n-gram frequency profiles** and **cosine similarity** to identify the language of a given text.

**📁 Files:**
* `write_profiles.py` – Generates language profiles from training text  
* `evaluate.py` – Tests recognition accuracy on labeled samples  
* `langdetect.py` – Core n-gram functions (WIP)  
* `match_language.py` – CLI interface for language recognition  

**📁 Expected folder structure:**
~~~text
./datafiles/
├── training/
└── testing/
~~~

> 📦 Dependencies: `os`, `math`, `re`

---

## 🧪 Perceptron Learning Algorithm (Incomplete)

**File**: `Programmeer opdracht 1.py`

An unfinished attempt to implement the **Perceptron Learning Algorithm** (PLA) for binary classification. Includes:

* `sign()`, `initialize_weights()`  
* `perceptron()` hypothesis function (incomplete)  
* `update_weights()`  
* `learn_weights()` (stub)  

**🚧 Known Issues:**
* Contains syntax errors (e.g., `return h = ...`)  
* Needs control loop and test cases  

---

## 📦 Requirements

Install the required libraries using:
~~~bash
pip install nltk
python -m nltk.downloader brown gutenberg conll2002
~~~

---

## 👨‍🎓 Author

**Tobias Spilker**  
Bachelor Student in Artificial Intelligence  
Utrecht University

---

## 📄 License

This project is for educational and personal use. Contact for reuse or commercial inquiries.
