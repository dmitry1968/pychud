from numpy.distutils.core import Extension, setup
from numpy.distutils.system_info import get_info, NotFoundError


def setup_package(src_files, **kwargs):
    """ 
    Get source files and create a list of options for compilation.
    """
    fext = Extension(name="pychud",
                     sources=src_files,
                     extra_compile_args=["-O3"],
                     **kwargs)

    setup(name='pychud',
          version='0.1',
          description="Attempt to provide cholupdate in Python",
          author="Dmitry Mikhin",
          author_email="dmitry.mikhin@gmail.com",
          tests_require=['pytest'],
          ext_modules=[fext])

if __name__ == '__main__':
    sources = ['src/pychud.pyf', 'src/dchud.f', 'src/dchdd.f']

    config = {}
    try:
        extra_info = get_info('mkl', 2)
        config['extra_link_args'] = [f'-l{lib}' for lib in extra_info['libraries']]
    except NotFoundError:
        try:
            extra_info = get_info('blas', 2)
            config['extra_link_args'] = [f'-l{lib}' for lib in extra_info['libraries']]
        except NotFoundError:
            sources.extend(['src/ddot.f', 'src/dnrm2.f', 'src/drotg.f'])

    setup_package(sources, **config)
