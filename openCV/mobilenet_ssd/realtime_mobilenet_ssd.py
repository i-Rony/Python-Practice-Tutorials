# import the necessary packages
import numpy as np
import argparse
import cv2
import time
import imutils
from imutils.video import VideoStream


# initialize the list of class labels MobileNet SSD was trained to
# detect, then generate a set of bounding box colors for each class
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# load our serialized model from disk
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt.txt', 'MobileNetSSD_deploy.caffemodel')

# Get a reference to webcam #0 (the default one)
# initialize the cammera sensor for two seconds and start video stream as seperate thread
vs = VideoStream(src=0).start()
time.sleep(2.0)



# loop over the frames(images) from the video stream
while True:
	# Grab a single frame (image) of video and resize it
	# to have a maximum width of 400 pixels
	image = vs.read()
	image = imutils.resize(image, width=400)
 
	# grab the frame(image) dimensions and convert it to a blob
	(h, w) = image.shape[:2]
	blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
 
	# pass the blob through the network and obtain the detections and
	# predictions
	net.setInput(blob)
	detections = net.forward()



	# loop over the detections
	for i in np.arange(0, detections.shape[2]):
		# extract the confidence (i.e., probability) associated with the
		# prediction
		confidence = detections[0, 0, i, 2]

		# filter out weak detections by ensuring the `confidence` is
		# greater than the minimum confidence
		# type=float, default=0.2
		if confidence > 0.2:
			# extract the index of the class label from the `detections`,
			# then compute the (x, y)-coordinates of the bounding box for
			# the object
			idx = int(detections[0, 0, i, 1])
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")

			# display the prediction
			label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
			print("[INFO] {}".format(label))
			cv2.rectangle(image, (startX, startY), (endX, endY), COLORS[idx], 2)
			y = startY - 15 if startY - 15 > 15 else startY + 15
			cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

			# show the output image
			cv2.imshow("Output", image)
    # Hit 'q' on the keyboard to quit!
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()