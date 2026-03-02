from ultralytics import YOLO
import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    model = YOLO('yolo26n.pt')
    result = model.train(
        data = 'data.yaml',
        epochs = 10,
        imgsz = 640,
        batch = 16
    )

if __name__ == '__main__':
    main()


















































































































