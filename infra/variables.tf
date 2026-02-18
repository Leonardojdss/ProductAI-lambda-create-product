variable "lambda_name" {
    type = string
    description = "The name of the Lambda function"
}

variable "env" {
    type = string
    description = "The environment for the Lambda function (e.g., dev, prod)"
}   