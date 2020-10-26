import librosa
import numpy as np
from collections import Counter
from scipy.stats import entropy

def get_spl(wav):
    '''
    max sound pressure level (decibel) at each timestamp, dtype=np.array
    '''
    stft = np.abs(librosa.stft(wav))
    spl = librosa.power_to_db(stft**2, ref=1.0)
    spl_transpose = spl.T
    
    mixed_spl = np.array([max(spl_transpose[i]) for i in range(len(spl_transpose))])
    mixed_spl[mixed_spl<0] = 0
    
    return mixed_spl


def get_reaction_score(wav_data, threshold=10):

    wav, sr = wav_data
    spl = get_spl(wav)

    for i in range(len(spl)):
        if spl[i] >= threshold:
            reaction_time_in_second = i * 1/sr
            break
    return np.power(np.e, -reaction_time_in_second/10) * 10


def get_loudness_score(wav_data):
    wav, _ = wav_data
    spl = get_spl(wav)
    loudness_strength = np.mean(spl)
    if 30 <= loudness_strength <= 40:
        loudness_score = 10
    elif loudness_strength < 30:
        loudness_score = 10 - 1 / np.power(np.e, -5 / loudness_strength)
    else:
        loudness_score = 10 - 1 / np.power(np.e,  -loudness_strength / 280)

    return loudness_score


def get_tempo_score(wav_data):
    wav, sr = wav_data
    onset_env = librosa.onset.onset_strength(wav, sr=sr)
    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)[0]
    if tempo <= 130:
        tempo_score = 10 - 1 / np.power(np.e, -26 / tempo)
    else:
        tempo_score = 10 - 1 / np.power(np.e, -tempo / 910)

    return tempo_score

if __name__=="__main__":
    sample = "./data/sample.wav"
    wav, sr = librosa.load(sample)
    get_impression_score((wav,sr))