---
license: mit
title: textcleaner-partha Demonstration
sdk: gradio
emoji: 🐢
colorFrom: indigo
colorTo: blue
thumbnail: >-
  https://cdn-uploads.huggingface.co/production/uploads/677150afdd9607b6253d0d09/KppB5b2f75cZAlMcdLjGL.jpeg
short_description: Demonstration of the textcleaner-partha Library.
sdk_version: 5.37.0
---
# 🧼 textcleaner-partha Demonstration

Welcome to the interactive Gradio demo of the `textcleaner-partha` Python library — developed by **Dr. Partha Majumdar** — for text preprocessing. This app allows users to clean and normalize raw text through a configurable pipeline using simple toggles. Whether you're a researcher, data scientist, or developer, you can quickly test the library’s capabilities with your own input or explore randomly selected examples.

---

## 🚀 Features

- **Two Modes of Use:**
  - 🎲 **Examples:** See the library in action on real-world examples with randomised settings.
  - 🧪 **Try Yourself:** Manually enter text and choose preprocessing options.

- **Text Preprocessing Options:**
  - Convert to lowercase
  - Remove Stop Words
  - Remove HTML tags
  - Remove emojis and symbols
  - Remove White Spaces
  - Remove Punctuations
  - Expand contractions (e.g., “don’t” → “do not”)
  - Expand abbreviations (e.g., “idk” → “I don’t know”)
  - Correct spellings using `autocorrect`
  - Lemmatise using `spaCy` (e.g., “running” → “run”)

---

## 📦 Requirements

The app relies on the following Python packages:

```txt
gradio>=4.16.0
spacy>=3.0.0
autocorrect>=2.6.1
contractions>=0.1.73
bs4>=0.0.1
textcleaner_partha>=0.3.2