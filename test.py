if __name__ == "__main__" and __package__ is None:
    from os.path import dirname as dir
    from sys import path

    path.append(dir(path[0]))

    # run pytest
    import pytest

    pytest.main(["tests/"])
