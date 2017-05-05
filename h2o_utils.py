#!/usr/bin/env python
from __future__ import print_function

import h2o
import glob
import os
import re

class H2OUtils:
    def __init__(self, **args):
        print('H2OUtils: connect to H2O\n')
        h2o.init(**args)
        self.h2o = h2o
        print()
        
    def save_models_of_grid(self, grid_id, path):
        """Save models of a grid.

        :param grid_id: String containing a grid_id.
        :param path: String path, where to save your models.
        """
        g = self.h2o.get_grid(grid_id)
        for i, m in enumerate(g.models):
            h2o.save_model(model=m, path=path)
            
    def save_models(self, rx, path, overwrite=False):
        """Save models from H2O to path according to the regular expression.

        :param rx: String, python regular expression.
        :param path: String path, where to save your models.
        """
        models = self.list_models(rx)
        for i, m in enumerate(models):
            mh = self.h2o.get_model(m)
            print("Save model" + mh.model_id + " to " + path + "/" + mh.model_id)
            self.h2o.save_model(model=mh, path=path, force=overwrite)

    def load_models(self, path, verbose=True):
        """Load models to H2O from a directory
        :param path: String path, where to save your models.
        """
        models = glob.glob(path)
        for m in  models:
            if verbose: print('Load ', m)
            self.h2o.load_model(m)

    def list_models(self,rx, verbose=True):
        """List models of H2O."""
        models = []
        r = re.compile(rx)
        for m in self.h2o.ls()['key']:
            if r.search(m):
                models.append(m)
        if models and verbose:
            print('Models for rx: %s: %s' % (rx, models))
        return models
        
#main
if __name__ == '__main__':
    h = H2OUtils(ip='localhost', port="54321")
    h.list_models('^dp.+0')
    h.save_models(rx='^dp.+0', path='/tmp/', overwrite=True)