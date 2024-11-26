# scripts/data_uploader.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# scripts/question_uploader.py

import boto3
import inspect
import json
import api.data as data  # Import the data module

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('corplife-quiz-Questions')

def get_all_question_sets(module):
    """
    Dynamically fetch all QUESTION_* variables from the given module.
    """
    questions = {}
    for name, obj in inspect.getmembers(module):
        if name.startswith("QUESTIONS_") and isinstance(obj, list):
            # Extract the numeric part of the variable name (e.g., QUESTIONS_1 -> quiz_1)
            quiz_id = f"quiz_{name.split('_')[1]}"
            questions[quiz_id] = obj
            print(f"Found quiz: {quiz_id} with {len(obj)} questions")  # Debug log
    return questions

def upload_quiz_data(dry_run=False):
    """
    Upload quiz data to DynamoDB or display it for a dry run.
    """
    # Dynamically fetch all question sets
    question_sets = get_all_question_sets(data)

    total_questions = 0

    for quiz_id, questions in question_sets.items():
        if dry_run:
            print(f"\n=== DRY-RUN: Data for Quiz '{quiz_id}' ===")
        else:
            print(f"\nUploading Quiz: {quiz_id}")

        for idx, question in enumerate(questions):
            question_id = str(idx + 1)  # Numeric question ID within the quiz
            item = {
                'quizID': quiz_id,  # e.g., "quiz_1"
                'questionID': question_id,  # e.g., "1"
                'text': question['text'],
                'answers': question['answers'],
                'correctAnswer': question['correctAnswer'],
            }

            if dry_run:
                # Pretty print the item in dry-run mode
                print(json.dumps(item, indent=4))
            else:
                # Upload to DynamoDB in non-dry-run mode
                with table.batch_writer() as batch:
                    batch.put_item(item)

            total_questions += 1

        if not dry_run:
            print(f"Uploaded quiz: {quiz_id}")

    print(f"\nTotal quizzes processed: {len(question_sets)}")
    print(f"Total questions processed: {total_questions}")

if __name__ == "__main__":
    import argparse

    # Setup argument parser for dry-run mode
    parser = argparse.ArgumentParser(description="Upload quiz data to DynamoDB.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Perform a dry run without uploading data to DynamoDB.",
    )
    args = parser.parse_args()

    # Call the function with dry-run flag
    upload_quiz_data(dry_run=args.dry_run)
