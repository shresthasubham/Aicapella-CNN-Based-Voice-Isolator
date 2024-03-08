import tensorflow as tf
from tensorflow import keras
import librosa
import numpy as np
import os
import soundfile

WINDOW_SIZE=1024
HOP_LENGTH=256
SR =  16000
BASE_DIR = os.path.dirname(__file__)
uploads_file_path = os.path.join(BASE_DIR,'static/uploads/uploaded_song.wav')
outputs_file_path = os.path.join(BASE_DIR,'static/outputs/output_song.wav')
models_file_path =  os.path.join(BASE_DIR,'static/models/100model.keras')
def LoadAudio(file_path) :
    y, sr = librosa.load(file_path,sr=SR)
    stft = librosa.stft(y,n_fft=WINDOW_SIZE,hop_length=HOP_LENGTH)
    mag, phase = librosa.magphase(stft)
    mag = mag**2
    mag = librosa.power_to_db(mag)
    mag = mag.astype(np.float32)
    norm = mag.max()
    mag /= norm
    return mag, phase, norm

def extract_vocals():

    test_song_mag, test_song_phase, norm = LoadAudio(uploads_file_path)
    trained_model = keras.models.load_model(models_file_path)
    
    x_test = []
    num_chunks = test_song_mag.shape[1]//128
    
    for i in range(num_chunks):
        chunk = test_song_mag[:512, i * 128 : (i + 1) * 128, np.newaxis]
        x_test.append(chunk)

    x_test = np.asarray(x_test, dtype = np.float32)
    y_test = trained_model.predict(x_test)


    reconstructed_song =  np.zeros((512, 128*len(y_test), 1))
    for i, chunk in enumerate(y_test):
        reconstructed_song[:, i * 128:(i + 1) * 128, :] = chunk

    reconstructed_song = np.squeeze(reconstructed_song, axis=-1)

    reconstructed_song = reconstructed_song*norm

    reconstructed_song =  reconstructed_song.astype(np.float32)
    reconstructed_song = librosa.db_to_power(reconstructed_song)
    reconstructed_song = reconstructed_song ** 0.5

    test_song_phase = test_song_phase[:512,:128*len(x_test)]


    spectrum = reconstructed_song * np.exp(1j*test_song_phase)


    final_audio = librosa.istft(spectrum)
    soundfile.write(outputs_file_path, final_audio, SR)





if __name__ == "__main__":
    print("hello")