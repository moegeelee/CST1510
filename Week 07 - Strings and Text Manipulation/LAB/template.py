"""Week 7 Record Check: survey ratings.

Mohammed Mohammed Alhaji
Data Science | 12 November 2026
"""

from pathlib import Path


def parse_line(raw_line):
    """Clean a survey line and return its name, rating and age."""
    survey, answers = raw_line.strip().lower().split(",", 1)
    fields = {}
    for answer in answers.split(","):
        key, value = answer.split("=", 1)
        fields[key.strip()] = int(value.strip())
    return {"survey": survey.strip(), "rating": fields["rating"], "age": fields["age"]}


def status_of(record):
    """Flag ratings of 1 or 2 on the five-point survey for follow-up."""
    if record["rating"] <= 2:
        return "FLAGGED"
    return "OK"


def print_report(data_file):
    """Print each survey response with its status and count the flagged responses."""
    total = 0
    flagged = 0
    with open(data_file, encoding="utf-8") as survey_file:
        for raw_line in survey_file:
            if raw_line.strip():
                record = parse_line(raw_line)
                status = status_of(record)
                print(record, status)
                total += 1
                if status == "FLAGGED":
                    flagged += 1
    print(f"{total} records, {flagged} flagged")


if __name__ == "__main__":
    print_report(Path(__file__).with_name("survey_responses.txt"))
