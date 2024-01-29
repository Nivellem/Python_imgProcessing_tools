## inference_realesrgan with changes:
chose folder
put output in subfolder"Upscale_" + os.path.basename(folder_path)

FileNotFoundError: [Errno 2] No such file or directory: 'experiments/pretrained_models/RealESRNet_x4plus.pth' 
It worked when I changed the path in  options/finetune_realesrgan_x4plus.yml
from:
pretrain_network_g: experiments/pretrained_models/RealESRNet_x4plus.pth
to:
pretrain_network_g: experiments/pretrained_models/RealESRGAN_x4plus.pth

# install Real-ESRGAN

Install python 3.10.11

https://www.python.org/downloads/release/python-31011/

Install Nvidia CUDA
https://developer.nvidia.com/cuda-11-8-0-download-archive

Install Git
https://git-scm.com/downloads

```powershell
# clone git repo
git clone https://github.com/xinntao/Real-ESRGAN.git

# Enter repo folder
cd Real-ESRGAN

```


```powershell

# be sure you are in Real-ESRGAN folder

pip install onnxmltools
pip install wheel

pip install torch==2.0.0+cu118 -f https://download.pytorch.org/whl/torch_stable.html
pip install torchvision==0.15.1+cu118 -f https://download.pytorch.org/whl/torch_stable.html

# Install basicsr - https://github.com/xinntao/BasicSR
# We use BasicSR for both training and inference
pip install basicsr
# facexlib and gfpgan are for face enhancement

pip install facexlib
pip install gfpgan
pip install -r requirements.txt
python setup.py develop
```

https://github.com/onnx/onnxmltools

https://github.com/xinntao/Real-ESRGAN/issues/407

https://github.com/xinntao/Real-ESRGAN/issues/433

https://github.com/xinntao/Real-ESRGAN/issues/586
## detect if img is squere
15% tolerance

## watermark
add @Nivellem Studio watermark

## How to install llama-cpp-python

``` Error log
Error

Building wheels for collected packages: llama-cpp-python
  Building wheel for llama-cpp-python (pyproject.toml) ... error
  error: subprocess-exited-with-error

  × Building wheel for llama-cpp-python (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [20 lines of output]
      *** scikit-build-core 0.8.0 using CMake 3.28.1 (wheel)
      *** Configuring CMake...
      2024-01-29 20:16:07,178 - scikit_build_core - WARNING - Can't find a Python library, got libdir=None, ldlibrary=None, multiarch=None, masd=None
      loading initial cache file C:\Users\*\AppData\Local\Temp\tmpeuhtnr0m\build\CMakeInit.txt
      -- Building for: NMake Makefiles
      CMake Error at CMakeLists.txt:3 (project):
        Running

         'nmake' '-?'

        failed with:

         no such file or directory


      CMake Error: CMAKE_C_COMPILER not set, after EnableLanguage
      CMake Error: CMAKE_CXX_COMPILER not set, after EnableLanguage
      -- Configuring incomplete, errors occurred!

      *** CMake configuration failed
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for llama-cpp-python
Failed to build llama-cpp-python
ERROR: Could not build wheels for llama-cpp-python, which is required to install pyproject.toml-based projects
```


# How to fix


## Install VIsual Studio 2019


https://my.visualstudio.com/Downloads?q=visual%20studio%202019&wt.mc_id=o~msft~vscom~older-downloads


https://visualstudio.microsoft.com/pl/vs/older-downloads/

## Install CMake 

https://cmake.org/download/

## Install Mingw

https://code.visualstudio.com/docs/cpp/config-mingw

You can download the latest installer from the MSYS2 page or use this direct link to the installer.

Run the installer and follow the steps of the installation wizard. Note that MSYS2 requires 64 bit Windows 8.1 or newer.

In the wizard, choose your desired Installation Folder. Record this directory for later. In most cases, the recommended directory is acceptable. The same applies when you get to setting the start menu shortcuts step. When complete, ensure the Run MSYS2 now box is checked and select Finish. This will open a MSYS2 terminal window for you.

In this terminal, install the MinGW-w64 toolchain by running the following command:

```powershell
pacman -S --needed base-devel mingw-w64-ucrt-x86_64-toolchain

```

Accept the default number of packages in the toolchain group by pressing Enter.

Enter Y when prompted whether to proceed with the installation.

Add the path to your MinGW-w64 bin folder to the Windows PATH environment variable by using the following steps:

In the Windows search bar, type Settings to open your Windows Settings.

Search for Edit environment variables for your account.
In your User variables, select the Path variable and then select Edit.

Select New and add the MinGW-w64 destination folder you recorded during the installation process to the list. If you used the default settings above, then this will be the path: 

``` add to Path
C:\msys64\ucrt64\bin
```

Select OK to save the updated PATH. You will need to reopen any console windows for the new PATH location to be available.
Check your MinGW installation

To check that your MinGW-w64 tools are correctly installed and available, open a new Command Prompt and type:

```powershell
gcc --version
g++ --version
gdb --version

```

## Install Dependencies

```powershell
pip install typing-extensions
pip install numpy
pip install diskcache
pip install jinja2
pip install uvicorn
pip install fastapi
pip install pydantic-settings
pip install sse-starlette
pip install starlette-context
pip install pytest
pip install httpx
pip install scipy
pip install black
pip install twine
pip install mkdocs
pip install mkdocstrings[python]
pip install mkdocs-material

```


```powershell

git clone https://github.com/abetlen/llama-cpp-python/tree/main

```

## Open Visual Studio 2019 And open llama-cpp-python

```powershell

pip install llama-cpp-python

```

![image](https://github.com/Nivellem/Python_imgProcessing_tools/assets/84031994/1cf6c4a9-43c8-4b89-abf0-57b2575e1721)

Output 
![image](https://github.com/Nivellem/Python_imgProcessing_tools/assets/84031994/aa5638ca-256b-4ec4-9e66-9a63eef9b81e)






