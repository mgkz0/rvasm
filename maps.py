from types import IType

INSTRUCTIONS = {
    # RV32I — U/J
    "lui":   (IType.U, 0b0110111),
    "auipc": (IType.U, 0b0010111),
    "jal":   (IType.J, 0b1101111),
    # RV32I — I
    "jalr":  (IType.I, 0b000, 0b1100111),
    "lb":    (IType.I, 0b000, 0b0000011),
    "lh":    (IType.I, 0b001, 0b0000011),
    "lw":    (IType.I, 0b010, 0b0000011),
    "lbu":   (IType.I, 0b100, 0b0000011),
    "lhu":   (IType.I, 0b101, 0b0000011),
    "addi":  (IType.I, 0b000, 0b0010011),
    "slti":  (IType.I, 0b010, 0b0010011),
    "sltiu": (IType.I, 0b011, 0b0010011),
    "xori":  (IType.I, 0b100, 0b0010011),
    "ori":   (IType.I, 0b110, 0b0010011),
    "andi":  (IType.I, 0b111, 0b0010011),
    "slli":  (IType.I, 0b001, 0b0010011),
    "srli":  (IType.I, 0b101, 0b0010011),
    "srai":  (IType.I, 0b101, 0b0010011),
    # RV32I — S
    "sb":    (IType.S, 0b000, 0b0100011),
    "sh":    (IType.S, 0b001, 0b0100011),
    "sw":    (IType.S, 0b010, 0b0100011),
    # RV32I — B
    "beq":   (IType.B, 0b000, 0b1100011),
    "bne":   (IType.B, 0b001, 0b1100011),
    "blt":   (IType.B, 0b100, 0b1100011),
    "bge":   (IType.B, 0b101, 0b1100011),
    "bltu":  (IType.B, 0b110, 0b1100011),
    "bgeu":  (IType.B, 0b111, 0b1100011),
    # RV32I — R
    "add":   (IType.R, 0b0000000, 0b000, 0b0110011),
    "sub":   (IType.R, 0b0100000, 0b000, 0b0110011),
    "sll":   (IType.R, 0b0000000, 0b001, 0b0110011),
    "slt":   (IType.R, 0b0000000, 0b010, 0b0110011),
    "sltu":  (IType.R, 0b0000000, 0b011, 0b0110011),
    "xor":   (IType.R, 0b0000000, 0b100, 0b0110011),
    "srl":   (IType.R, 0b0000000, 0b101, 0b0110011),
    "sra":   (IType.R, 0b0100000, 0b101, 0b0110011),
    "or":    (IType.R, 0b0000000, 0b110, 0b0110011),
    "and":   (IType.R, 0b0000000, 0b111, 0b0110011),
    # System ebreak/ecall (immediate for it because it's constant)
    "ecall":  (IType.I, 0b000, 0b1110011, 0b000000000000),
    "ebreak": (IType.I, 0b000, 0b1110011, 0b000000000001),
    # Zicsr
    "csrrw":  (IType.I, 0b001, 0b1110011),
    "csrrs":  (IType.I, 0b010, 0b1110011),
    "csrrc":  (IType.I, 0b011, 0b1110011),
    "csrrwi": (IType.I, 0b101, 0b1110011),
    "csrrsi": (IType.I, 0b110, 0b1110011),
    "csrrci": (IType.I, 0b111, 0b1110011),
    # RV32M
    "mul":    (IType.R, 0b0000001, 0b000, 0b0110011),
    "mulh":   (IType.R, 0b0000001, 0b001, 0b0110011),
    "mulhsu": (IType.R, 0b0000001, 0b010, 0b0110011),
    "mulhu":  (IType.R, 0b0000001, 0b011, 0b0110011),
    "div":    (IType.R, 0b0000001, 0b100, 0b0110011),
    "divu":   (IType.R, 0b0000001, 0b101, 0b0110011),
    "rem":    (IType.R, 0b0000001, 0b110, 0b0110011),
    "remu":   (IType.R, 0b0000001, 0b111, 0b0110011),
    # Machine-mode return
    "mret":   (IType.R, 0b0111000, 0b000, 0b1110011),
}
