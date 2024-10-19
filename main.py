import pickle
import numpy as np

# Load the model from the pickle file
with open('user_behavior_classifier.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to get user input
def get_user_input():
    user_id = input("Enter User ID: ")
    device_model = input("Enter Device Model (e.g., Xiaomi MI 11): ")
    operating_system = input("Enter Operating System (e.g., iOS or Android): ")
    app_usage_time = float(input("Enter App Usage Time (in minutes): "))
    screen_on_time = float(input("Enter Screen On Time (in hours): "))
    battery_drain = float(input("Enter Battery Drain (in mAh): "))
    num_apps_installed = int(input("Enter Number of Apps Installed: "))
    data_usage = float(input("Enter Data Usage (in MB): "))
    age = int(input("Enter Age: "))
    gender = input("Enter Gender (Male or Female): ")

    return [user_id, device_model, operating_system, app_usage_time, screen_on_time,
            battery_drain, num_apps_installed, data_usage, age, gender]

# Function to preprocess the input for the model
def preprocess_input(user_input):
    # You will need to implement any necessary preprocessing based on your model's requirements
    # For example, if you used Label Encoding or One-Hot Encoding, handle those here
    return user_input

# Main program loop
if __name__ == "__main__":
    while True:
        user_input = get_user_input()
        processed_input = preprocess_input(user_input)

        # Convert processed input into the right format (e.g., NumPy array)
        input_array = np.array(processed_input).reshape(1, -1)

        # Make prediction
        prediction = model.predict(input_array)

        print(f"Predicted User Behavior Class: {prediction[0]}")

        # Ask if the user wants to make another prediction
        another = input("Do you want to make another prediction? (y/n): ")
        if another.lower() != 'y':
            break
