# face-recognition

![example 1](Users/Darshil/Documents/example1.png)

## What it is
This program implements facial recognition by using the OpenCV library and the dlib and face_recognition packages. The program identifies faces within an input image and assigns predicted names to each face using a dataset of faces and names. 

## Optional 
If you wish to re-train the model on the provided dataset then run `encode_faces.py` to encode the images within the dataset and store them in encodings.pickle. Do so by using this command: `python encode_faces.py --dataset dataset --encodings encodings.pickle`. However, this is not required as I have already trained the model and included `encodings.pickle` within the repo. 

## How to use it
Run `recognize_faces_image.py` using this command: `python recognize_faces_image.py --encodings encodings.pickle \--image LOCATION_OF_DESIRED_IMAGE`. Replace `LOCATION_OF_DESIRED_IMAGE` with the file location of the image you wish to test (look in the examples folder). 
For a faster outcome, add the following text to the end of the previous command: `--detection-method hog`. For a more accurate outcome, leave the command as is (will use CNN method by default).

The name is displayed for one face in the image to start with. Press any key while you have the ouput image selected to have the system display the name for the next face and repeat until all faces are labeled. Once all faces are labeled, press any key again and the program will exit.  

## Customize
If you want to add more faces to the dataset then create a sub-folder with the name of the individual in the dataset folder and add images of the individual to the sub-folder. Then, retrain the model by running `encode_faces.py` and add an image containing your desired face to the examples folder. Finally run `recongize_faces_impage.py` on the example image you added and enjoy the results.

## Disclaimer
The dataset used in this project is a condesed version of this dataset: http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html. This project is meant to be non-commerical and all dataset credits go to the linked website. 


![example 2](Users/Darshil/Documents/example1.png)
