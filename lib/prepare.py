# -*- coding: utf-8 -*-
# UFES - Universidade Federal do Espiríto Santo
# Gun Detection
# Written by Guilherme Cardoso


"""
Full documentation is at:
<TROCAR>.
"""


# __all__ = ['divide_dataset']
__author__ = ('Guilherme Vinícius Simões Cardoso <cardoso.guivi@gmail.com>')


# Importa o arquivo de configuração
import os
import sys
import numpy as np
import pandas as pd
from glob import glob

# Add config files
sys.path.insert(0, os.getcwd())
import cfg.config as cfg

_img = cfg.file_types['img']
_txt = cfg.file_types['txt']
_xml = cfg.file_types['xml']


def verbose(text):
    if __debug__:
        print(text)


class CreateDivisionList():
    def __init__(self):
        verbose('> Check folder tree...')
        self._check_tree()

        verbose('> Create file list...')
        lst_img_pistol = self._check_folder(cfg.path_db['pistol'])
        lst_img_others = self._check_folder(cfg.path_db['others'])

        verbose('> Divide lists (pandas - series)')
        _pistol_pd = pd.Series(lst_img_pistol)
        _others_pd = pd.Series(lst_img_others)
        self._tra_pistol, self._val_pistol = self._divide_pd(_pistol_pd)
        self._tra_others, self._val_others = self._divide_pd(_others_pd)

        verbose('> Training list and validation list completed!')
        verbose('> Train: {0:05d} files'.format(len(self.tra_pistol) + len(self.tra_others)))
        verbose('> Valid: {0:05d} files'.format(len(self.val_pistol) + len(self.val_others)))
        
    @property
    def tra_pistol(self): return self._tra_pistol

    @property
    def val_pistol(self): return self._val_pistol

    @property
    def tra_others(self): return self._tra_others

    @property
    def val_others(self): return self._val_others

    def _check_tree(self):
        def _make_dir(path): os.mkdir(path); verbose('> Make dir: ' + path)
        if not os.path.exists(cfg.paths['db']): _make_dir(cfg.paths['db'])
        if not os.path.exists(cfg.paths['valid']): _make_dir(cfg.paths['valid'])
        if not os.path.exists(cfg.paths['train']): _make_dir(cfg.paths['train'])
        if not os.path.exists(cfg.paths['test']): _make_dir(cfg.paths['test'])

    def _check_folder(self, path):
        lst = [arq for folder in glob(path + '/*') for arq in glob(folder + '/*' + _img)]
        if not lst:
            lst = [arq for arq in glob(path + '/*' + _img)]
            return lst
        else:
            return lst

    def _divide_pd(self, pd):
        sample = np.random.choice(
            a=pd.index,
            size=int(len(pd)*cfg.params['train']),
            replace=False)
        return pd.ix[sample], pd.drop(sample)


def divide_dataset():
    if __debug__: os.system('clear')

    obj = CreateDivisionList()