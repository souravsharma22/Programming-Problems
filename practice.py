INSTRUCTION_SET = {
    "LDA": "00",
    "STA": "01",
    "ADD": "02",
    "SUB": "03",
    "JMP": "04",
    "NOP": "05",
}

# Assembler for pass one
def pass_one_assembler(assembly_code):
    symbol_table = {}  # To store labels with addresses
    location_counter = 0  # To track the current memory address
    intermediate_code = []  # To store intermediate code (labels and instructions)

    # First pass over the code
    for line in assembly_code:
        line = line.strip()
        if not line:  # Skip empty lines
            continue
        
        # Split into possible label and instruction
        parts = line.split()
        
        # Check if the line contains a label
        if line.endswith(':'):  # If it has a colon, it's a label
            label = parts[0].replace(':', '')
            symbol_table[label] = location_counter
            print(f"Label found: {label} at address {location_counter}")
        elif len(parts) > 1 and parts[1].endswith(':'):
            label = parts[1].replace(':', '')
            symbol_table[label] = location_counter
            print(f"Label found: {label} at address {location_counter}")
            parts.pop(1)  # Remove the label part to process instruction

        # Process the instruction part
        instruction = parts[0]
        if instruction in INSTRUCTION_SET:
            intermediate_code.append((location_counter, instruction, parts[1:]))  # Save instruction with operands
            location_counter += 1  # Increment the location counter by 1 (can vary based on instruction size)

    return symbol_table, intermediate_code

# Example assembly code
assembly_code = [
    "START: LDA 100",
    "STA 200",
    "ADD 300",
    "SUB 400",
    "LOOP: JMP START",
    "NOP",
]

# Run pass one assembler
symbol_table, intermediate_code = pass_one_assembler(assembly_code)

# Output symbol table and intermediate code
print("\nSymbol Table:")
for label, address in symbol_table.items():
    print(f"{label}: {address}")

print("\nIntermediate Code:")
for line in intermediate_code:
    print(f"Address {line[0]}: {line[1]} {line[2]}")
