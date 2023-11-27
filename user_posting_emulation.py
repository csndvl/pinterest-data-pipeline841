import requests
from time import sleep
import random
from multiprocessing import Process
import boto3
import json
import sqlalchemy
from sqlalchemy import text


random.seed(100)


class AWSDBConnector:

    def __init__(self):

        self.HOST = "pinterestdbreadonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com"
        self.USER = 'project_user'
        self.PASSWORD = ':t%;yCY3Yjg'
        self.DATABASE = 'pinterest_data'
        self.PORT = 3306
        

        
    def create_db_connector(self):
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}?charset=utf8mb4")
        return engine


new_connector = AWSDBConnector()

def send_data_to_Kafka(data, topic):
    invoke_url = "https://iij0y5sisb.execute-api.us-east-1.amazonaws.com/Init"
    url = invoke_url + "/topics/" + topic
    print (url)

    payload = json.dumps({
    "records": [
        {
        #Data should be send as pairs of column_name:value, with different columns separated by commas       
        "value": {"index": data["index"], "unique_id": data["unique_id"], "title": data["title"], "description": data["description"], 
                  "poster_name": data["poster_name"], "follower_count": data["follower_count"], "tag_list": data["tag_list"], 
                  "is_image_or_video": data["is_image_or_video"], "image_src": data["image_src"], "downloaded": data["downloaded"], 
                  "save_location": data["save_location"], "category": data["category"]}
        }
    ]
})

    headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}
    response = requests.request("POST", url, headers = headers, data = payload)
    print (response.status_code)
    return 

def run_infinite_post_data_loop():
    while True:

        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 11000)
        engine = new_connector.create_db_connector()

        with engine.connect() as connection:

            pin_string = text(f"SELECT * FROM pinterest_data LIMIT {random_row}, 1")
            pin_selected_row = connection.execute(pin_string)
            
            for row in pin_selected_row:
                pin_result = dict(row._mapping)
                topic_name = "12f4a3e5b9c5.pin"
                send_data_to_Kafka(pin_result, topic_name)
                print ("pin result sent")


            geo_string = text(f"SELECT * FROM geolocation_data LIMIT {random_row}, 1")
            geo_selected_row = connection.execute(geo_string)
            
            for row in geo_selected_row:
                geo_result = dict(row._mapping)

            user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")
            user_selected_row = connection.execute(user_string)
            
            for row in user_selected_row:
                user_result = dict(row._mapping)
            
            print(pin_result.keys())
            # print(geo_result)
            # print(user_result)
            break

if __name__ == "__main__":
    run_infinite_post_data_loop()
    print('Working')
    
    


