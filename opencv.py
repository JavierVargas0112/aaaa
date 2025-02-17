import cv2

class Camera:
    def __init__(self, frame_width=1280, frame_height=720, camera_number=0):
        # Initialize the camera with the specified width, height, and camera number
        self.video_capture = cv2.VideoCapture(camera_number)
        self.video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
        self.video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

    def frame(self):
        # Capture a frame from the camera
        _, frame = self.video_capture.read()
        
        # Add text and a rectangle to the frame
        category_name = "JSVP-ACOL"
        text_position = (50, 50)
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_size = 1
        color = (255, 0, 0)  # Blue color in BGR
        font_thickness = 2

        # Draw a rectangle
        rect_start = (100, 100)
        rect_end = (400, 300)
        cv2.rectangle(frame, rect_start, rect_end, color, font_thickness)

        # Add text to the frame
        cv2.putText(frame, category_name, text_position, font, font_size, color, font_thickness)

        return frame
camera = Camera()

while True:
    frame = camera.frame()  # Get the current frame
    cv2.imshow("Camera", frame)  # Show the frame in a window

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close any open windows
camera.video_capture.release()
cv2.destroyAllWindows()
