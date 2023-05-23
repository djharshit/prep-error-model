# Preposition Error Detection ML Program

This is a machine learning program that uses the Natural Language Toolkit (NLTK) and the Random Forest algorithm to detect preposition errors in text. It is designed to help identify and correct preposition usage mistakes, which are common in writing and can affect the clarity and correctness of the text.
The program is trained on a labeled dataset of sentences, where each sentence is annotated with the correct usage of prepositions. The Random Forest algorithm is used to learn patterns and features from the data, enabling it to predict whether a given preposition in a sentence is used correctly or incorrectly.

## Features

- Accurately detects preposition errors in text.
- Easy-to-use command-line interface.
- Built using NLTK and scikit-learn.
- Trained on a large annotated dataset for improved accuracy.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/djharshit/preposition-error-detection.git
   cd preposition-error-detection
   ```

2. Create a virtual environment (optional but recommended):

   ```shell
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

<a href="https://preposition.djharshit.app" target="_blank"><img src="https://www.transparentpng.com/thumb/click-here-button/Gaezhb-click-here-button-images-png.png" height=100 width=100></img></a>

The program will analyze the sentences and output the detected preposition errors along with their suggested corrections.

## Example

Consider the following input sentence:

```text
I will meet you in the restaurant at 7 PM.
```

The program will identify the error in the preposition "in" and suggest the correct usage:

```text
Error: 'in' should be 'at'
```

## Deploying on Google Cloud

This program can be deployed on Google Cloud Platform (GCP) to make it accessible as an API or a web service. Follow these steps to deploy on GCP:

1. Set up a Google Cloud project and enable the necessary APIs (e.g., Cloud Functions, App Engine).
2. Create a deployment package by including the program files and dependencies.
3. Deploy the program on GCP using either Cloud Functions or App Engine.
4. Configure the necessary endpoints and permissions for accessing the deployed program.

## Acknowledgments

This project was developed using the NLTK library and scikit-learn. We would like to acknowledge the contributions of the open-source community and the developers of these libraries. Thank you!
