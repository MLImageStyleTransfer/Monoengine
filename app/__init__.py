from pathlib import Path

PATH_TO_APP: Path = Path(__file__).absolute().parent.resolve()

__all__ = ['PATH_TO_APP']
