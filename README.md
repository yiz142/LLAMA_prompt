# LLAMA Model Classification Project

## Project Overview
This project explores the use of LLAMA models from SambaNova's prompting API for classification tasks across various datasets from the XClass repository. We aim to evaluate the performance of different prompting methods using 1B, 3B, and 8B LLAMA models, comparing accuracy under multiple prompt strategies.

# Installation
To set up your environment and install the necessary dependencies, run the following command from the root directory of the project:

pip install -r requirements.txt
Ensure you have all dependencies, including the OpenAI library and any required packages for data handling and model evaluation.

# Datasets
This project uses datasets from the XClass repository. Each dataset has multiple classes, and we will randomly sample data for testing.

# API Key Setup
Ensure your API key for SambaNova is set as an environment variable:
export SAMBANOVA_API_KEY="your-api-key-here"
