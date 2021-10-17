import cv2
import mediapipe as mp
import winsound
import server
import threading

def play_sound():
    audio_file = "max.wav"
    winsound.PlaySound(audio_file, winsound.SND_FILENAME)

cap = cv2.VideoCapture("walk.mp4")

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose(False, 1, True, True, True, 0.9, 0.5)

# Keep track of people that enter and leave
OCCUPANCY_LIMIT = 5
number_of_people = 0
in_frame = False

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks)
        points = []
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            if id == 6 or id == 23:
                cx, cy = int(lm.x * w), int(lm.y * h)
                points.append((cx, cy))
                
        cv2.rectangle(img, points[0], points[1], (0,0,255), 3)        

        if not in_frame:
            
            if cx < (h/2):
                number_of_people += 1
            else:
                number_of_people -= 1

            if number_of_people == OCCUPANCY_LIMIT:
                cv2.rectangle(img, (0,0), (1920, 1080), (0, 0, 255), -1)
                cv2.putText(img, "Max Occupancy Reached", (150, 500), cv2.FONT_HERSHEY_PLAIN, 8, (255, 255, 255), 10)
                cv2.imshow("MediaPipe Pose", img)
                cv2.waitKey(1)

                play_sound()

            t = threading.Thread(target=server.update_db, args = [number_of_people])
            t.start()

            in_frame = True
            
    else:
        in_frame = False
    
    cv2.putText(img, "Number of people: " + str(number_of_people), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
    cv2.putText(img, "Enter -->", (850, 1000), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    cv2.putText(img, "<-- Exit", (850, 950), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
    cv2.imshow("MediaPipe Pose", img)
    cv2.waitKey(1)

    if cv2.getWindowProperty("MediaPipe Pose", cv2.WND_PROP_VISIBLE) < 1: 
        break

server.graph()
cap.release()
cv2.destroyAllWindows()


