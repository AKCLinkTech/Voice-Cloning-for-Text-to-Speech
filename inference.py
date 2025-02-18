import torch
from config.config import model_path
from utils.helpers import setup_device

def load_model():
    device = setup_device()
    model = ...  # Your model initialization
    model.load_state_dict(torch.load(model_path))
    model.to(device)
    model.eval()
    return model

def text_to_speech(text):
    model = load_model()
    # Convert text to speech using the model
    speech = model.generate(text)
    return speech

if __name__ == "__main__":
    import sys
    text = " ".join(sys.argv[1:])
    speech = text_to_speech(text)
    # Save or play the speech output
