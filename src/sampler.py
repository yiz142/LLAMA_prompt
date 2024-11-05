import random

def create_topic_to_phrases_mapping(phrases, topics_labels, topics):
    topic_to_phrases = {i: [] for i in range(len(topics))}
    for i, label in enumerate(topics_labels):
        topic_to_phrases[label].append(phrases[i])
    return topic_to_phrases

def sample_multiple_sets(topic_to_phrases, num_sets=20, samples_per_set=10):
    """
    Generate multiple sets of samples from the topic-to-phrases mapping.

    :param topic_to_phrases: Dictionary mapping each topic to a list of phrases.
    :param num_sets: Number of sets to generate.
    :param samples_per_set: Number of samples per set.
    :return: A list of sets, where each set is a list of sampled phrases.
    """
    all_sampled_sets = []
    for _ in range(num_sets):
        sampled_set = []
        for label, texts in topic_to_phrases.items():
            sampled_set.extend(random.sample(texts, min(samples_per_set, len(texts))))
        all_sampled_sets.append(sampled_set)
    return all_sampled_sets
