INSTRUCTION_SET = {
    "LDA": "00",
    "STA": "01",
    "ADD": "02",
    "SUB": "03",
    "JMP": "04",
    "NOP": "05",
}

# Two-Pass Assembler
def two_pass_assembler(assembly_code):
    symbol_table = {}  # To store labels with addresses
    location_counter = 0  # To track the current memory address

    # Pass One: Build the symbol table
    for line in assembly_code:
        line = line.strip()
        if not line:  # Skip empty lines
            continue
        
        parts = line.split()
        
        # Check for label at the beginning of the line
        if line.endswith(':'):
            label = parts[0][:-1]  # Remove the colon
            symbol_table[label] = location_counter
        elif len(parts) > 1 and parts[1].endswith(':'):
            label = parts[1][:-1]  # Remove the colon
            symbol_table[label] = location_counter
            parts.pop(1)  # Remove the label part to process instruction

        # Increment location counter for each instruction
        if parts[0] in INSTRUCTION_SET:
            location_counter += 1

    # Pass Two: Generate machine code
    machine_code = []
    location_counter = 0  # Reset location counter for the second pass

    for line in assembly_code:
        line = line.strip()
        if not line:  # Skip empty lines
            continue
        
        parts = line.split()
        
        # Skip label lines and process instructions
        if line.endswith(':') or (len(parts) > 1 and parts[1].endswith(':')):
            parts = parts[1:]  # Remove the label part if exists

        if parts and parts[0] in INSTRUCTION_SET:
            instruction = parts[0]
            operands = parts[1:] if len(parts) > 1 else []

            # Generate machine code
            opcode = INSTRUCTION_SET[instruction]
            operand_codes = [symbol_table[operand] if operand in symbol_table else operand for operand in operands]
            machine_code.append((location_counter, opcode, operand_codes))
            location_counter += 1  # Increment location counter

    return symbol_table, machine_code

# Example assembly code
assembly_code = [
    "START: LDA 100",
    "STA 200",
    "ADD 300",
    "SUB 400",
    "LOOP: JMP START",
    "NOP",
]

# Run the Two-Pass Assembler
symbol_table, machine_code = two_pass_assembler(assembly_code)

# Output symbol table
print("\nSymbol Table:")
for label, address in symbol_table.items():
    print(f"{label}: {address}")

# Output machine code
print("\nMachine Code:")
for line in machine_code:
    address, opcode, operands = line
    operand_str = ' '.join(map(str, operands))
    print(f"Address {address}: {opcode} {operand_str}")
