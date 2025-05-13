import os
from django.apps import AppConfig
from llama_cpp import Llama
from QA_VTA.qa_vta import VTA

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    model = None
    model_path = None
    context_path = None
    model_root_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'VTA-tools', 'models')
    capstone_qa_vta = None

    if os.path.exists(model_root_dir):
        model_path = os.path.join(model_root_dir, 'mistral-7b-instruct-v0.2.Q4_K_M.gguf')
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}")
            
        # Инициализируем модель через llama-cpp
        try:
            model = Llama(
                model_path=model_path,
                n_ctx=2048,  # Размер контекста
                n_threads=4   # Количество потоков для обработки
            )
        except Exception as e:
            print(f"Error loading model: {e}")
            raise
        
        # Путь к датасету
        context_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                                  'vta_qa_model', 'training', 'newdataset', 'vista.json')
        if not os.path.exists(context_path):
            raise FileNotFoundError(f"Context file not found at {context_path}")
    else:
        print(f"Directory: {model_root_dir} does not exist")

    def ready(self):
        if self.model and self.context_path:
            self.capstone_qa_vta = VTA(self.model, None, self.context_path)
