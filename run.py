import time
from src.data_loader import load_all_data
from src.sampler import create_topic_to_phrases_mapping, sample_multiple_sets
from src.api_client import initialize_client, call_api
from src.evaluator import evaluate_metrics

def main():
    # Load data
    labels, location_labels, locations, phrases, topics_labels, topics = load_all_data()

    # Create topic-to-phrases mapping
    topic_to_phrases = create_topic_to_phrases_mapping(phrases, topics_labels, topics)

    # Generate 20 sets of 10 samples
    sampled_data_sets = sample_multiple_sets(topic_to_phrases, num_sets=20, samples_per_set=10)

    # List of models to evaluate
    models = [
        "Meta-Llama-3.2-1B-Instruct",
        "Meta-Llama-3.2-3B-Instruct",
        "Meta-Llama-3.2-8B-Instruct"
    ]

    # Loop through each model and evaluate
    for model in models:
        print(f"\nEvaluating model: {model}")
        # Initialize the client and update the model in the parameters
        client, params = initialize_client()
        params["model"] = model  # Update the model in the parameters

        # Evaluate metrics for each set
        for i, sampled_data in enumerate(sampled_data_sets):
            print(f"\nEvaluating set {i + 1} with {model}...")
            # Call the API and evaluate metrics
            evaluate_metrics(
                sampled_data,
                phrases,
                topics_labels,
                topics,
                lambda prompt: call_api(client, prompt, params)
            )
            # Pause for 1 second between API requests
            time.sleep(1)

if __name__ == '__main__':
    main()
