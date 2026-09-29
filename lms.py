submissions = [
    {
        "quiz_name": "Statistics Quiz 1",
        "quiz_module": "Statistics",
        "quiz_score": 85,
        "student_id": 101,
        "student_name": "Jack",
        "submission_date": "2026-09-01"
    },
    {
        "quiz_name": "Statistics Quiz 2",
        "quiz_module": "Statistics",
        "quiz_score": 82,
        "student_id": 102,
        "student_name": "Bob",
        "submission_date": "2026-09-01"
    },
    {
        "quiz_name": "Algebra Quiz 1",
        "quiz_module": "Algebra",
        "quiz_score": 78,
        "student_id": 101,
        "student_name": "Jack",
        "submission_date": "2026-09-02"
    },
    {
        "quiz_name": "Algebra Quiz 2",
        "quiz_module": "Algebra",
        "quiz_score": 81,
        "student_id": 103,
        "student_name": "Charlie",
        "submission_date": "2026-09-02"
    },
    {
        "quiz_name": "History Quiz 1",
        "quiz_module": "History",
        "quiz_score": 80,
        "student_id": 102,
        "student_name": "Bob",
        "submission_date": "2026-09-03"
    }
        {
        "quiz_name": "History Quiz 1",
        "quiz_module": "History",
        "quiz_score": 79,
        "student_id": 104,
        "student_name": "Alex",
        "submission_date": "2026-09-03"
    }
]
def filter_by_date(date, submissions):
    """
    Returns all submissions whose submission_date matches the given date.

    Args:
        date (str): The date to search for.
        submissions (list): A list of submission dictionaries.

    Returns:
        list: Submission dictionaries matching the date.
    """
    results = []

    for submission in submissions:
        if submission["submission_date"] == date:
            results.append(submission)

    return results


def filter_by_student_id(student_id, submissions):
    """
    Returns all submissions belonging to the specified student ID.

    Args:
        student_id (int): The student ID to search for.
        submissions (list): A list of submission dictionaries.

    Returns:
        list: Submission dictionaries matching the student ID.
    """
    results = []

    for submission in submissions:
        if submission["student_id"] == student_id:
            results.append(submission)

    return results


def find_unsubmitted(date, student_names, submissions):
    """
    Finds students who did not submit any quiz on the specified date.

    Args:
        date (str): The date to check.
        student_names (list): A list of student names.
        submissions (list): A list of submission dictionaries.

    Returns:
        list: Names of students with no submission on the specified date.
    """
    results = []

    submissions_on_date = filter_by_date(date, submissions)

    for student_name in student_names:
        submitted = False

        for submission in submissions_on_date:
            if submission["student_name"] == student_name:
                submitted = True
                break

        if not submitted:
            results.append(student_name)

    return results


def get_average_score(submissions):
    """
    Calculates the average quiz score for all submissions.

    Args:
        submissions (list): A list of submission dictionaries.

    Returns:
        float: The average quiz score rounded to one decimal place.

    Raises:
        ZeroDivisionError: If the submission list is empty.
    """
    total = 0

    for submission in submissions:
        total += submission["quiz_score"]

    average = total / len(submissions)

    return round(average, 1)


def get_average_score_by_module(submissions):
    """
    Calculates the average quiz score for each quiz module.

    Args:
        submissions (list): A list of submission dictionaries.

    Returns:
        dict: A dictionary where each key is a module name and each
              value is the average score for that module.
    """
    module_scores = {}
    module_averages = {}

    for submission in submissions:
        module = submission["quiz_module"]
        score = submission["quiz_score"]

        if module not in module_scores:
            module_scores[module] = []

        module_scores[module].append(score)

    for module in module_scores:
        module_averages[module] = round(
            get_average_score(module_scores[module]), 1
        )

    return module_averages