#!/usr/bin/env python
# coding: utf-8
# This is the API for using Yolo Model
import detect
from common import Config


def janssen_detect(model, root, opath, oname, options=None, imgParams=None):

    conf = Config(model, root, opath, oname)
    print(conf.weights)
    detect.run(
        weights=conf.weights,
        source=conf.img_folder,
        imgsz=conf.imgsz,
        conf_thres=conf.conf_thres,
        save_txt=True,
        project=conf.opath,
        name=conf.custom_name,
    )

    # If Options, add crater details to outputs
