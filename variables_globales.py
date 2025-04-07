from cubo import *

COLORES = ["B", "V", "N", "R", "AZ", "AM"]
cube_state = {cara: [[cara for _ in range(3)] for _ in range(3)] for cara in COLORES}

instrucciones = {
    "b1": "Gira la cara blanca 1 vez.",
    
    "g1b2g3b2g3a1g1a3": (
        "1. Gira la cara roja 1 vez.\n"
        "2. Gira la cara blanca 2 veces.\n"
        "3. Gira la cara roja 3 veces.\n"
        "4. Gira la cara blanca 2 veces.\n"
        "5. Gira la cara roja 3 veces.\n"
        "6. Gira la cara azul 1 vez.\n"
        "7. Gira la cara roja 1 vez.\n"
        "8. Gira la cara azul 3 veces."
    ),
    
    "g3b2g1b2g1v3g3v1": (
        "1. Gira la cara roja 3 veces.\n"
        "2. Gira la cara blanca 2 veces.\n"
        "3. Gira la cara roja 1 vez.\n"
        "4. Gira la cara blanca 2 veces.\n"
        "5. Gira la cara roja 1 vez.\n"
        "6. Gira la cara verde 3 veces.\n"
        "7. Gira la cara roja 3 veces.\n"
        "8. Gira la cara verde 1 vez."
    ),
    
    "g1b1g3b3g3a1g1a3": (
        "1. Gira la cara roja 1 vez.\n"
        "2. Gira la cara blanca 1 vez.\n"
        "3. Gira la cara roja 3 veces.\n"
        "4. Gira la cara blanca 3 veces.\n"
        "5. Gira la cara roja 3 veces.\n"
        "6. Gira la cara azul 1 vez.\n"
        "7. Gira la cara roja 1 vez.\n"
        "8. Gira la cara azul 3 veces."
    ),
    
    "g3b3g1b1g1v3g3v1": (
        "1. Gira la cara roja 3 veces.\n"
        "2. Gira la cara blanca 3 veces.\n"
        "3. Gira la cara roja 1 vez.\n"
        "4. Gira la cara blanca 1 vez.\n"
        "5. Gira la cara roja 1 vez.\n"
        "6. Gira la cara verde 3 veces.\n"
        "7. Gira la cara roja 3 veces.\n"
        "8. Gira la cara verde 1 vez."
    ),
    
    "a1b2a3b2a3n1a1n3": (
        "1. Gira la cara azul 1 vez.\n"
        "2. Gira la cara blanca 2 veces.\n"
        "3. Gira la cara azul 3 veces.\n"
        "4. Gira la cara blanca 2 veces.\n"
        "5. Gira la cara azul 3 veces.\n"
        "6. Gira la cara naranja 1 vez.\n"
        "7. Gira la cara azul 1 vez.\n"
        "8. Gira la cara naranja 3 veces."
    ),
    
    "a3b2a1b2a1g3a3g1": (
        "1. Gira la cara azul 3 veces.\n"
        "2. Gira la cara blanca 2 veces.\n"
        "3. Gira la cara azul 1 vez.\n"
        "4. Gira la cara blanca 2 veces.\n"
        "5. Gira la cara azul 1 vez.\n"
        "6. Gira la cara roja 3 veces.\n"
        "7. Gira la cara azul 3 veces.\n"
        "8. Gira la cara roja 1 vez."
    ),
    
    "a1b1a3b3a3n1a1n3": (
        "1. Gira la cara azul 1 vez.\n"
        "2. Gira la cara blanca 1 vez.\n"
        "3. Gira la cara azul 3 veces.\n"
        "4. Gira la cara blanca 3 veces.\n"
        "5. Gira la cara azul 3 veces.\n"
        "6. Gira la cara naranja 1 vez.\n"
        "7. Gira la cara azul 1 vez.\n"
        "8. Gira la cara naranja 3 veces."
    ),
    
    "a3b3a1b1a1g3a3g1": (
        "1. Gira la cara azul 3 veces.\n"
        "2. Gira la cara blanca 3 veces.\n"
        "3. Gira la cara azul 1 vez.\n"
        "4. Gira la cara blanca 1 vez.\n"
        "5. Gira la cara azul 1 vez.\n"
        "6. Gira la cara roja 3 veces.\n"
        "7. Gira la cara azul 3 veces.\n"
        "8. Gira la cara roja 1 vez."
    ),
    
    "n1b2n3b2n3v1n1v3": (
        "1. Gira la cara naranja 1 vez.\n"
        "2. Gira la cara blanca 2 veces.\n"
        "3. Gira la cara naranja 3 veces.\n"
        "4. Gira la cara blanca 2 veces.\n"
        "5. Gira la cara naranja 3 veces.\n"
        "6. Gira la cara verde 1 vez.\n"
        "7. Gira la cara naranja 1 vez.\n"
        "8. Gira la cara verde 3 veces."
    ),
    
    "n3b2n1b2n1a3n3a1": (
        "1. Gira la cara naranja 3 veces.\n"
        "2. Gira la cara blanca 2 veces.\n"
        "3. Gira la cara naranja 1 vez.\n"
        "4. Gira la cara blanca 2 veces.\n"
        "5. Gira la cara naranja 1 vez.\n"
        "6. Gira la cara azul 3 veces.\n"
        "7. Gira la cara naranja 3 veces.\n"
        "8. Gira la cara azul 1 vez."
    ),
    
    "n1b1n3b3n3v1n1v3": (
        "1. Gira la cara naranja 1 vez.\n"
        "2. Gira la cara blanca 1 vez.\n"
        "3. Gira la cara naranja 3 veces.\n"
        "4. Gira la cara blanca 3 veces.\n"
        "5. Gira la cara naranja 3 veces.\n"
        "6. Gira la cara verde 1 vez.\n"
        "7. Gira la cara naranja 1 vez.\n"
        "8. Gira la cara verde 3 veces."
    ),
    
    "n3b3n1b1n1a3n3a1": (
        "1. Gira la cara naranja 3 veces.\n"
        "2. Gira la cara blanca 3 veces.\n"
        "3. Gira la cara naranja 1 vez.\n"
        "4. Gira la cara blanca 1 vez.\n"
        "5. Gira la cara naranja 1 vez.\n"
        "6. Gira la cara azul 3 veces.\n"
        "7. Gira la cara naranja 3 veces.\n"
        "8. Gira la cara azul 1 vez."
    ),
    
    "v1b2v3b2v3g1v1g3": (
        "1. Gira la cara verde 1 vez.\n"
        "2. Gira la cara blanca 2 veces.\n"
        "3. Gira la cara verde 3 veces.\n"
        "4. Gira la cara blanca 2 veces.\n"
        "5. Gira la cara verde 3 veces.\n"
        "6. Gira la cara roja 1 vez.\n"
        "7. Gira la cara verde 1 vez.\n"
        "8. Gira la cara roja 3 veces."
    ),
    
    "v3b2v1b2v1n3v3n1": (
        "1. Gira la cara verde 3 veces.\n"
        "2. Gira la cara blanca 2 veces.\n"
        "3. Gira la cara verde 1 vez.\n"
        "4. Gira la cara blanca 2 veces.\n"
        "5. Gira la cara verde 1 vez.\n"
        "6. Gira la cara naranja 3 veces.\n"
        "7. Gira la cara verde 3 veces.\n"
        "8. Gira la cara naranja 1 vez."
    ),
    
    "v1b1v3b3v3g1v1g3": (
        "1. Gira la cara verde 1 vez.\n"
        "2. Gira la cara blanca 1 vez.\n"
        "3. Gira la cara verde 3 veces.\n"
        "4. Gira la cara blanca 3 veces.\n"
        "5. Gira la cara verde 3 veces.\n"
        "6. Gira la cara roja 1 vez.\n"
        "7. Gira la cara verde 1 vez.\n"
        "8. Gira la cara roja 3 veces."
    ),
    
    "v3b3v1b1v1n3v3n1": (
        "1. Gira la cara verde 3 veces.\n"
        "2. Gira la cara blanca 3 veces.\n"
        "3. Gira la cara verde 1 vez.\n"
        "4. Gira la cara blanca 1 vez.\n"
        "5. Gira la cara verde 1 vez.\n"
        "6. Gira la cara naranja 3 veces.\n"
        "7. Gira la cara verde 3 veces.\n"
        "8. Gira la cara naranja 1 vez."
    ),
    
    "b3": "Gira la cara blanca 3 veces.",
    
    "a1g3a3g1b2g1b2g3": (
        "1. Gira la cara azul 1 vez.\n"
        "2. Gira la cara roja 3 veces.\n"
        "3. Gira la cara azul 3 veces.\n"
        "4. Gira la cara roja 1 vez.\n"
        "5. Gira la cara blanca 2 veces.\n"
        "6. Gira la cara roja 1 vez.\n"
        "7. Gira la cara blanca 2 veces.\n"
        "8. Gira la cara roja 3 veces."
    ),
    
    "v3g1v1g3b2g3b2g1": (
        "1. Gira la cara verde 3 veces.\n"
        "2. Gira la cara roja 1 vez.\n"
        "3. Gira la cara verde 1 vez.\n"
        "4. Gira la cara roja 3 veces.\n"
        "5. Gira la cara blanca 2 veces.\n"
        "6. Gira la cara roja 3 veces.\n"
        "7. Gira la cara blanca 2 veces.\n"
        "8. Gira la cara roja 1 vez."
    ),
    
    "a1g3a3g1b1g1b3g3": (
        "1. Gira la cara azul 1 vez.\n"
        "2. Gira la cara roja 3 veces.\n"
        "3. Gira la cara azul 3 veces.\n"
        "4. Gira la cara roja 1 vez.\n"
        "5. Gira la cara blanca 1 vez.\n"
        "6. Gira la cara roja 1 vez.\n"
        "7. Gira la cara blanca 3 veces.\n"
        "8. Gira la cara roja 3 veces."
    ),
    
    "v3g1v1g3b3g3b1g1": (
        "1. Gira la cara verde 3 veces.\n"
        "2. Gira la cara roja 1 vez.\n"
        "3. Gira la cara verde 1 vez.\n"
        "4. Gira la cara roja 3 veces.\n"
        "5. Gira la cara blanca 3 veces.\n"
        "6. Gira la cara roja 3 veces.\n"
        "7. Gira la cara blanca 1 vez.\n"
        "8. Gira la cara roja 1 vez."
    ),
    
    "n1a3n3a1b2a1b2a3": (
        "1. Gira la cara naranja 1 vez.\n"
        "2. Gira la cara azul 3 veces.\n"
        "3. Gira la cara naranja 3 veces.\n"
        "4. Gira la cara azul 1 vez.\n"
        "5. Gira la cara blanca 2 veces.\n"
        "6. Gira la cara azul 1 vez.\n"
        "7. Gira la cara blanca 2 veces.\n"
        "8. Gira la cara azul 3 veces."
    ),
    
    "g3a1g1a3b2a3b2a1": (
        "1. Gira la cara roja 3 veces.\n"
        "2. Gira la cara azul 1 vez.\n"
        "3. Gira la cara roja 1 vez.\n"
        "4. Gira la cara azul 3 veces.\n"
        "5. Gira la cara blanca 2 veces.\n"
        "6. Gira la cara azul 3 veces.\n"
        "7. Gira la cara blanca 2 veces.\n"
        "8. Gira la cara azul 1 vez."
    ),
    
    "n1a3n3a1b1a1b3a3": (
        "1. Gira la cara naranja 1 vez.\n"
        "2. Gira la cara azul 3 veces.\n"
        "3. Gira la cara naranja 3 veces.\n"
        "4. Gira la cara azul 1 vez.\n"
        "5. Gira la cara blanca 1 vez.\n"
        "6. Gira la cara azul 1 vez.\n"
        "7. Gira la cara blanca 3 veces.\n"
        "8. Gira la cara azul 3 veces."
    ),
    
    "g3a1g1a3b3a3b1a1": (
        "1. Gira la cara roja 3 veces.\n"
        "2. Gira la cara azul 1 vez.\n"
        "3. Gira la cara roja 1 vez.\n"
        "4. Gira la cara azul 3 veces.\n"
        "5. Gira la cara blanca 3 veces.\n"
        "6. Gira la cara azul 3 veces.\n"
        "7. Gira la cara blanca 1 vez.\n"
        "8. Gira la cara azul 1 vez."
    ),
    
    "v1n3v3n1b2n1b2n3": (
        "1. Gira la cara verde 1 vez.\n"
        "2. Gira la cara naranja 3 veces.\n"
        "3. Gira la cara verde 3 veces.\n"
        "4. Gira la cara naranja 1 vez.\n"
        "5. Gira la cara blanca 2 veces.\n"
        "6. Gira la cara naranja 1 vez.\n"
        "7. Gira la cara blanca 2 veces.\n"
        "8. Gira la cara naranja 3 veces."
    ),
    
    "a3n1a1n3b2n3b2n1": (
        "1. Gira la cara azul 3 veces.\n"
        "2. Gira la cara naranja 1 vez.\n"
        "3. Gira la cara azul 1 vez.\n"
        "4. Gira la cara naranja 3 veces.\n"
        "5. Gira la cara blanca 2 veces.\n"
        "6. Gira la cara naranja 3 veces.\n"
        "7. Gira la cara blanca 2 veces.\n"
        "8. Gira la cara naranja 1 vez."
    ),
    
    "v1n3v3n1b1n1b3n3": (
        "1. Gira la cara verde 1 vez.\n"
        "2. Gira la cara naranja 3 veces.\n"
        "3. Gira la cara verde 3 veces.\n"
        "4. Gira la cara naranja 1 vez.\n"
        "5. Gira la cara blanca 1 vez.\n"
        "6. Gira la cara naranja 1 vez.\n"
        "7. Gira la cara blanca 3 veces.\n"
        "8. Gira la cara naranja 3 veces."
    ),
    
    "a3n1a1n3b3n3b1n1": (
        "1. Gira la cara azul 3 veces.\n"
        "2. Gira la cara naranja 1 vez.\n"
        "3. Gira la cara azul 1 vez.\n"
        "4. Gira la cara naranja 3 veces.\n"
        "5. Gira la cara blanca 3 veces.\n"
        "6. Gira la cara naranja 3 veces.\n"
        "7. Gira la cara blanca 1 vez.\n"
        "8. Gira la cara naranja 1 vez."
    ),
    
    "g1v3g3v1b2v1b2v3": (
        "1. Gira la cara roja 1 vez.\n"
        "2. Gira la cara verde 3 veces.\n"
        "3. Gira la cara roja 3 veces.\n"
        "4. Gira la cara verde 1 vez.\n"
        "5. Gira la cara blanca 2 veces.\n"
        "6. Gira la cara verde 1 vez.\n"
        "7. Gira la cara blanca 2 veces.\n"
        "8. Gira la cara verde 3 veces."
    ),
    
    "n3v1n1v3b2v3b2v1": (
        "1. Gira la cara naranja 3 veces.\n"
        "2. Gira la cara verde 1 vez.\n"
        "3. Gira la cara naranja 1 vez.\n"
        "4. Gira la cara verde 3 veces.\n"
        "5. Gira la cara blanca 2 veces.\n"
        "6. Gira la cara verde 3 veces.\n"
        "7. Gira la cara blanca 2 veces.\n"
        "8. Gira la cara verde 1 vez."
    ),
    
    "g1v3g3v1b1v1b3v3": (
        "1. Gira la cara roja 1 vez.\n"
        "2. Gira la cara verde 3 veces.\n"
        "3. Gira la cara roja 3 veces.\n"
        "4. Gira la cara verde 1 vez.\n"
        "5. Gira la cara blanca 1 vez.\n"
        "6. Gira la cara verde 1 vez.\n"
        "7. Gira la cara blanca 3 veces.\n"
        "8. Gira la cara verde 3 veces."
    ),
    
    "n3v1n1v3b3v3b1v1": (
        "1. Gira la cara naranja 3 veces.\n"
        "2. Gira la cara verde 1 vez.\n"
        "3. Gira la cara naranja 1 vez.\n"
        "4. Gira la cara verde 3 veces.\n"
        "5. Gira la cara blanca 3 veces.\n"
        "6. Gira la cara verde 3 veces.\n"
        "7. Gira la cara blanca 1 vez.\n"
        "8. Gira la cara verde 1 vez."
    )
}
