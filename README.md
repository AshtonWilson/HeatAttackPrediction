Heart Attack Risk Prediction

This project uses a machine learning model to predict the risk of a heart attack based on user-provided input data. The K-Nearest Neighbors (KNN) algorithm is employed, achieving a 92% accuracy after training. The project includes a graphical user interface (GUI) built with Tkinter, allowing users to enter patient data and receive a prediction.
Features

    Model: K-Nearest Neighbors (KNN) classifier
    Input: Patient information such as age, sex, cholesterol levels, etc.
    Output: Prediction of heart attack risk (either "at risk" or "not at risk")
    GUI: Simple form interface for entering patient data and receiving results

Requirements

To run the project, ensure the following dependencies are installed:
pip install pandas scikit-learn tkinter
How It Works

    Dataset: The model is trained using the heart.csv dataset, which includes multiple features such as age, cholesterol level, and exercise-induced angina to predict heart attack risk.
    Preprocessing: The dataset is standardized using StandardScaler to ensure features are on the same scale.
    Model Training: The KNN classifier is trained on 80% of the data, and 20% is used for testing.
    User Input: The GUI allows users to enter values for different medical indicators, and the model predicts whether the patient is at risk.
    Prediction: After entering the patient data, the program outputs a prediction, either showing that the patient is at risk or not at risk.

Usage

    Download the heart.csv dataset and place it in the same directory as the script.
    Run the Python script:
    python heart_attack_prediction.py
    Enter the required patient data into the form that appears in the GUI.
    Click the Predict button to receive the heart attack risk prediction.

Input Fields

    Age
    Sex (1 = Male, 0 = Female)
    Chest Pain Type (0-3)
    Resting Blood Pressure
    Cholesterol Level
    Fasting Blood Sugar (1 = True, 0 = False)
    Resting ECG (0-2)
    Max Heart Rate
    Exercise-induced Angina (1 = Yes, 0 = No)
    ST Depression
    Slope of ST Segment (0-2)
    Number of Major Vessels (0-3)
    Thalassemia (1, 2, or 3)

Output

A message box will display one of the following:

    "This patient is at risk of a heart attack."
    "This patient is not at risk of a heart attack."
