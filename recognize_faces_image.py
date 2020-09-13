import face_recognition
import argparse
import pickle
import cv2

# Parse Command Line Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-e", "--encodings", required=True,
	            help="path to serialized db of facial encodings")
ap.add_argument("-i", "--image", required=True,
	            help="path to input image")
ap.add_argument("-d", "--detection-method", type=str, default="cnn",
	            help="face detection model to use: either `hog` or `cnn`")
args = vars(ap.parse_args())

print("Loading encodings...")
data = pickle.loads(open(args["encodings"], "rb").read())

image = cv2.imread(args["image"])
# Convert image from BGR to RGB for dlib
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print("Recognizing faces...")
# Detect coordinates for bounding boxes of each face in the image
boxes = face_recognition.face_locations(rgb, model=args["detection_method"])
# Compute facial embedding for each face
encodings = face_recognition.face_encodings(rgb, boxes)

names = []
for encoding in encodings:
    # Try to match each face in image to known encodings (uses k-NN model)
    matches = face_recognition.compare_faces(data["encodings"], encoding)
    name = "Unknown"

    if True in matches:
        # Indexes of all matched faces 
        matchedIdxs = [i for (i, b) in enumerate(matches) if b]
        counts = {}

        for i in matchedIdxs:
            name = data["names"][i].replace('_', ' ')
            counts[name] = counts.get(name, 0) + 1
        
        # Determines face by choosing the name with the most votes 
        name = max(counts, key=counts.get)


    names.append(name)

for ((top, right, bottom, left), name) in zip(boxes, names):
    # Create a green rectangle and displays predicted face name within it
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
    if top - 15 > 15:
        y = top - 15
    else:
        y = top + 15
    cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    cv2.imshow("Image", image)
    cv2.waitKey(0)
