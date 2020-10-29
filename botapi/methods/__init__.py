'''Methods Directory'''

def __list_all_methods():
    from os.path import dirname, basename, isfile
    import glob
    # This generates a list of modules in this folder for the * in __main__ to work.
    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    return [
        basename(f)[:-3] for f in mod_paths if isfile(f)
        and f.endswith(".py")
        and not f.endswith('__init__.py')
        ]


ALL_METHODS = sorted(__list_all_methods())
__all__ = ALL_METHODS + ["ALL_METHODS"]
