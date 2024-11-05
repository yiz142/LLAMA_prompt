import os

base_dir = "data/nyt_data"  # Updated to nyt_data

def load_data(file_name):
    file_path = os.path.join(base_dir, file_name)
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def load_all_data():
    labels = load_data("label.txt")
    location_labels = [int(label) for label in load_data("locations_label.txt")]
    locations = load_data("locations.txt")
    phrases = load_data("phrase_text.txt")
    topics_labels = [int(label) for label in load_data("topics_label.txt")]
    topics = load_data("topics.txt")
    return labels, location_labels, locations, phrases, topics_labels, topics
