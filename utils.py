import os

def get_model_paths():
    models_dir = os.path.expanduser("~/.ollama/models")
    model_files = []
    for root, dirs, files in os.walk(models_dir):
        for file in files:
            if file.endswith(".bin") or file.endswith(".gguf"):
                model_files.append(os.path.join(root, file))
    return model_files
