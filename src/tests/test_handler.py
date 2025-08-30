from handler.handler import lambda_handler,get_cleaned_data

def test_get_cleaned_data():
    """
    Tests the get_cleaned_data function
    
    Verifies that the length of the list returned by get_cleaned_data is
    equal to the number argument passed to the function.
    """
    number = 1
    data = get_cleaned_data(number)
    
    assert number == len(data)

# # Commenting for testing failure case of coverage
def test_lambda_function_data(create_bucket1):
    """_summary_

    Args:
        create_bucket1 (_type_): _description_
    """
    
    bucket_name = "sample-test"
    number = 10
    event = dict(bucket_name=bucket_name,number=number)
    context = {}
    response = lambda_handler(event, context)
    users_count = response.get("users_count")
    
    assert number == users_count

