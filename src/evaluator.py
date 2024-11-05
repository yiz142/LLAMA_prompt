from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

def create_prompt(text, topics):
    return f"Classify the following text into one of the categories: {', '.join(topics)}. Text: {text}"

def map_response_to_label(response, topics):
    if response in topics:
        return topics.index(response)
    return -1

def evaluate_metrics(sampled_data, phrases, topics_labels, topics, call_api_function):
    y_true = []  # Ground truth labels
    y_pred = []  # Predicted labels

    # Generate predictions and collect true labels
    for text in sampled_data:
        prompt = create_prompt(text, topics)
        response = call_api_function(prompt)
        predicted_label = map_response_to_label(response, topics)
        actual_label = topics_labels[phrases.index(text)]

        y_true.append(actual_label)
        y_pred.append(predicted_label)

    # Calculate metrics
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted')
    recall = recall_score(y_true, y_pred, average='weighted')
    f1 = f1_score(y_true, y_pred, average='weighted')

    # Print metrics
    print(f"Accuracy: {accuracy:.2%}")
    print(f"Precision: {precision:.2%}")
    print(f"Recall: {recall:.2%}")
    print(f"F1 Score: {f1:.2%}")
