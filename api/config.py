from dataclasses import dataclass


@dataclass
class Config:
    api_url: str
    dynamodb_table_name_users: str
    dynamodb_table_name_quizzes: str
    dynamodb_table_name_questions: str
    dynamodb_table_name_quiz_records: str

def get_config():
    return Config(
        api_url="http://localhost:8000",
        dynamodb_table_name_users="corp-life_local_users",
        dynamodb_table_name_quizzes="corp-life_local_quizzes",
        dynamodb_table_name_questions="corp-life_local_questions",
        dynamodb_table_name_quiz_records="corp-life_local_quiz_records",
    )