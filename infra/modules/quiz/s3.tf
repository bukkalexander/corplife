# Define the S3 bucket resource with static website hosting
resource "aws_s3_bucket" "static_website_bucket" {
  bucket = "${var.resource_prefix}website"  # Replace with a unique bucket name 
}

resource "aws_s3_bucket_policy" "allow_access_from_another_account" {
  bucket = aws_s3_bucket.static_website_bucket.id
  policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": "*",
        "Action": "s3:GetObject",
        "Resource": "${aws_s3_bucket.static_website_bucket.arn}/*"
      }
    ]
  })

  depends_on = [ aws_s3_bucket_public_access_block.public_access ]
}

resource "aws_s3_bucket_website_configuration" "web_config" {
  bucket = aws_s3_bucket.static_website_bucket.id

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "error.html"
  }

}

# Public access settings for the bucket
resource "aws_s3_bucket_public_access_block" "public_access" {
  bucket                  = aws_s3_bucket.static_website_bucket.id
  block_public_acls       = false
  ignore_public_acls      = false
  block_public_policy     = false
  restrict_public_buckets = false
}

# Calculate a hash for all files in the `dist` directory
locals {
  dist_files = fileset("${path.module}/${var.npm_output_dir}", "**")  # Select all files in `dist`
  dist_hash  = sha256(join("", [for file in local.dist_files : filesha256("${path.module}/${var.npm_output_dir}/${file}")]))
}

# Upload files in `dist` to the S3 bucket
resource "aws_s3_object" "dist_files" {
  for_each = local.dist_files
  bucket   = aws_s3_bucket.static_website_bucket.id
  key      = each.value
  source   = "${path.module}/${var.npm_output_dir}/${each.value}"

  # Trigger re-upload if the hash changes
  etag     = local.dist_hash

   # Set content_type based on file extension
  content_type = lookup(
    {
      "html" = "text/html",
      "css"  = "text/css",
      "js"   = "application/javascript",
      "svg"  = "image/svg+xml"
    },
    split(".", each.value)[length(split(".", each.value)) - 1],  # Get file extension
    "application/octet-stream"  # Default if not matched
  )

  depends_on = [ local_file.config_json ]
}

resource "local_file" "config_json" {
  filename = "${path.module}/${var.npm_output_dir}/config.json"
  content  = jsonencode({
    apiUrl = "${aws_apigatewayv2_api.api-gateway.api_endpoint}"
    userPoolId = "${aws_cognito_user_pool.user_pool.id}"
    userPoolWebClientId = "${aws_cognito_user_pool_client.user_pool_client.id}"
    region = "${var.region}"
  })

  depends_on = [ aws_apigatewayv2_api.api-gateway ]
}
