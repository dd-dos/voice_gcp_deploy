from mlchain.base import ServeModel
from mlchain.base.converter import Converter
import numpy as np 
from utils.utils import wav_to_ndarray

Converter.add_convert_file("wav", wav_to_ndarray, np.ndarray)
from main import VoiceModel

model = VoiceModel()
serve_model = ServeModel(model)