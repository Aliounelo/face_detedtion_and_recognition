# Face detection & recognition

This little project is a study about object detection especially, Face recognition. Object detection is the technique of identifying objects present in images and videos. It is one of the most important applications of machine learning and deep learning. There are many algorithms for that task, but we will only focus on :

    +Viola-Jones algorithm ( Machine Learning) :

    This algorithm is widely used for face detection in the image or real-time. It performs Haar-like feature extraction from the image. This generates a large number of features. These features are then passed into a boosting classifier. This generates a cascade of the boosted classifier to perform image detection. An image needs to pass to each of the classifiers to generate a positive (face found) result. The advantage of Viola-Jones is that it has a detection time of 2 fps which can be used in a real-time face recognition system.
