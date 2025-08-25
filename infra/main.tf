resource "aws_lambda_function" "lambda_name" {
  #function_name = var.lambda_name
  function_name = "teste"
  runtime       = "python3.12"
  handler      = "main.create_product"
  role         = aws_iam_role.lambda_role.arn
}