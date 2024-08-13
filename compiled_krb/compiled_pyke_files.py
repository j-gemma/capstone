# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'synth.krb'):
           [1723577687.1581578, 'synth_bc.py'],
         ('', '', 'synthesizer.kfb'):
           [1723577687.162094, 'synthesizer.fbc'],
        },
        compiler_version)
