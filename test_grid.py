from h2o_utils import H2OUtils

h = H2OUtils(ip='localhost', port="54321")
h.save_models_of_grid("grid-ff50c4f6-c015-4e9c-a482-819efa061eb5", '/tmp/')
