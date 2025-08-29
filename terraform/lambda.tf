resource "aws_lambda_function" "users_lambda" {
  function_name = "${terraform.workspace}-users-generator"
  package_type  = "Image"
  image_uri     = "${aws_ecr_repository.users.repository_url}:latest"
  role          = aws_iam_role.iam_for_lambda.arn
  architectures = ["arm64"]
  runtime          = "python3.11"

  depends_on = [aws_iam_role.iam_for_lambda, aws_ecr_repository.users, null_resource.image_build]

  # Timeout
  timeout = 300 # In seconds (up to 900 seconds or 15 minutes)

  # Memory
  memory_size = 512 # In MB (from 128 MB to 10240 MB)

  image_config {
    command     = ["handler.lambda_handler"]
  }


  tags = {
    Name = "Users generator Lambda function in ${terraform.workspace}"
  }

}