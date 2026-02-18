resource "aws_lambda_function" "lambda_name" {
  function_name = var.lambda_name
  runtime       = "python3.12"
  handler       = "handler.lambda_handler"
  role          = aws_iam_role.lambda_role.arn

  s3_bucket = var.lambda_s3_bucket
  s3_key    = "ProductAI-lambda-create-product/${var.lambda_name}.zip"

  tags = {
    Environment = var.env
  }
}

resource "aws_iam_role" "lambda_role" {
  name = "${var.lambda_name}-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })

  tags = {
    Environment = var.env
  }
}

resource "aws_iam_role_policy_attachment" "lambda_logs" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}