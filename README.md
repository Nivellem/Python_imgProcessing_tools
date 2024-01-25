## inference_realesrgan with changes:
chose folder
put output in subfolder"Upscale_" + os.path.basename(folder_path)

FileNotFoundError: [Errno 2] No such file or directory: 'experiments/pretrained_models/RealESRNet_x4plus.pth' 
It worked when I changed the path in  options/finetune_realesrgan_x4plus.yml
from:
pretrain_network_g: experiments/pretrained_models/RealESRNet_x4plus.pth
to:
pretrain_network_g: experiments/pretrained_models/RealESRGAN_x4plus.pth

https://github.com/xinntao/Real-ESRGAN/issues/407
https://github.com/onnx/onnxmltools

https://github.com/xinntao/Real-ESRGAN/issues/433
https://github.com/xinntao/Real-ESRGAN/issues/586

## detect if img is squere
15% tolerance

## watermark
add @Nivellem Studio watermark
