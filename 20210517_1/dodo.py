import glob
from doit.tools import create_folder

def task_test():
    """Preform tests."""
    return {'actions': ['python3 -m unittest']}


def task_pot():
    """Re-create .pot ."""
    return {
            'actions': ['pybabel extract -o solve.pot solve'],
            'file_dep': glob.glob('solve/*.py'),
            'targets': ['solve.pot'],
           }


def task_po():
    """Update translations."""
    return {
            'actions': ['pybabel update -D solve -d po -i solve.pot'],
            'file_dep': ['solve.pot'],
            'targets': ['po/ru/LC_MESSAGES/solve.po'],
           }


def task_mo():
    """Compile translations."""
    return {
            'actions': [
                (create_folder, ['solve/ru/LC_MESSAGES']),
                'pybabel compile -D solve -l ru -i po/ru/LC_MESSAGES/solve.po -d solve'
                       ],
            'file_dep': ['po/ru/LC_MESSAGES/solve.po'],
            'targets': ['solve/ru/LC_MESSAGES/solve.mo'],
           }


def task_wheel():
    """Create binary wheel distribution."""
    return {
            'actions': ['python -m build -w'],
            'task_dep': ['mo'],
           }

