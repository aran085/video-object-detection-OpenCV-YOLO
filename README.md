
# Video-Object-Detection-OpenCV-YOLO

This repo is designed for real-time object detection in (youtube) video streams utilizing:
* Python 3.6

To install necessary packages, use the following command:
```
$  pip install numpy pandas argparse datetime pafy streamlink flask_opencv_streamer youtube-dl flask_opencv_streamer opencv-contrib-python
```

This project also uses the YOLOv3 detection method (https://pjreddie.com/darknet/yolo/) and Streamlink (https://github.com/streamlink/streamlink).

Object detection in video streams occurs every x seconds with the number of detected objects being written to an output file. The frequency of detection is adjustable and performance dependent. The OpenCV library with YOLOv3 detection method forms the foundation of this process. For an introduction to OpenCV and YOLO, you can refer to: https://www.pyimagesearch.com/2018/11/12/yolo-object-detection-with-opencv/. This project's source code began with the repository by aran085.

## YOLO Weights:

To use the project, you need to download the YOLOv3 weights:
`$ wget https://pjreddie.com/media/files/yolov3.weights`
The weights were trained on the COCO dataset (http://cocodataset.org)

## Example Output Jackson Hole Town Square Webcam
 Sample youtube streams: Jackson Hole Wyoming USA Live Cams - SeeJH.com
* https://youtu.be/1EiC9bvVGnk
* https://youtu.be/RZWzyQuFxgE
Here user set:
* confidence level 0.30
* threshold level 0.55

Below are some output samples:
<br><br>
![](JacksonHole1.jpg)
<br><br>
![](JacksonHole2.jpg)