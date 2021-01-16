#    _____           ______  _____ 
#  / ____/    /\    |  ____ |  __ \
# | |        /  \   | |__   | |__) | Caer - Modern Computer Vision
# | |       / /\ \  |  __|  |  _  /  Languages: Python, C, C++
# | |___   / ____ \ | |____ | | \ \  http://github.com/jasmcaus/caer
#  \_____\/_/    \_ \______ |_|  \_\

# Licensed under the MIT License <http://opensource.org/licenses/MIT>
# SPDX-License-Identifier: MIT
# Copyright (c) 2020 The Caer Authors <http://github.com/jasmcaus>


class _TensorBase:
    def __init__(self):
        self.max_width = 2
        self.is_floating_point = False 
        self.sci_mode = False 
        self.int_mode = True  
        self.numelem = self.size
        self._mode = 'rgb'
        self.mode = self._mode # '._mode' is used internally --> prevents misuse of the API

    def __repr__(self):
        return "<class 'caer.Tensor'>"
    
    def __str__(self):
        return self.__repr__()
    
    def height(self):
        return self.shape[0]
    
    def width(self):
        return self.shape[1]
    
    def channels(self):
        return self.shape[2]

    def cmode(self):
        return self._mode 
    
    def numel(self):
        return self.numelem
    
    def dim(self):
        return self.ndim

    def size_dim(self, dim):
        return self.shape[dim]

    def type(self):
        return self.dtype 

    # Color-mode stuff
    def is_rgb(self):
        return self._mode == 'rgb'
    
    def is_bgr(self):
        return self._mode == 'bgr'
    
    def is_gray(self):
        return self._mode == 'gray'
    
    def is_hsv(self):
        return self._mode == 'hsv'
    
    def is_lab(self):
        return self._mode == 'lab'
    
    def is_hls(self):
        return self._mode == 'hls'