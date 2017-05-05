Save/Load an H2O enviornment in Python
-------------------------------------------------------

See a discussion http://stackoverflow.com/questions/43791092/way-to-save-the-whole-environment-in-h2o 

See a jupiter demo https://github.com/mmagnus/h2o_utils/blob/master/h2o_utils_demo.ipynb 

    python h2o_utils.py
    H2OUtils: connect to H2O
    
    Checking whether there is an H2O instance running at http://localhost:54321. connected.
    --------------------------  ----------------------
    H2O cluster uptime:         56 mins 05 secs
    H2O cluster version:        3.10.4.5
    H2O cluster version age:    16 days
    H2O cluster name:           magnus
    H2O cluster total nodes:    1
    H2O cluster free memory:    1.476 Gb
    H2O cluster total cores:    4
    H2O cluster allowed cores:  4
    H2O cluster status:         locked, healthy
    H2O connection url:         http://localhost:54321
    H2O connection proxy:
    H2O internal security:      False
    Python version:             2.7.13 final
    --------------------------  ----------------------
    
    Models for rx: ^dp.+0: ['dp_grid_model_0']
    Models for rx: ^dp.+0: ['dp_grid_model_0']
    Save modeldp_grid_model_0 to /tmp//dp_grid_model_0
    H2O session _sid_bea5 closed.

Get models of a grid
------------------------------------------------------------

```
python test_grid.py
H2OUtils: connect to H2O

Checking whether there is an H2O instance running at http://localhost:54321. connected.
--------------------------  ----------------------
H2O cluster uptime:         1 hour 35 mins
H2O cluster version:        3.10.4.5
H2O cluster version age:    16 days
H2O cluster name:           magnus
H2O cluster total nodes:    1
H2O cluster free memory:    1.484 Gb
H2O cluster total cores:    4
H2O cluster allowed cores:  4
H2O cluster status:         locked, healthy
H2O connection url:         http://localhost:54321
H2O connection proxy:
H2O internal security:      False
Python version:             2.7.13 final
--------------------------  ----------------------

grid-ff50c4f6-c015-4e9c-a482-819efa061eb5
               activation                                          model_ids  \
0               Rectifier  grid-ff50c4f6-c015-4e9c-a482-819efa061eb5_model_0
1    RectifierWithDropout  grid-ff50c4f6-c015-4e9c-a482-819efa061eb5_model_1

    residual_deviance
0  0.2607234254884427
1  0.4224899744556164

Save modelgrid-ff50c4f6-c015-4e9c-a482-819efa061eb5_model_0 to /tmp//grid-ff50c4f6-c015-4e9c-a482-819efa061eb5_model_0
Save modelgrid-ff50c4f6-c015-4e9c-a482-819efa061eb5_model_1 to /tmp//grid-ff50c4f6-c015-4e9c-a482-819efa061eb5_model_1
H2O session _sid_967a closed.
```
