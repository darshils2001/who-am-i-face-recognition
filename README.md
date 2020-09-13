# face-recognition

This program implements facial recognition by using the OpenCV library and the dlib and face_recognition packages. The program identifies faces within an input image and assigns predicted names to each face using the dataset of existing faces and names. 

To use the program first run `encode_faces.py` to encode the images within the dataset and store them in encodings.pickle. Do so by using this command: `python encode_faces.py --dataset dataset --encodings encodings.pickle`. 

Next, run `recognize_faces_image.py` using this command: `python recognize_faces_image.py --encodings encodings.pickle \--image LOCATION_OF_DESIRED_IMAGE`. Replace `LOCATION_OF_DESIRED_IMAGE` with the file location of the image you wish to test (look in the examples folder). 
For a faster outcome, add the following text to the end of the previous command: `--detection-method hog`. For a more accurate outcome, leave the command as is (will use CNN method by default).
