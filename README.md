# face-recognition

This program implements facial recognition by using the OpenCV library and the dlib and face_recognition packages. The program identifies faces within an input image and assigns predicted names to each face using the dataset of existing faces and names. 

If you wish to re-train the model on the provided dataset then run `encode_faces.py` to encode the images within the dataset and store them in encodings.pickle. Do so by using this command: `python encode_faces.py --dataset dataset --encodings encodings.pickle`. However, this is not required as I have already trained the model and included `encodings.pickle` within the repo. 

Next, run `recognize_faces_image.py` using this command: `python recognize_faces_image.py --encodings encodings.pickle \--image LOCATION_OF_DESIRED_IMAGE`. Replace `LOCATION_OF_DESIRED_IMAGE` with the file location of the image you wish to test (look in the examples folder). 
For a faster outcome, add the following text to the end of the previous command: `--detection-method hog`. For a more accurate outcome, leave the command as is (will use CNN method by default).

If you want to add more faces to the dataset then create a folder with the name of the individual and add images of the individual to the folder. Then, retrain the model by running `encode_faces.py` and add an image containing your desired face to the examples folder. Finally run `recongize_faces_impage.py` again and enjoy the results.

The dataset used in this project is a condesed version of this dataset: http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html. This project is meant to be non-commerical and all dataset credits go to the linked website. 
