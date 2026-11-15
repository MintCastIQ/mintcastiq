# models/clip_encoder.py

import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

_device = "cuda" if torch.cuda.is_available() else "cpu"
_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(_device)
_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def image_embedding(pil_img):
    inputs = _processor(images=pil_img, return_tensors="pt").to(_device)
    with torch.no_grad():
        emb = _model.get_image_features(**inputs)
    return emb.cpu().numpy()[0]

def best_label(pil_img, labels):
    inputs = _processor(images=pil_img, text=labels, return_tensors="pt", padding=True).to(_device)
    with torch.no_grad():
        outputs = _model(**inputs)
        probs = outputs.logits_per_image.softmax(dim=1)[0]
        idx = torch.argmax(probs).item()
    return labels[idx], float(probs[idx])
