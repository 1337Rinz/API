# API

## Hue Travel API

This repository contains the implementation of a Flask API for a machine learning model trained to recommend travel destinations in the city of Hue.

The data for training the model was collected and processed by the author. This API is designed to use the trained model to make predictions on new data.

## Requirements

To run this project, you will need Python installed on your system. If you don't have Python installed, you can download it [here](https://www.python.org/downloads/).

Once you have Python installed, you will need to install the Python libraries that the project depends on. You can install these dependencies using the following command:

pip install -r requirements.txt


## Running the API

To run the API, navigate to the project directory in your terminal and execute the following command:

python hue_travel_api.py


This will start the Flask API on your local machine, and it will be accessible at http://127.0.0.1:5000.

## Making a Prediction

Once the API is running, you can make a POST request to the `/predict` endpoint to get a prediction.

You should send a JSON payload with the request that contains the input data for the prediction. The data should have the following structure:

```json
{
    "AGE": [int],
    "Bạn đi với": [int],
    "Visiting time": [int],
    "sex": [int],
    "Desired amount": [int],
    "Di Tích Lịch Sử": [int],
    "Món ăn ngon": [int],
    "Trải nghiệm mới": [int],
    "Vẻ đẹp thiên": [int]
}
Replace [int] with the appropriate integer values for each field.


Mapping
Here is the mapping for categorical variables:
```json
{
"sex": {"Nữ": 0, "Nam": 1}
"Bạn đi với": {"Một Mình": 0, "Người yêu": 1, "Bạn Bè": 2, "Gia đình": 3}
"Visiting time": {"2 ngày 1 đêm": 2, "3 ngày 2 đêm": 3, "4 ngày 3 đêm": 4, "5 ngày 4 đêm": 5}
"Desired amount": {"Từ 1 đến 3 triệu": 0, "3,5 triệu": 1, "Từ 3 đến 5 Triệu": 2, "Từ 5 đến 7 triệu": 3, "Trên 10 triệu": 4}
}
The API will return a List response with the prediction.

Contact
If you have any questions or need further information, please feel free to contact 
