
# Projects Built in Auto-ML

## Character Recognition

#### Customized Object Detection Models to Detect Famous TV / Movie / Cartoon Characters

Output of model trained on famous Mickey Mouse Show

![Mickey-Mouse Demo](demos/mickey-mouse.gif)

Output of model trained on Classic Movie Wizard of Oz 

![Wizard-of-Oz Demo](demos/wizard-of-oz-1.gif)

![Wizard-of-Oz Demo](demos/wizard-of-oz-2.gif)

### Scripts in this directory :

	Detect-Character.py : Recognize popular tv / movie / cartoon characters..

	Usage:

		python3 Detect-Character.py VIDEO PROJECT_ID MODEL_ID

	In addition to the input video file, this script takes Auto-ML Project ID and Model ID
        as input parameters. Once the model is trained and deployed in Google Cloud, simply
        pass the corresponding project and model IDs to run this script.

	You can reach me at [amruta @ cinematrix.in] to request API credentials.

	Coming soon: Scripts for running offline predictions using TensorFlow.JS / Docker

