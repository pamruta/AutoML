
# Projects Built in Auto-ML

## Character Recognition

#### Custom Trained Object Detection Model to Detect Famous TV / Movie / Cartoon Characters

Model output tested on famous Mickey Mouse Show

![Mickey-Mouse Demo](demos/mickey-mouse.gif)

Model output tested on classic movie Wizard of Oz 

![Wizard-of-Oz Demo](demos/wizard-of-oz.gif)

Model tested on popular Super Heroes in Action & Sci-Fi films..

[coming soon..]

### Scripts in this directory :

	Detect-Character.py : Recognize popular tv / movie and cartoon characters..

	Usage:

		python3 Detect-Character.py VIDEO PROJECT_ID MODEL_ID
	
	In addition to the input video file, this script takes Auto-ML Project ID and Model ID
        as input parameters. Once the model is trained and deployed in Google Cloud, simply
        pass the corresponding project and model IDs to run this script.

        If you like to use any of my pre-trained models deployed on GCP, please contact me
        to obtain access credentials for APIs..

	Coming soon:  Scripts for running offline predictions using TensorFlow.JS / Docker

