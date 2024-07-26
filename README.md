修改`config.py`和`config_positions.py`中的相关配置进行适配

`config.py`中包含运行设置，邮箱相关的信息一定要设置

`config_positions.py`中包含点击位置设置

RKNN 相关固件信息
```
I RKNN: [08:37:06.542] RKNN Runtime Information, librknnrt version: 2.0.0b0 (35a6907d79@2024-03-24T10:31:14)
I RKNN: [08:37:06.542] RKNN Driver Information, version: 0.9.6
I RKNN: [08:37:06.542] RKNN Model Information, version: 6, toolkit version: 2.0.0b0+9bab5682(compiler version: 2.0.0b0 (35a6907d79@2024-03-24T02:34:11)), target: RKNPU v2, target platform: rk3588, framework name: ONNX, framework layout: NCHW, model inference type: static_shape
```

运行`run.py`进行每日活动

安卓容器镜像可使用：https://github.com/CNflysky/redroid-rk3588

保存图片需要手动创建文件夹：`screenShot`

# RKNN：

https://github.com/airockchip/rknn_model_zoo

https://github.com/airockchip/rknn-toolkit2
