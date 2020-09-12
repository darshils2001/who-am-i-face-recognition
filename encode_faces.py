from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os

# Parse Command Line Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dataset", required=True, 
                help="path to input directory of faces + images")
ap.add_argument("-e", "--encodings", required=True,
	            help="path to serialized db of facial encodings")
ap.add_argument("-d", "--detection-method", type=str, default="cnn",
	            help="face detection model to use: either `hog` or `cnn`")
args = vars(ap.parse_args())

# Get path to images in dataset
print("Quantifying faces...")
imagePaths = list(paths.list_images(args["dataset"]))

knownEncodings = []
knownNames = []
for (i, imagePath) in enumerate(imagePaths):
    print("Processing image {}/{}".format(i+1, len(imagePaths)))
    # Get person name 
    name = imagePath.split(os.path.sep)[-2]

    image = cv2.imread(imagePath)
    # Convert image from BGR to RGB for dlib 
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect coordinates for bounding boxes of each face in the image
    boxes = face_recognition.face_locations(rgb, model=args["detection_method"])
    # Compute facial embedding for each face
    encodings = face_recognition.face_encodings(rgb, boxes)

    for encoding in encodings:
        knownEncodings.append(encoding)
        knownNames.append(name)

# Store encodings and names 
print("Serializing encodings...")
data = {"encodings": knownEncodings, "names": knownNames}
f = open(args["encodings"], "wb")
f.write(pickle.dumps(data))
f.close()