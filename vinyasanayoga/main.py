import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
import pickle

# Load the trained model
model = tf.keras.models.load_model('mymodel.h5')

# Load the one-hot encoder
with open("onehot_encoder_output.pkl", "rb") as file:
    encoder = pickle.load(file)

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# Start webcam
cap = cv2.VideoCapture(0)

def process_pose(landmarks, pose_label, lang):
    """Calls the correct function based on pose prediction."""
    if pose_label == "Plankpose":
        return Plank_Pose(landmarks, lang)
    elif pose_label == "Cobra":
        return Cobra(landmarks, lang)
    elif pose_label == "adhomuka":
        return AdhoMukha(landmarks, lang)
    elif pose_label == "chathurangadandasana":
        return ChathurangaDandasana(landmarks, lang)
    else:
        return "Unknown Pose"

# Start real-time processing
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Process the frame
        results = pose.process(image)

        # Convert back to BGR for display
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Draw landmarks
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Extract landmark data
            landmarks = results.pose_landmarks.landmark
            pose_data = []
            base_x, base_y, base_z = landmarks[0].x, landmarks[0].y, landmarks[0].z  # Normalize based on first landmark

            for landmark in landmarks:
                pose_data.extend([landmark.x - base_x, landmark.y - base_y, landmark.z - base_z])

            # Convert to NumPy and predict
            pose_data = np.array(pose_data).reshape(1, -1)
            prediction = model.predict(pose_data)
            pose_label = encoder.inverse_transform(prediction)[0][0]  # Decode the one-hot prediction

            # Check pose correctness
            feedback = process_pose(landmarks, pose_label, lang="en")

            # Display result
            status_text = f"Pose: {pose_label} | Feedback: {feedback if feedback else 'Perfect'}"
            cv2.putText(image, status_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Show the image
        cv2.imshow('Yoga Pose Detection', image)

        # Exit on pressing 'q'
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
