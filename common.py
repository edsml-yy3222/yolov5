#!/usr/bin/env python
# coding: utf-8

# Model & training arguments are defined in this file
from pathlib import Path


class Config:
    def __init__(self, model, root, opath, oname):

        cwd = Path(".").absolute()
        if model == "Mars":
            self.weights = str(
                cwd / "janssen" / "Yolo_v5" / "weights" / "best.pt"
            )
        elif model == "Moon":
            self.weights = str(
                cwd / "janssen" / "Yolo_v5" / "weights" / "best.pt"
            )

        self.img_folder = root
        self.opath = opath
        self.custom_name = oname

        # Constant Configs
        self.imgsz = (416, 416)
        self.conf_thres = 0.1
