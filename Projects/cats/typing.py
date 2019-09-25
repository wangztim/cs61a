"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    selectable_paragraphs = []
    for paragraph in paragraphs:
        if select(paragraph) == True:
            selectable_paragraphs.append(paragraph)
    if len(selectable_paragraphs) > k:
        return selectable_paragraphs[k]
    else:
        return ""
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def check_if_about(paragraph):
        paragraph_in_lower_case = lower(paragraph)
        lower_case_paragraph_without_punc = remove_punctuation(
            paragraph_in_lower_case)
        words_of_paragraph = split(lower_case_paragraph_without_punc)
        for keyword in topic:
            if keyword in words_of_paragraph:
                return True
        return False

    return check_if_about
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    num_typed_words = len(typed_words)
    if num_typed_words == 0:
        return 0.0
    smaller_len = min(num_typed_words, len(reference_words))
    corrects = 0
    for i in range(0, smaller_len):
        typed_word = typed_words[i]
        reference_word = reference_words[i]
        if typed_word == reference_word:
            corrects += 1
    return (corrects / num_typed_words) * 100

    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    num_chars = len(typed)
    num_words = num_chars / 5

    return num_words * (60 / elapsed)
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than or equal to LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word
    else:
        lowest_diff = float('inf')
        best_word = ""
        for word in valid_words:
            difference = diff_function(user_word, word, limit)
            if (difference == True):
                difference = 1
            if (difference == False):
                difference = 0
            if (difference < lowest_diff):
                lowest_diff = difference
                best_word = word
        if lowest_diff > limit:
            return user_word
        else:
            return best_word
        # END PROBLEM 5


def swap_diff(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    trimmed_start = start[1:] if len(start) > 1 else ""
    trimmed_goal = goal[1:] if len(goal) > 1 else ""

    if start == goal:
        return 0
    elif len(start) == 0 or len(goal) == 0:
        return max(len(start), len(goal))
    elif limit == 0:
        return float('inf')
    elif start[0] == goal[0]:
        return swap_diff(trimmed_start, trimmed_goal, limit)
    else:
        return 1 + swap_diff(trimmed_start, trimmed_goal, limit - 1)
    # END PROBLEM 6


def edit_diff(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    trimmed_start = start[1:] if len(start) > 1 else ""
    trimmed_goal = goal[1:] if len(goal) > 1 else ""

    if start == goal:
        return 0

    elif len(start) == 0 or len(goal) == 0:
        return max(len(start), len(goal))

    elif limit == 0:
        return float('inf')

    elif start[0] == goal[0]:
        return edit_diff(trimmed_start,  trimmed_goal, limit)

    else:
        add_diff = edit_diff(start, trimmed_goal, limit - 1)
        remove_diff = edit_diff(trimmed_start, goal, limit - 1)
        substitute_diff = edit_diff(trimmed_start, trimmed_goal, limit - 1)
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 1 + min(add_diff, remove_diff, substitute_diff)
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    words_correct = 0
    for i in range(len(typed)):
        if i < len(prompt):
            if typed[i] == prompt[i]:
                words_correct += 1
            else:
                break
    words_accuracy = words_correct / len(prompt)
    send({"id": id, "progress": words_accuracy})
    return words_accuracy
    # END PROBLEM 8


def fastest_words_report(word_times):
    """Return a text description of the fastest words typed by each player."""
    fastest = fastest_words(word_times)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def fastest_words(word_times, margin=1e-5):
    """A list of which words each player typed fastest."""
    n_players = len(word_times)
    n_words = len(word_times[0]) - 1
    assert all(len(times) == n_words + 1 for times in word_times)
    assert margin > 0
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    best_scores = []
    for i in range(n_players):
        best_scores.append([])

    def find_diff_in_time(prev_list, curr_list):
        current_elapsed_time = elapsed_time(curr_list)
        previous_elapsed_time = elapsed_time(prev_list)
        diff = current_elapsed_time - previous_elapsed_time
        return abs(diff)

    for typed_word in range(1, n_words + 1):
        fastest_speed = float('inf')
        for player in range(n_players):
            current_word_list = word_times[player][typed_word]
            previous_word_list = word_times[player][typed_word - 1]
            diff = find_diff_in_time(previous_word_list, current_word_list)
            if diff < fastest_speed:
                fastest_speed = diff

        for player in range(n_players):
            current_word_list = word_times[player][typed_word]
            previous_word_list = word_times[player][typed_word - 1]
            diff = find_diff_in_time(previous_word_list, current_word_list)
            if (abs(diff - fastest_speed) <= margin) == True:
                best_scores[player].append(word(current_word_list))

    return best_scores
    # END PROBLEM 9


def word_time(word, elapsed_time):
    """A data abstrction for the elapsed time that a player finished a word."""
    return [word, elapsed_time]


def word(word_time):
    """An accessor function for the word of a word_time."""
    return word_time[0]


def elapsed_time(word_time):
    """An accessor function for the elapsed time of a word_time."""
    return word_time[1]


enable_multiplayer = False  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    def select(p): return True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
