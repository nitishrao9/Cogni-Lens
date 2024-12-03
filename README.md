# Cogni-Lens
#Lumi Sight
**Project Overview:**
This project focuses on enhancing the quality of life for individuals diagnosed with Alzheimer’s and Frontotemporal Dementia (FTD) through the use of innovative technology. The system integrates smart glasses, smartwatch, and a mobile app, equipped with artificial intelligence (AI) and advanced hardware, to assist patients in recognizing familiar faces, performing day-to-day tasks, navigating their environment, and communicating with caregivers.

The system is designed to help patients cope with cognitive challenges by providing support for memory recall, location tracking, safety monitoring, and health-related notifications. These devices work in harmony to provide a seamless user experience that is both effective and unobtrusive.

Key Components of the System:
(a) Smart Glasses: AI-powered smart glasses equipped with facial recognition technology to identify people the patient is familiar with, including their name, age, and relationship. This feature helps patients in recognizing family members and caregivers, fostering a sense of familiarity.
The system stores new face data in the cloud for future reference, allowing for continuous learning and adaptation.

(b) Smartwatch: A motion sensor-equipped smartwatch monitors the patient's activity to ensure the device is being worn. If the device is removed, the system triggers an alarm to notify caregivers or family members.

In addition to activity tracking, the smartwatch includes features such as heart rate monitoring and fall detection, ensuring that the patient is constantly being monitored for potential health issues.

(c) Mobile App: The mobile app allows family members and caregivers to monitor the patient's location and status in real-time. It provides geofencing capabilities, sending alerts if the patient exits a predefined area.
The app also integrates with the smart glasses and smartwatch, providing a centralized platform for managing the patient’s health and safety.

Features of the System:
(i) Facial Recognition: AI-driven face recognition technology integrated into the smart glasses to help patients recognize familiar faces, reducing feelings of confusion and isolation.
(ii) Fall Detection and Safety Alerts: Using the smartwatch’s motion sensors, the system detects falls and sends immediate alerts to caregivers.
Location Tracking and Geofencing: The mobile app allows caregivers to track the patient’s location in real-time and receive notifications when the patient leaves a predefined safe area.
(iii) Health Monitoring: Real-time health status, including heart rate and activity levels, is monitored through the smartwatch, providing insights into the patient's well-being.
(iv) Cloud Integration: All data is stored securely in the cloud, enabling easy access and real-time updates for both the patient and caregivers.



Intel Tools and Techniques Used:
This project leverages various Intel Developer Tools and AI techniques to ensure optimal performance, real-time processing, and efficient resource utilization.

Intel OpenVINO Toolkit: The Intel OpenVINO™ Toolkit is used to optimize deep learning models for Intel hardware, significantly improving performance on devices like the smart glasses. OpenVINO helps accelerate computer vision tasks such as face detection and object recognition, making the system more responsive and accurate.
Model Optimization: Pre-trained models for face detection and recognition are optimized using OpenVINO’s Model Optimizer, allowing for faster inference and lower latency.
Inference on Intel Devices: OpenVINO enables the execution of optimized models on Intel CPUs, GPUs, and VPUs, ensuring that facial recognition and other AI tasks are processed efficiently.

**Intel’s Deep Learning Deployment Toolkit:**
The Intel® Distribution of OpenVINO™ is used for deploying deep learning models efficiently, especially for real-time tasks like face recognition, enabling the AI system on the smart glasses to quickly identify and match faces.
(A) Intel® AI Analytics Toolkit: Utilized for fine-tuning models and ensuring that the AI-powered facial recognition system delivers accurate and real-time results. The toolkit helps optimize the underlying machine learning models used for face embedding and similarity checks.

(B) Intel® Threading Building Blocks (TBB): Intel TBB is employed to optimize parallelism and concurrency in the software. This enables efficient processing, especially in real-time applications like face recognition, where the system needs to process multiple frames per second.

(C) Intel® OpenCL™ and Python Optimization: By using Intel-optimized Python libraries, the performance of computationally intensive tasks is significantly improved. Libraries like NumPy and OpenCV are used in conjunction with Intel-optimized Python to achieve high performance in tasks such as face cropping, scaling, and image processing.

(D) Intel® Computer Vision SDK: This toolkit is used for implementing optimized algorithms in computer vision tasks, such as face detection and recognition. It enables the smart glasses to identify faces in real time with minimal latency.


**Intel Optimized Python**
This project is developed using Intel Optimized Python, which enhances the performance of Python applications, particularly those that require high computational power, such as AI-based applications in real-time systems. Intel-optimized libraries for NumPy, OpenCV, and other Python modules are integrated into the system to ensure that tasks like image processing and model inference are as fast as possible.


**Conclusion**
This system integrates state-of-the-art AI and Intel-optimized tools to assist individuals with Alzheimer’s and FTD, improving their daily lives by providing memory recall, location tracking, health monitoring, and safety features. By using Intel OpenVINO, Intel Optimized Python, and other Intel technologies, this project ensures that the system operates efficiently and delivers real-time results, providing a seamless experience for both patients and caregivers.
