

############################################################################
#      https://pjreddie.com/darknet/install/  
############################################################################
git clone https://github.com/pjreddie/darknet.git
cd darknet
make

./darknet


GPU=1
./darknet -i 1 imagenet test cfg/alexnet.cfg alexnet.weights
./darknet -nogpu imagenet test cfg/alexnet.cfg alexnet.weights


OPENCV=1
brew search opencv
brew install opencv@2
./darknet imtest data/eagle.jpg

############################################################################

############################################################################
#	https://pjreddie.com/darknet/yolo/
############################################################################
# config files are present inside 'cfg/'

wget https://pjreddie.com/media/files/yolov3.weights
# run the detector
./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
# or use the long version command
./darknet detector test cfg/coco.data cfg/yolov3.cfg yolov3.weights data/dog.jpg


## Changing the threshold
./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg -thresh 0.25

## Tiny YOLOv3
wget https://pjreddie.com/media/files/yolov3-tiny.weights
./darknet detect cfg/yolov3-tiny.cfg yolov3-tiny.weights data/dog.jpg

## Real-Time Detection on a Webcam
# compile with GPU enabled and OpenCV then
./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights

./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights <video file>



##### Training the VOC
wget https://pjreddie.com/media/files/VOCtrainval_11-May-2012.tar
wget https://pjreddie.com/media/files/VOCtrainval_06-Nov-2007.tar
wget https://pjreddie.com/media/files/VOCtest_06-Nov-2007.tar
tar xf VOCtrainval_11-May-2012.tar
tar xf VOCtrainval_06-Nov-2007.tar
tar xf VOCtest_06-Nov-2007.tar
wget https://pjreddie.com/media/files/voc_label.py
python voc_label.py

## training data format .txt
<object-class> <x> <y> <width> <height>

cat 2007_train.txt 2007_val.txt 2012_*.txt > train.txt


Modifying cfg/voc.data
  1 classes= 20
  2 train  = <path-to-voc>/train.txt
  3 valid  = <path-to-voc>2007_test.txt
  4 names = data/voc.names
  5 backup = backup

## getting the weight
wget https://pjreddie.com/media/files/darknet53.conv.74

## Train the model
./darknet detector train cfg/voc.data cfg/yolov3-voc.cfg darknet53.conv.74





########## 

cp scripts/get_coco_dataset.sh data
cd data
bash get_coco_dataset.sh

cfg/yolo.cfg
[net]
# Testing
# batch=1
# subdivisions=1
# Training
batch=64
subdivisions=8

./darknet detector train cfg/coco.data cfg/yolov3.cfg darknet53.conv.74
./darknet detector train cfg/coco.data cfg/yolov3.cfg darknet53.conv.74 -gpus 0,1,2,3
./darknet detector train cfg/coco.data cfg/yolov3.cfg backup/yolov3.backup -gpus 0,1,2,3

#########
wget https://pjreddie.com/media/files/yolov3-openimages.weights
./darknet detector test cfg/openimages.data cfg/yolov3-openimages.cfg yolov3-openimages.weights

