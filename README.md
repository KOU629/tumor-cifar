# Tumor-CIFAR

This is the supplementary material for the oral-presentation paper of MICCAIW-MLMI 2019: 

"Distanced LSTM: Time-Distanced Gates in LSTM to adapt Longitudinal Lung Cancer Detection". 

and Journal Version: 

"Time-Distanced Gates in Long Short Term Memory Networks", Medical Image Analysis, 2020 (IF=11.15).

Please cite our paper if you find our work is helpful to you. 

<img src="https://github.com/MASILab/tumor-cifar/blob/master/Figure.png" width="700">

---------------------------------------------------------------------------------------------

## Functions to Generate Simulation Set

In the python code script we have 4 functions:

1. get_csv_v1:

This function generate the meta information for tumor-CIFAR-v1 and save it in a csv file. The meta information includes: image name, image time point, nodule position, ground truth (cancer or non-cancer) and nodule size.

2. get_csv_v2:

This function is for tumor-CIFAR-v2, serve the same function as get_csv_v1.

3. get_nodule_img:

Generating the image according to meta information from csv file.

4. add_nodule:

This function is called by get_nodule_img, which transfer the nodule information to image and add noise.



--------------------------------------

## Usage

### Generate Dataset
There is an example showing how to use the data in demo_submit.ipynb.

### Setup (Windows, PowerShell)

1) Create and activate a virtual environment (VS Code uses it automatically if configured)

2) Install dependencies (CPU)

```powershell
& ".\.venv\Scripts\python.exe" -m pip install -U pip setuptools wheel
& ".\.venv\Scripts\python.exe" -m pip install -r requirements.txt
```

Optional: Install GPU build (CUDA). Pick your CUDA version, e.g., cu121:

```powershell
# Example for CUDA 12.1 wheels
& ".\.venv\Scripts\python.exe" -m pip install --index-url https://download.pytorch.org/whl/cu121 torch torchvision
```

3) Verify environment

```powershell
& ".\.venv\Scripts\python.exe" scripts\check_env.py
```

4) Prepare CSV from provided T-dirs (if needed)

```powershell
& ".\.venv\Scripts\python.exe" scripts\gen_csv_from_T_dirs.py --root "tumor-cifar-v1" --phase train
& ".\.venv\Scripts\python.exe" scripts\gen_csv_from_T_dirs.py --root "tumor-cifar-v1" --phase test
```

### Training (Smoke Run)

Default config is `cifar10.yaml`. Set `save_path` to a writable folder, then run:

```powershell
& ".\.venv\Scripts\python.exe" new_main.py
```

You can also use templates in `configs/`:

```powershell
Copy-Item configs\cifar10.cpu.yaml cifar10.yaml -Force
# or for GPU oriented run
Copy-Item configs\cifar10.gpu.yaml cifar10.yaml -Force
& ".\.venv\Scripts\python.exe" new_main.py
```

<img src="https://github.com/MASILab/tumor-cifar/blob/master/illustration.png" width="600">

--------------------------------------

## Document

The file TumorCIFAR_materials.pdf describes why and how we create the Tumor-CIFAR. Please email Riqiang Gao (riqiang.gao@vanderbilt.edu) if you have further concerns. 
