from typing import Any, List, Tuple

class Genero:
    MALE = 0
    FEMALE = 1
    NONE = None

class TipoEquipamento:
    EPI=0
    EPC=1
    NONE=None

def get_choices(constant_clazz: Any) -> List[Tuple[str, Any]]:
    return [(value, value) for key, value in vars(constant_clazz).items() if not key.startswith('__')]