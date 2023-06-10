from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model

# Load the model, mean and standard deviation files
model = load_model('trained_model(HUE1).h5')
X_mean = pd.read_csv('X_mean.csv', index_col=0).squeeze("columns")
X_std = pd.read_csv('X_std.csv', index_col=0).squeeze("columns")

# Create Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data
    data = request.get_json(force=True)

    # Transform the incoming JSON data into DataFrame
    new_input = pd.DataFrame(data, index=[0])

    # Normalize the new input data
    new_input_norm = (new_input - X_mean) / X_std

    # Make predictions
    predictions = model.predict(new_input_norm)

    # Apply threshold of 0.5 to convert predictions to binary values
    predictions_binary = (predictions >= 0.5).astype(int)

    # Convert predictions to a list and return as JSON
    return jsonify(predictions_binary.tolist())


if __name__ == '__main__':
    app.run(port=5000, debug=False)
