from enum import IntEnum
from dataclasses import dataclass

class IType(IntEnum): R, I, S, B, U, J, SYS, CSR = range(0, 8)

@dataclass(frozen=True)
class Instruction:
  itype: IType
  data: str


