# Create Cognito User Pool
resource "aws_cognito_user_pool" "user_pool" {
  name = "${var.resource_prefix}user_pool"

  # Password policy for the User Pool
  password_policy {
    minimum_length    = 8
    require_lowercase = true
    require_numbers   = true
    require_symbols   = true
    require_uppercase = true
  }

   # Enable email verification
  auto_verified_attributes = ["email"]

  # Set up the alias for sign-in with email or preferred username
  alias_attributes = ["email", "preferred_username"]

  # Optional: Customize the email verification message
  verification_message_template {
    email_message = "Thank you for signing up to ${var.resource_prefix}app ! Your verification code is {####}"
    email_subject = "Your verification code for ${var.resource_prefix}app"
  }

    mfa_configuration = "OFF"

  account_recovery_setting {
    recovery_mechanism {
      name     = "verified_email"
      priority = 1
    }
  }

  lambda_config {
    post_confirmation = aws_lambda_function.post_confirmation_trigger.arn
  }

   depends_on = [ aws_lambda_function.post_confirmation_trigger ]

}

# Create App Client for User Pool (without client secret)
resource "aws_cognito_user_pool_client" "user_pool_client" {
  name                         = "my_user_pool_client"
  user_pool_id                 = aws_cognito_user_pool.user_pool.id
  generate_secret              = false
  prevent_user_existence_errors = "ENABLED"

  explicit_auth_flows = [
    "ALLOW_USER_PASSWORD_AUTH",
    "ALLOW_REFRESH_TOKEN_AUTH",
    "ALLOW_USER_SRP_AUTH"
  ]

  # Token expiration times (optional)
  access_token_validity  = 1      # hours
  id_token_validity      = 1      # hours
  refresh_token_validity = 30     # days
}

