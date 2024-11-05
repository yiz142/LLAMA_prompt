# LLAMA Model Classification Project

## Project Overview
This project explores the use of LLAMA models from SambaNova's prompting API for classification tasks across various datasets from the XClass repository. We aim to evaluate the performance of different prompting methods using 1B, 3B, and 8B LLAMA models, comparing accuracy under multiple prompt strategies.

# Installation
To set up your environment and install the necessary dependencies, run the following command from the root directory of the project:

pip install -r requirements.txt
Ensure you have all dependencies, including the OpenAI library and any required packages for data handling and model evaluation.

# Datasets
This project uses datasets from the XClass repository. Each dataset has multiple classes, and we will randomly sample data for testing.

# Running the code 
To run the project, use the run.py script. Make sure to specify your chosen dataset and prompting method.

# API Key Setup
API Key Setup
You need an API key from SambaNova to make API requests. Follow these steps to get your API key:

Visit SambaNova's website and sign up or log in.
Once logged in, generate an API key from your account dashboard.
Ensure your API key for SambaNova is set as an environment variable:
export SAMBANOVA_API_KEY="your-api-key-here"
