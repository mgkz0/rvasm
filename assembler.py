from pathlib import Path
from maps import INSTR_VALUES, REGISTERS
from instruction import Instruction, IType


class Assembler:
  def __init__(self) -> None:
    self._labels: dict[str, int] = {}
    self.pc = 0

  def _tok_to_reg(self, t: str, allow_imm:bool) -> int:
    v = REGISTERS.get(t)
    if not v:
      if allow_imm: return int(t)
      raise ValueError(f"unknown reg: {t}")
    return v

  def _build_instruction(self, toks: tuple[str, ...]=(), vals: tuple[IType, ...]=()) -> Instruction:
    itype = vals[0]
    regs: list = []
    if not isinstance(itype, IType): raise ValueError("v[0] must have IType type")
    if itype is IType.R:
      assert len(toks) == 4, f"Invalid syntax: {toks}"
      for t in toks[1:]: regs.append(self._tok_to_reg(t, False))
      return Instruction.concat(IType.R, vals[1], regs[2], regs[1], vals[2], regs[0], vals[3])
    elif itype is IType.SYS and not toks: return Instruction(IType.SYS, vals[1])        

  def parse(self, line:str) -> Instruction|None:
    if line.startswith("#"): return None
    line = line.split("#")[0]
    toks = line.split(",")
    vals: tuple|None = INSTR_VALUES.get(toks[0])
    if len(toks) == 1:
      if toks[0].endswith(":"): 
        self._labels[toks[0][:-1]] = self.pc
        return None
      else:
        # return SYS type instructions here because they didn't need encoding
        if not vals: raise ValueError(f"Instruction {toks[0]} incorrect or didn't exists")
        return self._build_instruction(vals=vals)
    else:
      if not vals: raise ValueError(f"Instruction: {toks[0]} incorrect or didn't exists")
      if vals[0] is IType.SYS: raise ValueError(f"Invalid syntax on line {line}")


  def assembly(self, path: str|Path):
    with open(path, "r") as f:
      for l in f: 
        instr = self.parse(l)

  
