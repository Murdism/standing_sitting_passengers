# standing_sitting_passengers
This is project is part of RTA competition 2023 Academia catagory.  
**Developed by** :  Murad Mebrahtu   
**Model** :  Based on [yolov7](https://github.com/WongKinYiu/yolov7) 


## Passenger_monitoring_system
Main components
- Passenger counting and Monitoring
- Number of available sits
# ENV Set Up:
- Python 3.10.8
- Torch  1.13.0 

## Creating ENV  
Using Conda:  
```
conda create -n passenger_env  python==3.10.8
```

To activate use:  
```
conda activate passenger_env 
```

Install the rest of the requirements using the following command:
``` 
pip install -r requirements.txt 
```
## Results:
Results of training can be found [HERE](https://github.com/Murdism/standing_sitting_passengers/tree/main/runs/train/yolov7_passenger_monitoring_Final).  
Trained Model can be found [HERE](https://github.com/Murdism/standing_sitting_passengers/tree/main/runs/train/yolov7_passenger_monitoring_Final/weights).

 
# Run
## Running with ROS 
Running with ROS requires you to have ROS packages installed (rospy):
- Start ROS:
```  
roscore 
```  
- Set the flag ***--ros_topic*** to True to run and publish Results. Just add --ros_topic when running detect.py

- The results will be published on rostopic ***Passenger*** by default. The rate will be 10hz. Those parameters can be updated from [config.py](https://github.com/Murdism/standing_sitting_passengers/blob/main/config.py)
-  To see results of the publisher, run the following command on terminal:
```  
rostopic echo Passenger 
```
- The Results will look something like this: 
<pre>
layout: 
  dim: []
  data_offset: 0
data: [1, 0]
</pre>
The information we need is saved on data: 
  - The first term data[0] : Number of ***Sitting Passengers***
  - The Second term data[1] : Number of ***Standing Passengers***  
In the above sample, there is only one person detected and he/she is sitting.  
## Run Detector 
### ***To Run Code (Webcam) video:***
***Without ROS***  
```  
python detect.py --weights 'runs/train/yolov7_passenger_monitoring_Final/weights/best.pt' --conf 0.25 --img-size 640 --source 0

```
***With ROS***
```  
python detect.py --weights 'runs/train/yolov7_passenger_monitoring_Final/weights/best.pt' --conf 0.25 --img-size 640 --ros_topic --source 0

```
The model was trained for 300 epochs, if you want to use the last saved weight; use the following:
```    
python detect.py --weights 'runs/train/yolov7_passenger_monitoring_Final/weights/last.pt' --conf 0.25 --img-size 640 --source 0
```
### **NOTE:** 
Source could be 0,1 or other number.  
If not sure or want to select one camera from multiple, use the following command to list all available cameras:    
```   
v4l2-ctl --list-devices
```
if you do not have the packages to view devices use the following command to install:
``` 
sudo apt-get install v4l-utils  
```
### *To Run Code Image:*  
```   
python detect.py --weights 'runs/train/yolov7_passenger_monitoring_Final/weights/best.pt' --conf 0.25 --img-size 640 --source path/images/image.jpg
```

### **NOTE:** 
*path/images/image.jpg*:  is path of the image.

# To Train
Download Dataset from:
[Dataset](https://kuacae-my.sharepoint.com/:f:/g/personal/100043387_ku_ac_ae/EuWNC6lIqbFKnhFcOijec44BSKkB2czz8lFgPPHaTcAtlQ?e=dT1Xju)


![](https://kuacae.sharepoint.com/:v:/s/Self-drivingCarsResearch/EaFvzItQ7whFvKm51GT30scBnhQi4lAnPJqvqIbumJFldg?e=KI3Jhe)
