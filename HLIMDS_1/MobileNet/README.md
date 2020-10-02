# MobileNet_SSD_opencv
MobileNet-SSD object detection in opencv 3.4.1 and python 3 or 2

Назначение параметров:
--video:    Path to video file. If empty, camera's stream will be used
--prototxt: Path to text network file: MobileNetSSD_deploy.prototxt for Caffe model (default="MobileNetSSD_deploy.prototxt")
--weights:  Path to weights: MobileNetSSD_deploy.caffemodel for Caffe model (default="MobileNetSSD_deploy.caffemodel")
--thr:      confidence threshold to filter out weak detections (default=0.2, type=float)

Программа изначально работает с файлами, установленными по умолчанию, они должны находиться в одной директории с программой, для использования своих используйте параметры.

Программа производит поиск объектов на видеопотоке или в видеофайле, обводит найденные объекты в рамку, выводит название и вероятность определения, также дуюлирует эти данные в консоль.
К каждому фрагменту кода в файле mobilenet_ssd_python.py есть комментарии, поясняющие те или иные решения в программном коде. 