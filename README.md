# AI Companion

AI Companion is a web application that allows you to chat with an artificial intelligence agent that can help you with various tasks. You can customize the agent's personality and skills by changing the prompt in the `config.py` file. In this example, we have AVA, a quality assurance companion that helps you debug and understand code in any given language. AVA uses the OpenAI model to generate natural language responses based on your input.

## Features

- Chat with AVA, a quality assurance companion that can help you with coding problems
- Ask AVA questions about syntax, logic, errors, or best practices in any programming language
- Get feedback and suggestions from AVA on how to improve your code quality and performance
- Learn from AVA's explanations and examples on how to solve common coding challenges

## Installation

To run this application, you need to have Python 3.8 or higher and Streamlit installed on your system. You also need to have an OpenAI API key to access the OpenAI model. You can get one from https://openai.com/.

### For Mac

- Open a terminal and navigate to the directory where you want to clone this repository
- Run the following command to clone this repository:

    ```bash
    git clone https://github.com/aiproduct-creators/ai-companion.git
    ```
- Navigate to the cloned repository:

    ```
    cd ai-companion
    ```
- Create a virtual environment and activate it:
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
- Install the required packages:
    ```
    pip install -r requirements.txt
    ```
- Set your OpenAI API key as an environment variable:
    ```
    export OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    ```
- Run the streamlit app:
    ```
    streamlit run companion.py
    ```
    Open your browser and go to http://localhost:8501 to see the app

### For Windows
Open a command prompt and navigate to the directory where you want to clone this repository

- Run the following command to clone this repository:
```
git clone https://github.com/aiproduct-creators/ai-companion.git
```
- Navigate to the cloned repository:

    ```
    cd ai-companion
    ```
- Create a virtual environment and activate it:
    ```
    python -m venv venv
    venv\Scripts\activate
    ```
- Install the required packages:
    ```
    pip install -r requirements.txt
    ```
- Set your OpenAI API key as an environment variable:
    ```
    set OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    ```
- Run the streamlit app:
    ```
    streamlit run companion.py
    ```
Open your browser and go to http://localhost:8501 to see the app
