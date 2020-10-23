import io
import librosa
import numpy as np 

def wav_to_ndarray(filename, data_bytes):
    the_file = io.BytesIO(data_bytes)

    wav, sr = librosa.load(the_file, sr=None)
    return wav, sr
