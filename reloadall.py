"""
reload_all.py: транзитивная перезагрузка вложенных модулей

Usage:
> from reloadall import reload_all
> import os, tkinter
> reload_all(os)
> reload_all(tkinter)
"""

import types
from importlib import reload


def status(mod):
    print('reloading ' + mod.__name__)


def transitive_reload(mod, visited):
    # Пропустить повторные посещения
    if mod not in visited:
        status(mod)
        # Перезагрузить модуль
        reload(mod)
        visited[mod] = None
        # И посетить дочерние модули
        for attr_obj in mod.__dict__.values():
            # Рекурсия если модуль
            if isinstance(attr_obj, types.ModuleType):
                transitive_reload(attr_obj, visited)


def reload_all(*modules_names):
    visited = {}
    for module_name in modules_names:
        transitive_reload(module_name, visited)


if __name__ == '__main__':
    # Тест: перезагрузить самого себя
    import reloadall
    reload_all(reloadall)
