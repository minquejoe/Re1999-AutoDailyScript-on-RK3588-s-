import subprocess
import cv2
import numpy as np
from rknnlite.api import RKNNLite
from scipy.special import softmax
import config
from utils import take_screenshot

RKNN_MODEL = config.RKNN_MODEL
IMG_PATH = config.IMG_PATH
CLASS_LABEL_PATH = config.CLASS_LABEL_PATH

def once_infer():
    take_screenshot()

    rknn_lite = RKNNLite()

    # Load RKNN model
    ret = rknn_lite.load_rknn(RKNN_MODEL)
    if ret != 0:
        print('Load RKNN model failed')
        exit(ret)

    # Init runtime environment
    ret = rknn_lite.init_runtime(core_mask=RKNNLite.NPU_CORE_AUTO)
    if ret != 0:
        print('Init runtime environment failed')
        exit(ret)

    # Set inputs
    img = cv2.imread(IMG_PATH)
    img = cv2.resize(img, (224, 224))
    img = np.expand_dims(img, 0)

    # Inference
    outputs = rknn_lite.inference(inputs=[img])

    rknn_lite.release()

    # Post Process
    with open(CLASS_LABEL_PATH, 'r') as f:
        labels = [l.rstrip() for l in f]

    scores = softmax(outputs[0])
    scores = np.squeeze(scores)
    idx_sorted = np.argsort(scores)[::-1]

    return scores, idx_sorted, labels

if __name__ == '__main__':
    scores, idx_sorted, labels = once_infer()
    for i in idx_sorted[0:5]:
        print('[%d] score=%.2f class="%s"' % (i, scores[i], labels[i]))
