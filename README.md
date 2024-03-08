
# Aicapella-CNN-Based-Voice-Isolator
A Convolutional Neural Network Based audio vocal separator.


This is an extremely simple tool for separating vocals from its music, completely localized for web operation.


#### UNet Architecture
![App Screenshot](https://github.com/shresthasubham/Aicapella-CNN-Based-Voice-Isolator/blob/master/unet.png?raw=true)

## Running in Notebook /Colabs

Run in Google Colab or any other notebook from the given .ipynb at /src/

```bash
  minorAICAPELLAgpu.ipynb
```
For testing,set up model and proper directory path in source code
```bash
  testing.ipynb
```
## Run Locally

Clone the project

```bash
  git clone git@github.com:shresthasubham/Aicapella-CNN-Based-Voice-Isolator.git
```
Go to the project directory

```bash
  cd Aicapella-CNN-Based-Voice-Isolator
```


Create a virtual environment

```bash
 python -m venv venv
```


Activate the environment. On Windows, the command is
 ```bash 
%cd%/venv/scripts/activate
```
and on Linux and Mac, the command is 
```bash
 source ./venv/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Go to the frontend directory

```bash
  cd src/front
```
Execute  
```bash
  python app.py
```
 and wait for the local browser window to open and Enjoy.

## Screenshots

![App Screenshot](https://github.com/shresthasubham/Aicapella-CNN-Based-Voice-Isolator/blob/755bdf534f0dd2c40b60842834df3080c438f96c/fro.png?raw=true)


## Documentation

[Documentation](https://github.com/shresthasubham/Aicapella-CNN-Based-Voice-Isolator/tree/master/docs)

## Drive link
[Drive]([https://github.com/shresthasubham/Aicapella-CNN-Based-Voice-Isolator/tree/master/docs](https://drive.google.com/drive/folders/19WO-Xl-0wD24SWnnCFSWcR8CzwbCJw0B?usp=sharing))


## References

 - [ Singing Voice Separation With Deep U-NET Convolutinal Networks](https://openaccess.city.ac.uk/id/eprint/19289/1/7bb8d1600fba70dd79408775cd0c37a4ff62.pdf)
 - [Youtube-Valerio Velardo](https://youtu.be/iCwMQJnKk2c?si=TRWCKHeU7h-Kt9lE)


