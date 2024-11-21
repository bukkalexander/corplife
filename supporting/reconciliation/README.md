# Reconciliation Lambda Function

This function is to make sure that if a user is deleted manually from cognito it eventually is removed from dynamodb too. Otherwise normal user deletion flow should remove the user from both. 

TODO: Implement "delete my account"
