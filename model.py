import json
import torch
from torchvision import models
from transforms import transform_image
from utils import load_class_index

model = models.densenet121(weights='IMAGENET1K_V1')
model.eval()

imagenet_class_index = load_class_index()

def get_prediction(image_bytes):
    tensor = transform_image(image_bytes)
    with torch.no_grad():
        outputs = model(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    return imagenet_class_index[predicted_idx]