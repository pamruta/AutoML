
# Projects Built in Auto-ML

## Character Recognition

#### Customized Object Detection Models to Detect Famous TV / Movie / Cartoon Characters

Output of model on famous Mickey Mouse Show

![Mickey-Mouse Demo](demos/mickey-mouse.gif)

Output of model on Classic Movie Wizard of Oz 

![Wizard-of-Oz Demo](demos/wizard-of-oz-1.gif)

![Wizard-of-Oz Demo](demos/wizard-of-oz-2.gif)

### Scripts in this directory :

	Detect-Character.py : Recognize popular tv / movie / cartoon characters in video clips..

	Usage:

		python3 Detect-Character.py VIDEO PROJECT_ID MODEL_ID

	As these models are deployed on google-cloud, the script requires Auto-ML Project ID and Model ID
        as input parameters, in addition to the video file for predictions.

	For now, you can reach me at [amruta @ cinematrix.in] to request API credentials, while I figure
	out ways to make these models generally available.

	Coming soon: Scripts for running offline predictions using TensorFlow.JS / Docker

