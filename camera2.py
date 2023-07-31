import cv2
import datetime
import os

# Define the cameras to use
camera1 = cv2.VideoCapture(0)
camera2 = cv2.VideoCapture(1)

# Define the hotkey to trigger image capture
hotkey = 32  # Spacebar key
hotkey2 = 27  # Esc key

# Create a window to display both camera frames side by side
cv2.namedWindow('Cameras', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Cameras', 1280, 480)

# Capture and display frames from the cameras
while True:
    # Capture frames from the cameras
    ret1, frame1 = camera1.read()
    ret2, frame2 = camera2.read()

    # Resize the frames to 640x480
    frame1 = cv2.resize(frame1, (640, 480))
    frame2 = cv2.resize(frame2, (640, 480))

    # Concatenate the frames horizontally
    frame = cv2.hconcat([frame1, frame2])

    # Display the concatenated frame
    cv2.imshow('Cameras', frame)

    # Check for hotkey press
    key = cv2.waitKey(1)
    if key == hotkey:
        # Generate a timestamp
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

        # Create the directory to save the images
        save_dir = r'C:/Users/Asus Tuf/Desktop/test tyres'

        # Define the file names for the images
        file_name1 = os.path.join(save_dir, 'Left_' + timestamp + '.jpg')
        file_name2 = os.path.join(save_dir, 'Right_' + timestamp + '.jpg')

        # Save the images to the directory
        cv2.imwrite(file_name1, frame1)
        cv2.imwrite(file_name2, frame2)
        print('Images saved!')

    # Check for 'q' key press to exit
    if key == hotkey2:
        break

# Release the cameras and close windows
camera1.release()
camera2.release()
cv2.destroyAllWindows()
