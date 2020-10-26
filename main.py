from pure_voice_processing import voice_metric
import librosa
import numpy as np 

class VoiceModel:
    def __init__(self):
        pass

    def get_reaction_score(self, wav_data:np.ndarray):
        """
        Process Reaction score 
        :wav_data: Input voice data, read by librosa
        """
        return voice_metric.get_reaction_score(wav_data)

    def get_loudness_score(self, wav_data:np.ndarray):
        """
        Process Loudness score
        :wav_data: Input voice data, read by librosa
        """
        return voice_metric.get_loudness_score(wav_data)

    def get_tempo_score(self, wav_data:np.ndarray):
        """
        Process Tempo score 
        :wav_data: Input voice data, read by librosa
        """
        return voice_metric.get_tempo_score(wav_data)

    def predict(self, wav_data:np.ndarray):
        """
        Process predict all score 
        :wav_data: Input voice data, read by librosa
        """
        return {
            "score_reaction": voice_metric.get_reaction_score(wav_data), 
            "score_tempo": voice_metric.get_tempo_score(wav_data),
            "score_loudness": voice_metric.get_loudness_score(wav_data)
        }