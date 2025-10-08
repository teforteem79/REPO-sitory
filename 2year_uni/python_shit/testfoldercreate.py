from typing import Iterable, Tuple, List, Dict, Any
from pathlib import Path

def Folder_create_function(pairs: Iterable[Tuple[str, str]],
                           *,
                           dry_run: bool = False,
                           verbose: bool = True,
                           exist_ok: bool = True) -> List[Dict[str, Any]]:
    """
    Створює папки за списком пар (name, base_path).

    Параметри:
      pairs: ітерабель об'єктів типу (name, base_path)
      dry_run: якщо True — імітація, змін не робить
      verbose: якщо True — виводить інформацію в stdout
      exist_ok: якщо True — дозволяє створення, якщо папка вже існує

    Повертає:
      Список словників з ключами: name, path, ok, msg
    """
    result: List[Dict[str, Any]] = []

    for ind, item in enumerate(pairs):
        if not (isinstance(item, (tuple, list)) and len(item) == 2):
            result.append({
                'name': None,
                'path': None,
                'ok': False,
                'msg': f'Item {ind} is not a tuple/list of (name, base_path)'
            })
            if verbose:
                print(result[-1]['msg'])
            continue

        name, base = item

        if not isinstance(name, str) or not name.strip():
            result.append({
                'name': name,
                'path': base,
                'ok': False,
                'msg': f'Item {ind} has invalid name'
            })
            if verbose:
                print(result[-1]['msg'])
            continue

        if not isinstance(base, (str, Path)):
            result.append({
                'name': name,
                'path': base,
                'ok': False,
                'msg': f'Item {ind} has invalid base path'
            })
            if verbose:
                print(result[-1]['msg'])
            continue

        try:
            base_path = Path(base).expanduser()
            base_resolved = base_path.resolve()
            full_path = base_resolved / name
        except Exception as e:
            result.append({
                'name': name,
                'path': str(base),
                'ok': False,
                'msg': f'Path resolution error: {e}'
            })
            if verbose:
                print(result[-1]['msg'])
            continue

        if any(part in ('..', '') for part in Path(name).parts) or '\x00' in name:
            result.append({
                'name': name,
                'path': str(full_path),
                'ok': False,
                'msg': 'Path traversal detected'
            })
            if verbose:
                print(result[-1]['msg'])
            continue

        if dry_run:
            result.append({
                'name': name,
                'path': str(full_path),
                'ok': True,
                'msg': 'Dry run: directory not created'
            })
            if verbose:
                print(result[-1]['msg'])
            continue

        try:
            full_path.mkdir(parents=True, exist_ok=exist_ok)
            result.append({
                'name': name,
                'path': str(full_path),
                'ok': True,
                'msg': 'Directory created successfully'
            })
            if verbose:
                print(result[-1]['msg'])
        except Exception as e:
            result.append({
                'name': name,
                'path': str(full_path),
                'ok': False,
                'msg': f'Error creating directory: {e}'
            })
            if verbose:
                print(result[-1]['msg'])

    return result


test_pairs = [
    ("logs", "C:/Users/Dream/Desktop"),
    ("data", "C:/Users\Dream/Desktop"),
    ("../secret", "C:/Users/Dream/Desktop"),
]
results = Folder_create_function(test_pairs, dry_run=False, verbose=True)
for r in results:
    print(r)