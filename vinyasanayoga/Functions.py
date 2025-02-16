#importing libraries
import cv2
import mediapipe as mp
import numpy as np
import os
import threading
import pygame
import pyttsx3
import streamlit as st
import base64


mp_drawing=mp.solutions.drawing_utils
mp_pose=mp.solutions.pose

pygame.mixer.init()

gif_placeholder = st.empty()

def Plank_Pose(landmarks,lang):
    message=[]
    elbow_x,elbow_y=landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y
    wrist_x,wrist_y=landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y
    hip_x,hip_y=landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y
    shoulder_x,shoulder_y=landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y
    knee_x,knee_y=landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y

    if(angle([shoulder_x,shoulder_y],[hip_x,hip_y],[knee_x,knee_y])<160):
        feedback=6
    else:
         return "perfect"
    tts_thread = threading.Thread(target=speech, args=(os.path.join('.','languages','feedback',f'{lang}',f'{feedback}.mp3'),))
    tts_thread.start()
    return None

def Cobra(landmarks,lang):
    message=[]
    shoulder_x,shoulder_y=landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y
    hip_x,hip_y=landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y
    knee_x,knee_y=landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y
    if(angle([shoulder_x,shoulder_y],[hip_x,hip_y],[knee_x,knee_y])>135):
        feedback=8
    else:
         return "perfect"
    
    tts_thread = threading.Thread(target=speech, args=(os.path.join('.','languages','feedback',f'{lang}',f'{feedback}.mp3'),))
    tts_thread.start()
    return None

def AdhoMukha(landmarks,lang):
    message=[]
    elbow_x,elbow_y=landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y
    shoulder_x,shoulder_y=landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y
    hip_x,hip_y=landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y
    knee_x,knee_y=landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y
    l_ankle_x,l_ankle_y=landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y
    if(angle([shoulder_x,shoulder_y],[hip_x,hip_y],[knee_x,knee_y])>90):
        feedback=11
    elif(angle([elbow_x,elbow_y],[shoulder_x,shoulder_y],[hip_x,hip_y])>168):
        feedback=6
    if(angle([hip_x,hip_y],[knee_x,knee_y],[l_ankle_x,l_ankle_y])>168):
        feedback=2
    else:
         return "perfect"
    tts_thread = threading.Thread(target=speech, args=(os.path.join('.','languages','feedback',f'{lang}',f'{feedback}.mp3'),))
    tts_thread.start()
    return None

def ChathurangaDandasana(landmarks,lang):
    message=[]
    elbow_x,elbow_y=landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y
    wrist_x,wrist_y=landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y
    hip_x,hip_y=landmarks[mp_pose.PoseLandmark.LEFT_HIP.vlaue].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.vlaue].y
    shoulder_x,shoulder_y=landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y
    Knee_x,knee_y=landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y

    if(angle([shoulder_x,shoulder_y],[hip_x,hip_y],[Knee_x,knee_y])<160):
        feedback=6
    elif(angle([shoulder_x,shoulder_y],[elbow_x,elbow_y],[wrist_x,wrist_y])>120):
        feedback=122312
    else:
        return "perfect"
    tts_thread = threading.Thread(target=speech, args=(os.path.join('.','languages','feedback',f'{lang}',f'{feedback}.mp3'),))
    tts_thread.start()
    return None


