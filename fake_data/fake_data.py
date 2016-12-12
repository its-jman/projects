from __future__ import division
from random import sample, randint
from numpy import random

# The number of questions in the test (eg. 100%)
test_max = 30

# Number of students to generate
number_students = 1000

# List of majors to select from
majors = ['AE', 'ACC', 'CIS', 'ANTH', 'ART', 'BIO', 'CHEM', 'DANCE', 'ENGL', 'GEO', 'LAW', 'MATH']
genders = ['male', 'female']


def get_header_names(title):
    """
    used to get the headers for each question (with prefix)

    :param title: Prefix to use
    :return:list of headers
    """
    out = []
    for i in range(1, test_max + 1):
        out.append(title + 'Question ' + str(i))
    return out


# Headers for the beginning of the file
first_headers = ['Student ID', 'Course Grade', 'Major', 'Gender', 'Pre Score Raw']
headers = first_headers + get_header_names('') + ['Post Score Raw'] + get_header_names('Post ')

# [PRE, POST] mean score for the class. (eg. [14, 26])
mean_scores = sorted(sample(xrange(10, test_max), 2))


def make_student_list(student_count):
    """
    creates students along with their pre and post raw scores

    :param student_count: number of students to create
    :return: [student id, PRE raw score, POST raw score]
    """

    # Randomly generated (not repeating) 9 digit id's (eg. 385652307)
    student_ids = sample(xrange(100000000, 999999999), student_count)

    def check_x(x):
        """
        Filters and fixes any data that is outside of the boundries of (0 to test_max)
        :param x: number to check
        :return:the corrected/unchanged answer
        """

        # the randomness is used to prevent a large spike at the max/min values
        if x > test_max:
            return test_max - randint(0, 7)
        if x < 0:
            return randint(0, 7)
        return x

    # normal distribution of scores capped within boudries of possible scores
    pre_list = map(
        lambda x: check_x(int(x)),
        random.normal(mean_scores[0], 7, student_count)
    )
    post_list = map(
        lambda x: check_x(int(x)),
        random.normal(mean_scores[1], 7, student_count)
    )

    # Attaches each student to their corresponding random pre and post score as a tuple (eg. (609089949, 18, 30))
    return zip(student_ids, pre_list, post_list)


# FCI key data from server. Needs to be sorted/selected. This contains the correct pre and post data
unsorted_js = {"_id": "ObjectId(\"547338c7530790dba41c4fb1\")", "AssessmentId": 5,
               "Key": {"Post Q13": {"Answer": "4", "Weight": 1}, "Post Q21": {"Answer": "5", "Weight": 1},
                       "Post Q17": {"Answer": "2", "Weight": 1}, "Post Q20": {"Answer": "4", "Weight": 1},
                       "Post Q24": {"Answer": "1", "Weight": 1}, "Post Q30": {"Answer": "3", "Weight": 1},
                       "Post Q25": {"Answer": "3", "Weight": 1}, "Post Q8": {"Answer": "2", "Weight": 1},
                       "Post Q9": {"Answer": "5", "Weight": 1}, "Post Q10": {"Answer": "1", "Weight": 1},
                       "Post Q2": {"Answer": "1", "Weight": 1}, "Post Q3": {"Answer": "3", "Weight": 1},
                       "Post Q1": {"Answer": "3", "Weight": 1}, "Post Q6": {"Answer": "2", "Weight": 1},
                       "Post Q7": {"Answer": "2", "Weight": 1}, "Post Q4": {"Answer": "5", "Weight": 1},
                       "Post Q5": {"Answer": "2", "Weight": 1}, "Pre Q30": {"Answer": "3", "Weight": 1},
                       "Post Q27": {"Answer": "3", "Weight": 1}, "Pre Q18": {"Answer": "2", "Weight": 1},
                       "Pre Q19": {"Answer": "5", "Weight": 1}, "Post Q18": {"Answer": "2", "Weight": 1},
                       "Post Q19": {"Answer": "5", "Weight": 1}, "Pre Q12": {"Answer": "2", "Weight": 1},
                       "Pre Q13": {"Answer": "4", "Weight": 1}, "Pre Q10": {"Answer": "1", "Weight": 1},
                       "Pre Q11": {"Answer": "4", "Weight": 1}, "Pre Q16": {"Answer": "1", "Weight": 1},
                       "Pre Q17": {"Answer": "2", "Weight": 1}, "Pre Q14": {"Answer": "4", "Weight": 1},
                       "Pre Q15": {"Answer": "1", "Weight": 1}, "Post Q11": {"Answer": "4", "Weight": 1},
                       "Post Q23": {"Answer": "2", "Weight": 1}, "Post Q22": {"Answer": "2", "Weight": 1},
                       "Post Q26": {"Answer": "5", "Weight": 1}, "Post Q14": {"Answer": "4", "Weight": 1},
                       "Post Q15": {"Answer": "1", "Weight": 1}, "Post Q16": {"Answer": "1", "Weight": 1},
                       "Pre Q8": {"Answer": "2", "Weight": 1}, "Pre Q9": {"Answer": "5", "Weight": 1},
                       "Post Q12": {"Answer": "2", "Weight": 1}, "Pre Q1": {"Answer": "3", "Weight": 1},
                       "Pre Q2": {"Answer": "1", "Weight": 1}, "Pre Q3": {"Answer": "3", "Weight": 1},
                       "Pre Q4": {"Answer": "5", "Weight": 1}, "Pre Q5": {"Answer": "2", "Weight": 1},
                       "Pre Q6": {"Answer": "2", "Weight": 1}, "Pre Q7": {"Answer": "2", "Weight": 1},
                       "Pre Q23": {"Answer": "2", "Weight": 1}, "Pre Q22": {"Answer": "2", "Weight": 1},
                       "Pre Q21": {"Answer": "5", "Weight": 1}, "Pre Q20": {"Answer": "4", "Weight": 1},
                       "Pre Q27": {"Answer": "3", "Weight": 1}, "Pre Q26": {"Answer": "5", "Weight": 1},
                       "Pre Q25": {"Answer": "3", "Weight": 1}, "Pre Q24": {"Answer": "1", "Weight": 1},
                       "Pre Q29": {"Answer": "2", "Weight": 1}, "Pre Q28": {"Answer": "5", "Weight": 1},
                       "Post Q29": {"Answer": "2", "Weight": 1}, "Post Q28": {"Answer": "5", "Weight": 1}}}

# final key will contain the correct answers for pre and post, sorted by question number
final_key = []
for element in unsorted_js['Key']:
    final_key.append([element, unsorted_js['Key'][element]['Answer']])

final_key = sorted(final_key, key=lambda x: int(x[0][x[0].index('Q') + 1:]))


# Correct answer key for FCI only. Would need adapting for other tests
# only use the elements whose title contains Pre/Post. (eg. there was an index, instead of -1 for not found)
pre_final_key = map(lambda x: int(x[1]), filter(lambda x: not x[0].find('Pre'), final_key))
post_final_key = map(lambda x: int(x[1]), filter(lambda x: not x[0].find('Post'), final_key))


def get_final_grade(pre_score, post_score):
    """
    Gets an average of student scores from the test max value.

    :param pre_score: pre score mean
    :param post_score: post score mean
    :return:average letter grade (with 30% "curve")
    """

    # Average score
    avg = (pre_score + post_score) / 2
    # In decimal percent in regards to the test max
    decimal_percent = avg / test_max
    # Actual percent value rounded off
    percent = int(decimal_percent * 100)

    if percent > 60:
        return 'A'
    if percent > 50:
        return 'B'
    if percent > 40:
        return 'C'
    if percent > 30:
        return 'D'
    return 'F'


def get_false_answer(correct_answer):
        """
        Returns an answer other than the correct answer for the selection

        :param correct_answer: The correct answer in number form
        :return:an incorrect choice
        """
        # tries a random number
        tmp = randint(1, 5)
        # repeats until it is a different number
        while tmp == correct_answer:
            tmp = randint(1, 5)

        return tmp


def get_answer_choices(answer_numbers):
        """
        gets a tuple of pre and post answers (which contains both correct and incorrect answers)

        :param answer_numbers: a list of [PRE, POST] questions that the student SHOULD get correct
        :return:[PRE, POST] answers, containing correct and incorrect answers for ALL questions.
        """

        pre_output_answers = []
        post_output_answers = []

        for question_number in range(test_max):
            # If the pre correct answers array contains the current value
            if question_number in answer_numbers[0]:
                # Append a lookup from the correct answers dictionary (pre_final_key)
                pre_output_answers.append(pre_final_key[question_number])
            else:
                # Append an answer other than the correct one using get_false_answer(lookup of the correct answer)
                pre_output_answers.append(get_false_answer(pre_final_key[question_number]))
            # If the post correct answers array contains the current value
            if question_number in answer_numbers[1]:
                # Append a lookup from the correct answers dictionary (post_final_key)
                post_output_answers.append(post_final_key[question_number])
            else:
                # Append an answer other than the correct one using get_false_answer(lookup of the correct answer)
                post_output_answers.append(get_false_answer(post_final_key[question_number]))
        return pre_output_answers, post_output_answers


def add_student_answers_and_metadata(student_list):
    """
    Adds all information, used to create the final students list

    :param student_list:initial students list, only containing [student id, pre score, post score]
    :return:list of final students with metadata and answer choices
    """

    output_students = []

    for current_student in student_list:
        # Sets the values to identifiable variables (student id, pre score, and post score)
        student_id = current_student[0]
        student_pre_score = current_student[1]
        student_post_score = current_student[2]

        # Creates a random selection of the answers that the student will get correct
        correct_pre_answers = sample(xrange(0, test_max), student_pre_score)
        correct_post_answers = sample(xrange(0, test_max), student_post_score)

        # [PRE correct list, POST correct list]
        answers = get_answer_choices([
            correct_pre_answers,
            correct_post_answers
        ])

        # Adds all meta-data and grades to the students array that is returned.
        output_students.append(
            [
                student_id,
                get_final_grade(student_pre_score, student_post_score),
                majors[randint(0, len(majors) - 1)],
                genders[randint(0, 1)],
                student_pre_score
            ]
            + answers[0]
            + [student_post_score]
            + answers[1]
        )

    return output_students

# Students list only containing [student id, pre score, post score]
initial_students = make_student_list(number_students)

# Students list containing all metadata, answer choices, and id number.
final_students = add_student_answers_and_metadata(initial_students)

# writes to a file (in my dropbox) whose name contains the mean scores chosen.
out_file = open(
    '/home/josh/Dropbox/KSU/KDD/Shared/manning/'
    + 'mean2[' + str(mean_scores[0]) + '-' + str(mean_scores[1])
    + '].csv', 'w'
)

# Add each header (except the last) to the file with a trailing comma
for header in headers[:-1]:
    out_file.write(header + ',')
# Write the last header with a trailing new line symbol
out_file.write(headers[-1] + '\n')

# For each student
for student in final_students:
    # On one line add all the metadata, id, and answer choices (order corresponds with headers)
    for element in student[:-1]:
        out_file.write(str(element) + ',')
    # Write the last element of the student with a trailing new line symbol
    out_file.write(str(student[-1]) + '\n')

# You be done, so close the file
out_file.close()
