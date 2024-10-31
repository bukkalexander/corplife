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
