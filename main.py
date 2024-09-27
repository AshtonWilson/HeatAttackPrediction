import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from tkinter import *
from tkinter import messagebox

# Load the dataset
df = pd.read_csv('heart.csv')

# Preprocess the data
X = df.drop('target', axis=1)  # Features
y = df['target']  # Target variable

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Initialize the KNN model
knn = KNeighborsClassifier(n_neighbors=5)

# Train the model
knn.fit(X_train, y_train)

# Create the main GUI window
window = Tk()
window.title("Heart Attack Prediction")
window.geometry("400x600")
window.config(bg="#FFF4EA")

# Define correct fields for input
fields = ['Age', 'Sex (1 = Male, 0 = Female)', 'Chest Pain type (0-3)', 'Resting Blood Pressure',
          'Cholesterol level', 'Fasting Blood Sugar (1 = True, 0 = False)', 'Resting ECG (0-2)',
          'Max Heart Rate', 'Exercise-induced angina (1 = Yes, 0 = No)', 'ST depression',
          'Slope of ST segment (0-2)', 'Number of vessels (0-3)', 'Thalassemia (1, 2, or 3)']

entries = {}

# Create input fields dynamically using grid method
for i, field in enumerate(fields):
    label = Label(window, text=field, bg="#FADFA1")
    label.grid(row=i, column=0, padx=10, pady=5, sticky='w')
    entry = Entry(window)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries[field] = entry


# Prediction function triggered by the button
def predict_heart_attack():
    try:
        # Get the user input values
        input_values = [float(entries[field].get()) for field in fields]

        # Ensure input is of proper shape (1 sample with all features)
        user_input_df = pd.DataFrame([input_values], columns=X.columns)

        # Scale the input using the same scaler
        user_input_scaled = scaler.transform(user_input_df)

        # Make a prediction using the trained KNN model
        prediction = knn.predict(user_input_scaled)

        # Output the prediction result
        if prediction[0] == 1:
            messagebox.showinfo("Prediction", "This patient is at risk of a heart attack.")
        else:
            messagebox.showinfo("Prediction", "This patient is not at risk of a heart attack.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")


# predict button
predict_button = Button(window, text="Predict", command=predict_heart_attack, bg="#C96868")
predict_button.grid(row=len(fields), columnspan=2, pady=20)

# This will keep the widow open
window.mainloop()
