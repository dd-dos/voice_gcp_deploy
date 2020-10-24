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


def get_reaction_score(wav_data, threshold=20):

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
    min_dB = 30
    max_dB = 100
    score_range = [
        [0,10,6],
        [10,20,7],
        [20,30,8],
        [30,40,10],
        [40,50,8],
        [60,70,7],
        [70,80,6],
        ['','',5]
    ]

    score_counter = np.zeros(len(score_range))
       
    for spl_value in spl:
        for i in range(len(score_range)):
            if spl_value < min_dB or spl_value > max_dB:
                score_counter[-1] += 1
                break
            if score_range[i][0] <= spl_value <= score_range[i][1]:
                score_counter[i] += 1
                break
    
    temp = np.array(score_range).T
    values = temp[2,:].astype(float)
    result = np.dot(values,score_counter)/np.sum(score_counter)
            
    return result


def get_impression_score(wav_data):
    wav, sr = wav_data
    chroma = librosa.feature.chroma_stft(wav, sr) #shape (12,)

    high_pitch = []
    for k in range(len(chroma.T)):
        high_pitch.append([i for i, j in enumerate(chroma.T[k]) \
                            if j==max(chroma.T[k])])
    high_pitch = sum(high_pitch, [])
    bases = Counter(high_pitch)
    dist = [x/sum(bases.values()) for x in bases.values()]
    entropy_value = entropy(dist, base=2)
    
    max_entropy = -np.log2(1/12)
    impression_score = entropy_value / max_entropy * 10
    return impression_score


def get_tempo_score(wav_data):
    wav, sr = wav_data
    onset_env = librosa.onset.onset_strength(wav, sr=sr)
    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)[0]
    if tempo < 120:
        return tempo / 12
    else:
        return (1-tempo/240) * 10


if __name__=="__main__":
    sample = "./data/sample.wav"
    wav, sr = librosa.load(sample)
    get_impression_score((wav,sr))