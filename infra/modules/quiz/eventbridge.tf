# Define the EventBridge Rule for scheduling
resource "aws_cloudwatch_event_rule" "schedule_lambda" {
  name        = "ReconciliationLambdaSchedule"
  description = "Runs the reconciliation lambda function every 6 hours"
  schedule_expression = "rate(6 hours)"  # Adjust as needed (e.g., "rate(1 day)" for daily)
}

# Add the EventBridge target to trigger the Reconciliation function
resource "aws_cloudwatch_event_target" "reconciliation_lambda_target" {
  rule      = aws_cloudwatch_event_rule.schedule_lambda.name
  target_id = "ReconciliationLambda"
  arn       = aws_lambda_function.reconciliation_lambda.arn
}
