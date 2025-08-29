import logging
from faker import Faker
from pprint import pprint
from datetime import date,datetime
import boto3
import awswrangler as wr
import pandas as pd

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


FAKE = Faker()


def get_cleaned_data(number):
    """_summary_

    Args:
        number (int): Take a number to generate data 

    Returns:
        List(dict): Return list of dictionaries
    """
    data = [FAKE.simple_profile() for _ in range(number)]
    cleaned_data = []
    for d in data:
        new = {}
        for k,v in d.items():
            if isinstance(v,date):
                new[k] = v.strftime("%Y-%m-%d")
            else:
                new[k] = v
        cleaned_data.append(new)
    return cleaned_data


def lambda_handler(event, context):
    LOGGER.info(f'Event Object: {event}')
    LOGGER.info(f'Context Object: {context}')
    session = boto3.session.Session()
    number = event.get("number")
    bucket_name = event.get("bucket_name")

    cleaned = get_cleaned_data(number)
    
    event["data"] = cleaned
    
    df = pd.DataFrame(data=cleaned)
    now_str = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"users_{now_str}.csv"
    file_location = f"s3://{bucket_name}/cicd/{file_name}"
    wr.s3.to_csv(df,path=file_location, boto3_session=session, index=False)
    
    response = {
        "status_code": 200,
        "file_location": file_location,
        "users_count": len(cleaned)
    }
    
    return response