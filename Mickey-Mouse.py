import sys
import cv2

# importing auto-ml libraries
from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2

# provide Project ID and Model ID to run Auto-ML
project_id = sys.argv[1]
model_id = sys.argv[2]

# detects characters from a given video frame
def detect_mickey(frame):
    model = automl_v1beta1.PredictionServiceClient()
    path = "projects/" + project_id + "/locations/us-central1/models/" + model_id
    result = model.predict(path, {'image': {'image_bytes': frame}})
    return result

# provide input video to process
stream = cv2.VideoCapture("sample-videos/mickey-1.mp4")

# assign color-codes based on class-labels
color_codes = { 'mickey_mouse': {'R': 0, 'G': 128, 'B': 255},
'donald_duck': {'R': 178, 'G': 102, 'B': 255},
'goofy': {'R': 255, 'G': 153, 'B': 51}}

# for Mac OS, this is the codec for writing mp4 files
codec = cv2.VideoWriter_fourcc('m','p','4','v')
frame_rate = 15
# output video file
output = cv2.VideoWriter('mickey1-output.mp4', codec, frame_rate, (1280,720), True)

# process input video frame by frame
while 1:
    flag, frame = stream.read()
    if flag:

        # converting frame into base-64 format
        cv2.imwrite('test.png', frame)
        with open('test.png', 'rb') as image_file:
            image_data = image_file.read()

            result = detect_mickey(image_data)

            # parse API response
            for character in result.payload:
                # get character name
                label = character.display_name

                # get bounding box co-ordinates
                bbox = character.image_object_detection.bounding_box
                x1 = round(bbox.normalized_vertices[0].x * 1280)
                y1 = round(bbox.normalized_vertices[0].y * 720)
                x2 = round(bbox.normalized_vertices[1].x * 1280)
                y2 = round(bbox.normalized_vertices[1].y * 720)

                # get color code
                color = color_codes[label]

                # print label and box on frame
                cv2.rectangle(frame, (x1, y1), (x2, y2), (color['R'], color['G'], color['B']), 2)

                if(y1-30 > 0):
                    # put label on top
                    cv2.rectangle(frame, (x1, y1-30), (x1+130, y1), (color['R'], color['G'], color['B']), cv2.FILLED)
                    cv2.putText(frame, label, (x1, y1-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
                else:
                    # put label below the box
                    cv2.rectangle(frame, (x1, y1+30), (x1+130, y1), (color['R'], color['G'], color['B']), cv2.FILLED)
                    cv2.putText(frame, label, (x1, y1+10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))

        # display output frame and write to mp4 file
        cv2.imshow('Mickey-Mouse', frame)
        output.write(frame)

        if cv2.waitKey(1)&0xFF == ord('q'):
            break
    else:
        break

stream.release()
output.release()
cv2.destroyAllWindows()
