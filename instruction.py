from enum import IntEnum


class IType(IntEnum): R, I, S, B, U, J, SYS, CSR = range(0, 8)

class Instruction:
  def __init__(self, itype: IType, data:int|str) -> None:
    self.itype = itype
    self.data = data if isinstance(data, int) else int(data)
  
  def __repr__(self) -> str: return f"IType({self.itype}), Data({self.data})"
  
  @classmethod
  def concat(cls, itype: IType, *vals) -> Instruction:
    result = 0
    for v, width in vals: result = (result << width) | v
    return cls(itype, result)


