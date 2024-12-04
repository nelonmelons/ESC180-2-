'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 20, 2023.
'''

import math

def norm(vec):
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    return math.sqrt(sum_of_squares)

def cosine_similarity(vec1, vec2):
    dot_product = 0.0
    for key in vec1:
        if key in vec2:
            dot_product += vec1[key] * vec2[key]
    norm_u = norm(vec1)
    norm_v = norm(vec2)
    if norm_u == 0 or norm_v == 0:
        return -1  # Cannot compute similarity
    return dot_product / (norm_u * norm_v)

def build_semantic_descriptors(sentences):
    d = {}
    for sentence in sentences:
        words_in_sentence = set(sentence)
        for word in words_in_sentence:
            if word not in d:
                d[word] = {}
            for other_word in words_in_sentence:
                if other_word != word:
                    d[word][other_word] = d[word].get(other_word, 0) + 1
    return d

def build_semantic_descriptors_from_files(filenames):
    text = ""
    for filename in filenames:
        with open(filename, "r", encoding="latin1") as f:
            text += f.read()
    text = text.replace("\n", " ")
    sentence_endings = [".", "!", "?"]
    for sep in sentence_endings:
        text = text.replace(sep, ".")
    punctuation = [",", "-", "--", ":", ";"]
    for p in punctuation:
        text = text.replace(p, " ")
    text = text.lower()
    sentences = text.split(".")
    sentences_list = []
    for sentence in sentences:
        words = sentence.split()
        if words:
            sentences_list.append(words)
    return build_semantic_descriptors(sentences_list)

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    max_similarity = -1
    best_choice = choices[0]
    for choice in choices:
        if word in semantic_descriptors and choice in semantic_descriptors:
            similarity = similarity_fn(semantic_descriptors[word], semantic_descriptors[choice])
            if similarity > max_similarity:
                max_similarity = similarity
                best_choice = choice
        else:
            similarity = -1
    return best_choice

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    total_questions = 0
    correct_guesses = 0
    with open(filename, "r", encoding="latin1") as f:
        for line in f:
            tokens = line.strip().split()
            if len(tokens) < 3:
                continue
            word = tokens[0]
            correct_answer = tokens[1]
            choices = tokens[2:]
            guess = most_similar_word(word, choices, semantic_descriptors, similarity_fn)
            if guess == correct_answer:
                correct_guesses += 1
            total_questions += 1
    if total_questions == 0:
        return 0.0
    percentage = (correct_guesses / total_questions) * 100
    return percentage
