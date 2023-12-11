#%%
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sounddevice as sd
import pandas as pd
from scipy.interpolate import interp1d

def generate_pink_noise(num_samples):
    """
    Gera ruído rosa com um número especificado de amostras.
    """
    white_noise = np.random.randn(num_samples)
    pink_noise = np.zeros(num_samples)
    
    B = [0.02109238, 0.07113478, 0.68873558]  # Coeficientes do filtro
    A = [1, -1.80248508, 0.80248432]          # Coeficientes de feedback
    
    for i in range(2, num_samples):
        pink_noise[i] = (B[0] * white_noise[i] + B[1] * white_noise[i - 1] + 
                         B[2] * white_noise[i - 2] - A[1] * pink_noise[i - 1] - 
                         A[2] * pink_noise[i - 2])

    return pink_noise

def normalize_audio(audio_data):
    """
    Normaliza o áudio para a amplitude máxima permitida.
    """
    max_amplitude = np.max(np.abs(audio_data))
    normalized_audio = audio_data / max_amplitude
    return normalized_audio

def plot_audio_waveform(audio_data, title="Audio Waveform"):
    """
    Plota a forma de onda de um sinal de áudio.
    """
    plt.plot(audio_data)
    plt.title(title)
    plt.xlabel("Sample")
    plt.ylabel("Amplitude")
    plt.show()

def play_audio(audio_data, sample_rate):
    """
    Reproduz um sinal de áudio.
    """
    sd.play(audio_data, samplerate=sample_rate)
    sd.wait()

def calculate_reverberation_time_per_frequency(dimensions, absorption_coeffs_floor, absorption_coeffs_wall, frequencies):
    volume = np.prod(dimensions)
    area_total = 2 * (dimensions[0] * dimensions[1] + dimensions[1] * dimensions[2] + dimensions[0] * dimensions[2])
    reverberation_times = []

    for i, freq in enumerate(frequencies):
        absorption_total = area_total * (absorption_coeffs_floor[i] + absorption_coeffs_wall[i])
        reverberation_time = 0.161 * volume / absorption_total
        reverberation_times.append({'Frequência': freq, 'Tempo de Reverberação': reverberation_time})

    return pd.DataFrame(reverberation_times)

# Parâmetros do ambiente
DIMENSOES = (5.95, 8.1, 3.26)
FREQUENCIAS = [125, 250, 500, 1000, 2000, 4000]
ABSORCAO_PISO = [0.01, 0.01, 0.01, 0.02, 0.02, 0.02] # Piso Cerâmico
ABSORCAO_PAREDE = [0.14, 0.10, 0.06, 0.05, 0.04, 0.03] # Parede Pintada
    #Adicionar os Outros Valores



# Calcula o tempo de reverberação para cada frequência
df_reverberacao = calculate_reverberation_time_per_frequency(DIMENSOES, ABSORCAO_PISO, ABSORCAO_PAREDE, FREQUENCIAS)

# Interpolação polinomial para suavizar a curva
interp_polynomial = interp1d(df_reverberacao['Frequência'], df_reverberacao['Tempo de Reverberação'], kind='quadratic')
frequencias_suaves = np.linspace(min(FREQUENCIAS), max(FREQUENCIAS), 300)
tempos_suaves = interp_polynomial(frequencias_suaves)

# Plota os tempos de reverberação
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
plt.plot(frequencias_suaves, tempos_suaves, label='Curva Suavizada')
plt.title("Tempo de Reverberação por Frequência")
plt.ylabel("Tempo de Reverberação (segundos)")
plt.xlabel("Frequência (Hz)")
plt.legend()
plt.show()

# Gera e reproduzir ruído rosa em altura máxima
N = 44100  # Número de amostras para 1 segundo de áudio
pink_noise = generate_pink_noise(N)
normalized_pink_noise = normalize_audio(pink_noise)
play_audio(normalized_pink_noise, N)

# %%
