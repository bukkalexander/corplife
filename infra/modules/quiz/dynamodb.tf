# Question Table
resource "aws_dynamodb_table" "corplife-quiz-questions" {
  name           = "${var.resource_prefix}Questions"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "questionID"
 

  attribute {
    name = "questionID"
    type = "S"
  }

  global_secondary_index {
    name               = "CategoryDifficultyIndex"
    hash_key           = "category"
    range_key          = "difficulty"
    projection_type    = "ALL"

  }

  # Group by category IAM, Storage..
  attribute {
    name = "category"
    type = "S"
  }

  # Sort by difficulty Easy, Medium, Hard..
  attribute {
    name = "difficulty"
    type = "S"
  }

  tags = {
    Name = "${var.resource_prefix}Questions"
  }
}

# User Table
resource "aws_dynamodb_table" "corplife-quiz-users" {
  name           = "${var.resource_prefix}Users"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "username"

  # Primary attribute - Cognito username
  attribute {
    name = "username"
    type = "S"  # String type for usernames
  }

  # Xp attribute for leaderboard
  attribute {
    name = "xp"
    type = "N"  # Numeric type for points or xp
  }

  # Global Secondary Index (GSI) for leaderboard queries sorted by xp
  global_secondary_index {
    name               = "XpIndex"
    hash_key           = "username"  # Must have a hash key (use username to make it unique)
    range_key          = "xp"     # Sort by xp for leaderboard
    projection_type    = "ALL"       # Include all attributes
  }

  tags = {
    Name = "${var.resource_prefix}Users"
  }
}
