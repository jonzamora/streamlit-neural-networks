# Streamlit Apps for Neural Networks

## Introduction

I am using this repository to experiment with [Streamlit](https://streamlit.io/), an open-source Python library which makes it easy to create and share elegant, custom web apps for Machine Learning and Data Science.

I'm hoping to implement some simple Streamlit apps for Neural Networks which can help me (and hopefully others) with their development and understanding of Neural Networks.

## Getting Started

### Step 1: Mamba Package Manager

I use the [Mamba](https://mamba.readthedocs.io/en/latest/index.html) package manager for Python. You can install it on your machine (if not installed already) prior to running any code from this repository.

### Step 2: Setting up your Environment

Next, you'll want to create an environment with Mamba for running your Python code. I've provided the commands for doing this below:

```bash
mamba create -n streamlit python=3.10
mamba activate streamlit
pip install streamlit watchdog
```

### Step 3: Running a Streamlit App

From your terminal, run the following command:

```bash
streamlit run src/main-concepts/1-displaying-data.py
```

You will be provided with a Local URL and Network URL from Streamlit to view the app in your browser. Both URLs should work.

## Note

This is an in-progress repository! I will be periodically working on this project. Stay tuned!