import os
from django.apps import AppConfig
from transformers import BertTokenizer, BertForQuestionAnswering
from QA_VTA.qa_vta import VTA

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    tokenizer = None
    model = None
    model_path = None
    context_path = None
    model_root_dir = os.path.abspath('./vta_qa_model')
    capstone_qa_vta = None

    def ready(self):
        if os.path.exists(self.model_root_dir):
            self.model_path = os.path.abspath('./vta_qa_model/model/vta_model_bert_7alpha')
            self.tokenizer = BertTokenizer.from_pretrained(self.model_path, local_files_only=True)
            self.context_path = os.path.abspath('./vta_qa_model/training/newdataset/vista.json')
            self.model = BertForQuestionAnswering.from_pretrained(self.model_path, local_files_only=True)
        self.capstone_qa_vta = VTA(self.model, self.tokenizer, self.context_path)
