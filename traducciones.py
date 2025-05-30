TRADUCCIONES = {
    'es': {
        'welcome':         'Bienvenido al Cubo Rubik',
        'press_start':     'Cuando esté listo, presione Comenzar',
        'start':           'Comenzar',
        'language':        'Idioma',
        'about':           'Acerca De',
        'exit':            'Salir',
        'solve_cube':      'Resolver Cubo',
        'toggle_view':     'Alternar Vista 3D/plana',
        'reset_cube':      'Restablecer Cubo',
        'shuffle_cube':    'Aleatorizar Cubo',
        'coment':          "Cómo funciona la solución\n\n"
                            "- Órbita canónica: Si tu cubo ya pertenece a la órbita canónica, es decir, no tiene ninguna ficha mal colocada, buscamos directamente la secuencia de giros en el grafo.\n"
                            "- Otra órbita: Si detectamos una pieza desorientada, calculamos todas las orientaciones válidas, de las que hay 4 posibles en el grafo, te pedimos que indiques cuál está mal para utilizar la correcta y generamos la solución desde ese nodo.\n\n"
                            "El proceso en otra órbita tiene tres fases:\n"
                            "  1) Corrección inicial de la pieza desorientada. Ten esto en cuenta si te guías por la imágen de la derecha\n"
                            "  2) Giros canónicos para llevar la órbita a la solución.\n"
                            "  3) 'Descorrección' final para devolver la pieza a su órbita original.\n\n"
                            "Sigue los pasos en el panel de la derecha\n\n"
                            "Muchas gracias por usar el programa y espero que te haya sido útil.\n\n",
        'step':          'Paso',
        'next_step':       'Siguiente paso',
        'goto_menu':       'Volver al menú',
        'solution_complete': '¡Solución completada!',
        'cube_shuffled':   'Cubo mezclado',
        'already_solved':  'El cubo ya está solucionado. No se puede reiniciar',
        'cube_reset':      'Cubo reiniciado',
        'cube_solved':     'El cubo ya está solucionado.',
        'only_9':          'Solo pueden haber 9 casillas de cada color.',
        'not_found':       'Movimiento no encontrado en el grafo. Es posible que esté en otra órbita.',
        'question_orbit':  '¿Deseas continuar en otra órbita o corregir el cubo?',
        'continue_orbit':  'Continuar en otra órbita',
        'correct_cube':    'Corregir el cubo',
        'dontknow':        'No sé cuál flipeé',
        'arista_flipped':    'Arista flipeada',
        'choose_arista_flipped': 'Elige la arista que flipeaste',
        'random_solution': 'He seleccionado una solución aleatoria para la arista.',
        'esquina_flipped': 'Esquina flipeada',
        'choose_esquina_flipped': 'Elige la esquina que flipeaste',
        'random_solution_esquina': 'He seleccionado una solución aleatoria para la esquina.',
        'select_lenguage': 'Selecciona el idioma',
        'lenguage':        'Idioma',
        'lenguage_selected': 'Idioma seleccionado',
        'about_text':      "Acerca de Cubo Rubik"
                            "<b>Cubo Rubik App</b><br>Versión 1.0<br>Desarrollado por RanaCGames<br>"
                            "Este programa te permite resolver la última cara de un cubo Rubik de forma interactiva.<br>"
                            "Tiene en cuenta también las distintas órbitas del grupo de Rubik.<br>"
                            "Es un proyecto de TFG, Universidad Alfonso X, 2025<br>"
                            "Es posible que haya errores, pero no dudes en reportarlos.<br>"
                            "¡Gracias por usarlo!<br>",
        'b1': "Gira la cara blanca 1 vez.",
        'b3': "Gira la cara blanca 3 veces.",
        'g1b2g3b2g3a1g1a3': (
            "1. Gira la cara roja 1 vez.\n"
            "2. Gira la cara blanca 2 veces.\n"
            "3. Gira la cara roja 3 veces.\n"
            "4. Gira la cara blanca 2 veces.\n"
            "5. Gira la cara roja 3 veces.\n"
            "6. Gira la cara azul 1 vez.\n"
            "7. Gira la cara roja 1 vez.\n"
            "8. Gira la cara azul 3 veces."
        ),
        'g3b2g1b2g1v3g3v1': (
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

    },
    'en': {
        'welcome':         'Welcome to the Rubik Cube',
        'press_start':     'When you are ready, press Start',
        'start':           'Start',
        'language':        'Language',
        'about':           'About',
        'exit':            'Exit',
        'solve_cube':      'Solve Cube',
        'toggle_view':     'Toggle 3D/Net View',
        'reset_cube':      'Reset Cube',
        'shuffle_cube':    'Shuffle Cube',
        'coment':          "How the solution works\n\n"
                            "- Canonical orbit: If your cube already belongs to the canonical orbit—that is, it has no misoriented pieces—we directly search for the move sequence in the graph.\n"
                            "- Other orbit: If we detect a misoriented piece, we calculate all valid orientations (there are 4 possible in the graph), ask you to indicate which one is wrong so we can use the correct one, and generate the solution from that node.\n\n"
                            "The process in another orbit has three phases:\n"
                            "  1) Initial correction of the misoriented piece. Keep this in mind if you follow the image on the right.\n"
                            "  2) Canonical moves to bring the orbit to the solution.\n"
                            "  3) Final 'uncorrection' to return the piece to its original orbit.\n\n"
                            "Follow the steps in the right panel.\n\n"
                            "Thank you very much for using the program, and I hope you found it useful.\n\n",
        'step':          'Step',
        'next_step':       'Next Step',
        'goto_menu':       'Return to Menu',
        'solution_complete': 'Solution Complete!',
        'cube_shuffled':   'Cube Shuffled',
        'already_solved':  'The cube is already solved. Cannot restart',
        'cube_reset':      'Cube Reset',
        'cube_solved':     'The cube is already solved.',
        'only_9':          'There can only be 9 stickers of each color.',
        'not_found':       'Move not found in the graph. It may be in another orbit.',
        'question_orbit':  'Do you want to continue in another orbit or correct the cube?',
        'continue_orbit':  'Continue in Another Orbit',
        'correct_cube':    'Correct the Cube',
        'dontknow':        "I don’t know which one I flipped",  
        'arista_flipped':  'Edge flipped',
        'choose_arista_flipped': 'Choose the edge you flipped',
        'random_solution': 'I have selected a random solution for the edge.',
        'esquina_flipped': 'Corner flipped',
        'choose_esquina_flipped': 'Choose the corner you flipped',
        'random_solution_esquina': 'I have selected a random solution for the corner.',
        'select_lenguage': 'Select Language',
        'lenguage':        'Language',
        'lenguage_selected': 'Language Selected',
        'about_text':      "About the Rubik Cube" \
                            "<b>Rubik Cube App</b><br>Version 1.0<br>Developed by RanaCGames<br>" \
                            "This program allows you to solve the last face of a Rubik's Cube interactively.<br>" \
                            "It also accounts for the different orbits of the Rubik group.<br>" \
                            "A final-year project, Universidad Alfonso X, 2025<br>" \
                            "There may be errors, but please feel free to report them.<br>" \
                            "Thank you for using it!<br>",
        'b1': 'Rotate the white face once.',
        'g1b2g3b2g3a1g1a3': (
            '1. Rotate the red face once.\n'
            '2. Rotate the white face twice.\n'
            '3. Rotate the red face three times.\n'
            '4. Rotate the white face twice.\n'
            '5. Rotate the red face three times.\n'
            '6. Rotate the blue face once.\n'
            '7. Rotate the red face once.\n'
            '8. Rotate the blue face three times.'
        ),
        'g3b2g1b2g1v3g3v1': (
            '1. Rotate the red face three times.\n'
            '2. Rotate the white face twice.\n'
            '3. Rotate the red face once.\n'
            '4. Rotate the white face twice.\n'
            '5. Rotate the red face once.\n'
            '6. Rotate the green face three times.\n'
            '7. Rotate the red face three times.\n'
            '8. Rotate the green face once.'
        ),
        'g1b1g3b3g3a1g1a3': (
            '1. Rotate the red face once.\n'
            '2. Rotate the white face once.\n'
            '3. Rotate the red face three times.\n'
            '4. Rotate the white face three times.\n'
            '5. Rotate the red face three times.\n'
            '6. Rotate the blue face once.\n'
            '7. Rotate the red face once.\n'
            '8. Rotate the blue face three times.'
        ),
        'g3b3g1b1g1v3g3v1': (
            '1. Rotate the red face three times.\n'
            '2. Rotate the white face three times.\n'
            '3. Rotate the red face once.\n'
            '4. Rotate the white face once.\n'
            '5. Rotate the red face once.\n'
            '6. Rotate the green face three times.\n'
            '7. Rotate the red face three times.\n'
            '8. Rotate the green face once.'
        ),
        'a1b2a3b2a3n1a1n3': (
            '1. Rotate the blue face once.\n'
            '2. Rotate the white face twice.\n'
            '3. Rotate the blue face three times.\n'
            '4. Rotate the white face twice.\n'
            '5. Rotate the blue face three times.\n'
            '6. Rotate the orange face once.\n'
            '7. Rotate the blue face once.\n'
            '8. Rotate the orange face three times.'
        ),
        'a3b2a1b2a1g3a3g1': (
            '1. Rotate the blue face three times.\n'
            '2. Rotate the white face twice.\n'
            '3. Rotate the blue face once.\n'
            '4. Rotate the white face twice.\n'
            '5. Rotate the blue face once.\n'
            '6. Rotate the red face three times.\n'
            '7. Rotate the blue face three times.\n'
            '8. Rotate the red face once.'
        ),
        'a1b1a3b3a3n1a1n3': (
            '1. Rotate the blue face once.\n'
            '2. Rotate the white face once.\n'
            '3. Rotate the blue face three times.\n'
            '4. Rotate the white face three times.\n'
            '5. Rotate the blue face three times.\n'
            '6. Rotate the orange face once.\n'
            '7. Rotate the blue face once.\n'
            '8. Rotate the orange face three times.'
        ),
        'a3b3a1b1a1g3a3g1': (
            '1. Rotate the blue face three times.\n'
            '2. Rotate the white face three times.\n'
            '3. Rotate the blue face once.\n'
            '4. Rotate the white face once.\n'
            '5. Rotate the blue face once.\n'
            '6. Rotate the red face three times.\n'
            '7. Rotate the blue face three times.\n'
            '8. Rotate the red face once.'
        ),
        'n1b2n3b2n3v1n1v3': (
            '1. Rotate the orange face once.\n'
            '2. Rotate the white face twice.\n'
            '3. Rotate the orange face three times.\n'
            '4. Rotate the white face twice.\n'
            '5. Rotate the orange face three times.\n'
            '6. Rotate the green face once.\n'
            '7. Rotate the orange face once.\n'
            '8. Rotate the green face three times.'
        ),
        'n3b2n1b2n1a3n3a1': (
            '1. Rotate the orange face three times.\n'
            '2. Rotate the white face twice.\n'
            '3. Rotate the orange face once.\n'
            '4. Rotate the white face twice.\n'
            '5. Rotate the orange face once.\n'
            '6. Rotate the blue face three times.\n'
            '7. Rotate the orange face three times.\n'
            '8. Rotate the blue face once.'
        ),
        'n1b1n3b3n3v1n1v3': (
            '1. Rotate the orange face once.\n'
            '2. Rotate the white face once.\n'
            '3. Rotate the orange face three times.\n'
            '4. Rotate the white face three times.\n'
            '5. Rotate the orange face three times.\n'
            '6. Rotate the green face once.\n'
            '7. Rotate the orange face once.\n'
            '8. Rotate the green face three times.'
        ),
        'n3b3n1b1n1a3n3a1': (
            '1. Rotate the orange face three times.\n'
            '2. Rotate the white face three times.\n'
            '3. Rotate the orange face once.\n'
            '4. Rotate the white face once.\n'
            '5. Rotate the orange face once.\n'
            '6. Rotate the blue face three times.\n'
            '7. Rotate the orange face three times.\n'
            '8. Rotate the blue face once.'
        ),
        'v1b2v3b2v3g1v1g3': (
            '1. Rotate the green face once.\n'
            '2. Rotate the white face twice.\n'
            '3. Rotate the green face three times.\n'
            '4. Rotate the white face twice.\n'
            '5. Rotate the green face three times.\n'
            '6. Rotate the red face once.\n'
            '7. Rotate the green face once.\n'
            '8. Rotate the red face three times.'
        ),
        'v3b2v1b2v1n3v3n1': (
            '1. Rotate the green face three times.\n'
            '2. Rotate the white face twice.\n'
            '3. Rotate the green face once.\n'
            '4. Rotate the white face twice.\n'
            '5. Rotate the green face once.\n'
            '6. Rotate the orange face three times.\n'
            '7. Rotate the green face three times.\n'
            '8. Rotate the orange face once.'
        ),
        'v1b1v3b3v3g1v1g3': (
            '1. Rotate the green face once.\n'
            '2. Rotate the white face once.\n'
            '3. Rotate the red face three times.\n'
            '4. Rotate the white face three times.\n'
            '5. Rotate the red face three times.\n'
            '6. Rotate the blue face once.\n'
            '7. Rotate the red face once.\n'
            '8. Rotate the blue face three times.'
        ),
        'v3b3v1b1v1n3v3n1': (
            '1. Rotate the green face three times.\n'
            '2. Rotate the white face three times.\n'
            '3. Rotate the red face once.\n'
            '4. Rotate the white face once.\n'
            '5. Rotate the red face once.\n'
            '6. Rotate the orange face three times.\n'
            '7. Rotate the red face three times.\n'
            '8. Rotate the orange face once.'
        ),
        'b3': 'Rotate the white face three times.',
        'a1g3a3g1b2g1b2g3': (
            '1. Rotate the blue face once.\n'
            '2. Rotate the red face three times.\n'
            '3. Rotate the blue face three times.\n'
            '4. Rotate the red face once.\n'
            '5. Rotate the white face twice.\n'
            '6. Rotate the red face once.\n'
            '7. Rotate the white face twice.\n'
            '8. Rotate the red face three times.'
        ),
        'v3g1v1g3b2g3b2g1': (
            '1. Rotate the green face three times.\n'
            '2. Rotate the red face once.\n'
            '3. Rotate the green face once.\n'
            '4. Rotate the red face three times.\n'
            '5. Rotate the white face twice.\n'
            '6. Rotate the red face three times.\n'
            '7. Rotate the white face twice.\n'
            '8. Rotate the red face once.'
        ),
        'a1g3a3g1b1g1b3g3': (
            '1. Rotate the blue face once.\n'
            '2. Rotate the red face three times.\n'
            '3. Rotate the blue face three times.\n'
            '4. Rotate the red face once.\n'
            '5. Rotate the white face once.\n'
            '6. Rotate the red face once.\n'
            '7. Rotate the white face three times.\n'
            '8. Rotate the red face three times.'
        ),
        'v3g1v1g3b3g3b1g1': (
            '1. Rotate the green face three times.\n'
            '2. Rotate the red face once.\n'
            '3. Rotate the green face once.\n'
            '4. Rotate the red face three times.\n'
            '5. Rotate the white face three times.\n'
            '6. Rotate the red face three times.\n'
            '7. Rotate the white face once.\n'
            '8. Rotate the red face once.'
        ),
        'n1a3n3a1b2a1b2a3': (
            '1. Rotate the orange face once.\n'
            '2. Rotate the blue face three times.\n'
            '3. Rotate the orange face three times.\n'
            '4. Rotate the blue face once.\n'
            '5. Rotate the white face twice.\n'
            '6. Rotate the blue face once.\n'
            '7. Rotate the white face twice.\n'
            '8. Rotate the blue face three times.'
        ),
        'g3a1g1a3b2a3b2a1': (
            '1. Rotate the red face three times.\n'
            '2. Rotate the blue face once.\n'
            '3. Rotate the red face once.\n'
            '4. Rotate the blue face three times.\n'
            '5. Rotate the white face twice.\n'
            '6. Rotate the blue face three times.\n'
            '7. Rotate the white face twice.\n'
            '8. Rotate the blue face once.'
        ),
        'n1a3n3a1b1a1b3a3': (
            '1. Rotate the orange face once.\n'
            '2. Rotate the blue face three times.\n'
            '3. Rotate the orange face three times.\n'
            '4. Rotate the blue face once.\n'
            '5. Rotate the white face once.\n'
            '6. Rotate the blue face once.\n'
            '7. Rotate the white face three times.\n'
            '8. Rotate the blue face three times.'
        ),
        'g3a1g1a3b3a3b1a1': (
            '1. Rotate the red face three times.\n'
            '2. Rotate the blue face once.\n'
            '3. Rotate the red face once.\n'
            '4. Rotate the blue face three times.\n'
            '5. Rotate the white face three times.\n'
            '6. Rotate the blue face three times.\n'
            '7. Rotate the white face once.\n'
            '8. Rotate the blue face once.'
        ),
        'v1n3v3n1b2n1b2n3': (
            '1. Rotate the green face once.\n'
            '2. Rotate the orange face three times.\n'
            '3. Rotate the green face three times.\n'
            '4. Rotate the orange face once.\n'
            '5. Rotate the white face twice.\n'
            '6. Rotate the orange face once.\n'
            '7. Rotate the white face twice.\n'
            '8. Rotate the orange face three times.'
        ),
        'a3n1a1n3b2n3b2n1': (
            '1. Rotate the blue face three times.\n'
            '2. Rotate the orange face once.\n'
            '3. Rotate the blue face once.\n'
            '4. Rotate the orange face three times.\n'
            '5. Rotate the white face twice.\n'
            '6. Rotate the orange face three times.\n'
            '7. Rotate the white face twice.\n'
            '8. Rotate the orange face once.'
        ),
        'v1n3v3n1b1n1b3n3': (
            '1. Rotate the green face once.\n'
            '2. Rotate the orange face three times.\n'
            '3. Rotate the green face three times.\n'
            '4. Rotate the orange face once.\n'
            '5. Rotate the white face once.\n'
            '6. Rotate the orange face once.\n'
            '7. Rotate the white face three times.\n'
            '8. Rotate the orange face three times.'
        ),
        'a3n1a1n3b3n3b1n1': (
            '1. Rotate the blue face three times.\n'
            '2. Rotate the orange face once.\n'
            '3. Rotate the blue face once.\n'
            '4. Rotate the orange face three times.\n'
            '5. Rotate the white face three times.\n'
            '6. Rotate the orange face three times.\n'
            '7. Rotate the white face once.\n'
            '8. Rotate the orange face once.'
        ),
        'g1v3g3v1b2v1b2v3': (
            '1. Rotate the red face once.\n'
            '2. Rotate the green face three times.\n'
            '3. Rotate the red face three times.\n'
            '4. Rotate the green face once.\n'
            '5. Rotate the white face twice.\n'
            '6. Rotate the green face once.\n'
            '7. Rotate the white face twice.\n'
            '8. Rotate the green face three times.'
        ),
        'n3v1n1v3b2v3b2v1': (
            '1. Rotate the orange face three times.\n'
            '2. Rotate the green face once.\n'
            '3. Rotate the orange face once.\n'
            '4. Rotate the green face three times.\n'
            '5. Rotate the white face twice.\n'
            '6. Rotate the green face three times.\n'
            '7. Rotate the white face twice.\n'
            '8. Rotate the green face once.'
        ),
        'g1v3g3v1b1v1b3v3': (
            '1. Rotate the red face once.\n'
            '2. Rotate the green face three times.\n'
            '3. Rotate the red face three times.\n'
            '4. Rotate the green face once.\n'
            '5. Rotate the white face once.\n'
            '6. Rotate the green face once.\n'
            '7. Rotate the white face three times.\n'
            '8. Rotate the green face three times.'
        ),
        'n3v1n1v3b3v3b1v1': (
            '1. Rotate the orange face three times.\n'
            '2. Rotate the green face once.\n'
            '3. Rotate the orange face once.\n'
            '4. Rotate the green face three times.\n'
            '5. Rotate the white face three times.\n'
            '6. Rotate the green face three times.\n'
            '7. Rotate the white face once.\n'
            '8. Rotate the green face once.'
        ),
        
    },
    'it': {
        'welcome':         'Benvenuto al Cubo di Rubik',
        'press_start':     'Quando sei pronto, premi Avvia',
        'start':           'Avvia',
        'language':        'Lingua',
        'about':           'Informazioni',
        'exit':            'Esci',
        'solve_cube':      'Risolvi Cubo',
        'toggle_view':     'Alterna Vista 3D/Rete',
        'reset_cube':      'Reimposta Cubo',
        'shuffle_cube':    'Mescola Cubo',
        'coment':          "Come funziona la soluzione\n\n"
                            "- Orbita canonica: se il tuo cubo appartiene già all'orbita canonica, cioè non ha pezzi disorientati, cerchiamo direttamente la sequenza di mosse nel grafo.\n"
                            "- Altra orbita: se rileviamo un pezzo disorientato, calcoliamo tutte le orientazioni valide (ce ne sono 4 possibili nel grafo), ti chiediamo quale è sbagliata per usare quella corretta e generiamo la soluzione da quel nodo.\n\n"
                            "Il processo in un'altra orbita ha tre fasi:\n"
                            "  1) Correzione iniziale del pezzo disorientato. Tienilo a mente se segui l'immagine a destra.\n"
                            "  2) Mosse canoniche per portare l'orbita alla soluzione.\n"
                            "  3) 'Scorrezione' finale per riportare il pezzo alla sua orbita originale.\n\n"
                            "Segui i passaggi nel pannello di destra.\n\n"
                            "Grazie mille per aver usato il programma e spero ti sia stato utile.\n\n",
        'step':          'Passo',
        'next_step':       'Passo successivo',
        'goto_menu':       'Torna al menu',
        'solution_complete': 'Soluzione completata!',
        'cube_shuffled':   'Cubo mescolato',
        'already_solved':  'Il cubo è già risolto. Impossibile reinizializzarlo',
        'cube_reset':      'Cubo reimpostato',
        'cube_solved':     'Il cubo è già risolto.',
        'only_9':          'Ci possono essere solo 9 tessere di ogni colore.',
        'not_found':       "Mossa non trovata nel grafo. Potrebbe essere in un'altra orbita.",
        'question_orbit':  "Vuoi continuare in un'altra orbita o correggere il cubo?",
        'continue_orbit':  "Continua in un'altra orbita",
        'correct_cube':    'Correggi il cubo',
        'dontknow':        'Non so quale ho invertito',
        'arista_flipped':  'Arista invertita',
        'choose_arista_flipped': 'Scegli l’arista invertita',
        'random_solution': 'Ho selezionato una soluzione casuale per l’arista.',
        'esquina_flipped': 'Angolo invertito',
        'choose_esquina_flipped': 'Scegli l’angolo invertito',
        'random_solution_esquina': 'Ho selezionato una soluzione casuale per l’angolo.',
        'select_lenguage': 'Seleziona la lingua',
        'lenguage':        'Lingua',
        'lenguage_selected': 'Lingua selezionata',
        'about_text':      "Informazioni sul Cubo di Rubik" \
                            "<b>App Cubo di Rubik</b><br>Versione 1.0<br>Sviluppato da RanaCGames<br>" \
                            "Questo programma ti permette di risolvere l'ultima faccia di un Cubo di Rubik in modo interattivo.<br>" \
                            "Tiene conto anche delle diverse orbite del gruppo di Rubik.<br>" \
                            "Progetto di TFG, Universidad Alfonso X, 2025<br>" \
                            "Potrebbero esserci errori, ma non esitare a segnalarli.<br>" \
                            "Grazie per averlo usato!<br>",
        'b1': 'Ruota la faccia bianca una volta.',
        
        'g1b2g3b2g3a1g1a3': (
            '1. Ruota la faccia rossa una volta.\n'
            '2. Ruota la faccia bianca due volte.\n'
            '3. Ruota la faccia rossa tre volte.\n'
            '4. Ruota la faccia bianca due volte.\n'
            '5. Ruota la faccia rossa tre volte.\n'
            '6. Ruota la faccia blu una volta.\n'
            '7. Ruota la faccia rossa una volta.\n'
            '8. Ruota la faccia blu tre volte.'
        ),
        
        'g3b2g1b2g1v3g3v1': (
            '1. Ruota la faccia rossa tre volte.\n'
            '2. Ruota la faccia bianca due volte.\n'
            '3. Ruota la faccia rossa una volta.\n'
            '4. Ruota la faccia bianca due volte.\n'
            '5. Ruota la faccia rossa una volta.\n'
            '6. Ruota la faccia verde tre volte.\n'
            '7. Ruota la faccia rossa tre volte.\n'
            '8. Ruota la faccia verde una volta.'
        ),
        
        'g1b1g3b3g3a1g1a3': (
            '1. Ruota la faccia rossa una volta.\n'
            '2. Ruota la faccia bianca una volta.\n'
            '3. Ruota la faccia rossa tre volte.\n'
            '4. Ruota la faccia bianca tre volte.\n'
            '5. Ruota la faccia rossa tre volte.\n'
            '6. Ruota la faccia blu una volta.\n'
            '7. Ruota la faccia rossa una volta.\n'
            '8. Ruota la faccia blu tre volte.'
        ),
        
        'g3b3g1b1g1v3g3v1': (
            '1. Ruota la faccia rossa tre volte.\n'
            '2. Ruota la faccia bianca tre volte.\n'
            '3. Ruota la faccia rossa una volta.\n'
            '4. Ruota la faccia bianca una volta.\n'
            '5. Ruota la faccia rossa una volta.\n'
            '6. Ruota la faccia verde tre volte.\n'
            '7. Ruota la faccia rossa tre volte.\n'
            '8. Ruota la faccia verde una volta.'
        ),
        
        'a1b2a3b2a3n1a1n3': (
            '1. Ruota la faccia blu una volta.\n'
            '2. Ruota la faccia bianca due volte.\n'
            '3. Ruota la faccia blu tre volte.\n'
            '4. Ruota la faccia bianca due volte.\n'
            '5. Ruota la faccia blu tre volte.\n'
            '6. Ruota la faccia arancione una volta.\n'
            '7. Ruota la faccia blu una volta.\n'
            '8. Ruota la faccia arancione tre volte.'
        ),
        
        'a3b2a1b2a1g3a3g1': (
            '1. Ruota la faccia blu tre volte.\n'
            '2. Ruota la faccia bianca due volte.\n'
            '3. Ruota la faccia blu una volta.\n'
            '4. Ruota la faccia bianca due volte.\n'
            '5. Ruota la faccia blu una volta.\n'
            '6. Ruota la faccia rossa tre volte.\n'
            '7. Ruota la faccia blu tre volte.\n'
            '8. Ruota la faccia rossa una volta.'
        ),
        
        'a1b1a3b3a3n1a1n3': (
            '1. Ruota la faccia blu una volta.\n'
            '2. Ruota la faccia bianca una volta.\n'
            '3. Ruota la faccia blu tre volte.\n'
            '4. Ruota la faccia bianca tre volte.\n'
            '5. Ruota la faccia blu tre volte.\n'
            '6. Ruota la faccia arancione una volta.\n'
            '7. Ruota la faccia blu una volta.\n'
            '8. Ruota la faccia arancione tre volte.'
        ),
        
        'a3b3a1b1a1g3a3g1': (
            '1. Ruota la faccia blu tre volte.\n'
            '2. Ruota la faccia bianca tre volte.\n'
            '3. Ruota la faccia blu una volta.\n'
            '4. Ruota la faccia bianca una volta.\n'
            '5. Ruota la faccia blu una volta.\n'
            '6. Ruota la faccia rossa tre volte.\n'
            '7. Ruota la faccia blu tre volte.\n'
            '8. Ruota la faccia rossa una volta.'
        ),
        
        'n1b2n3b2n3v1n1v3': (
            '1. Ruota la faccia arancione una volta.\n'
            '2. Ruota la faccia bianca due volte.\n'
            '3. Ruota la faccia arancione tre volte.\n'
            '4. Ruota la faccia bianca due volte.\n'
            '5. Ruota la faccia arancione tre volte.\n'
            '6. Ruota la faccia verde una volta.\n'
            '7. Ruota la faccia arancione una volta.\n'
            '8. Ruota la faccia verde tre volte.'
        ),
        
        'n3b2n1b2n1a3n3a1': (
            '1. Ruota la faccia arancione tre volte.\n'
            '2. Ruota la faccia bianca due volte.\n'
            '3. Ruota la faccia arancione una volta.\n'
            '4. Ruota la faccia bianca due volte.\n'
            '5. Ruota la faccia arancione una volta.\n'
            '6. Ruota la faccia blu tre volte.\n'
            '7. Ruota la faccia arancione tre volte.\n'
            '8. Ruota la faccia blu una volta.'
        ),
        'n1b1n3b3n3v1n1v3': (
            '1. Ruota la faccia arancione una volta.\n'
            '2. Ruota la faccia bianca una volta.\n'
            '3. Ruota la faccia arancione tre volte.\n'
            '4. Ruota la faccia bianca tre volte.\n'
            '5. Ruota la faccia arancione tre volte.\n'
            '6. Ruota la faccia verde una volta.\n'
            '7. Ruota la faccia arancione una volta.\n'
            '8. Ruota la faccia verde tre volte.'
        ),
        'n3b3n1b1n1a3n3a1': (
            '1. Ruota la faccia arancione tre volte.\n'
            '2. Ruota la faccia bianca tre volte.\n'
            '3. Ruota la faccia arancione una volta.\n'
            '4. Ruota la faccia bianca una volta.\n'
            '5. Ruota la faccia arancione una volta.\n'
            '6. Ruota la faccia blu tre volte.\n'
            '7. Ruota la faccia arancione tre volte.\n'
            '8. Ruota la faccia blu una volta.'
        ),
        'v1b2v3b2v3g1v1g3': (
            '1. Ruota la faccia verde una volta.\n'
            '2. Ruota la faccia bianca due volte.\n'
            '3. Ruota la faccia verde tre volte.\n'
            '4. Ruota la faccia bianca due volte.\n'
            '5. Ruota la faccia verde tre volte.\n'
            '6. Ruota la faccia rossa una volta.\n'
            '7. Ruota la faccia verde una volta.\n'
            '8. Ruota la faccia rossa tre volte.'
        ),
        'v3b2v1b2v1n3v3n1': (
            '1. Ruota la faccia verde tre volte.\n'
            '2. Ruota la faccia bianca due volte.\n'
            '3. Ruota la faccia verde una volta.\n'
            '4. Ruota la faccia bianca due volte.\n'
            '5. Ruota la faccia verde una volta.\n'
            '6. Ruota la faccia arancione tre volte.\n'
            '7. Ruota la faccia verde tre volte.\n'
            '8. Ruota la faccia arancione una volta.'
        ),
        'v1b1v3b3v3g1v1g3': (
            '1. Ruota la faccia verde una volta.\n'
            '2. Ruota la faccia bianca una volta.\n'
            '3. Ruota la faccia rossa tre volte.\n'
            '4. Ruota la faccia bianca tre volte.\n'
            '5. Ruota la faccia rossa tre volte.\n'
            '6. Ruota la faccia blu una volta.\n'
            '7. Ruota la faccia rossa una volta.\n'
            '8. Ruota la faccia blu tre volte.'
        ),
        'v3b3v1b1v1n3v3n1': (
            '1. Ruota la faccia verde tre volte.\n'
            '2. Ruota la faccia bianca tre volte.\n'
            '3. Ruota la faccia rossa una volta.\n'
            '4. Ruota la faccia bianca una volta.\n'
            '5. Ruota la faccia rossa una volta.\n'
            '6. Ruota la faccia arancione tre volte.\n'
            '7. Ruota la faccia rossa tre volte.\n'
            '8. Ruota la faccia arancione una volta.'
        ),
        'b3': 'Ruota la faccia bianca tre volte.',

        'g1b2g3b2g3a1g1a3': (
            '1. Ruota la faccia rossa una volta.\n'
            '2. Ruota la faccia bianca due volte.\n'
            '3. Ruota la faccia rossa tre volte.\n'
            '4. Ruota la faccia bianca due volte.\n'
            '5. Ruota la faccia rossa tre volte.\n'
            '6. Ruota la faccia blu una volta.\n'
            '7. Ruota la faccia rossa una volta.\n'
            '8. Ruota la faccia blu tre volte.'
        ),

        'g3b2g1b2g1v3g3v1': (
            '1. Ruota la faccia rossa tre volte.\n'
            '2. Ruota la faccia bianca due volte.\n'
            '3. Ruota la faccia rossa una volta.\n'
            '4. Ruota la faccia bianca due volte.\n'
            '5. Ruota la faccia rossa una volta.\n'
            '6. Ruota la faccia verde tre volte.\n'
            '7. Ruota la faccia rossa tre volte.\n'
            '8. Ruota la faccia verde una volta.'
        ),

        'g1b1g3b3g3a1g1a3': (
            '1. Ruota la faccia rossa una volta.\n'
            '2. Ruota la faccia bianca una volta.\n'
            '3. Ruota la faccia rossa tre volte.\n'
            '4. Ruota la faccia bianca tre volte.\n'
            '5. Ruota la faccia rossa tre volte.\n'
            '6. Ruota la faccia blu una volta.\n'
            '7. Ruota la faccia rossa una volta.\n'
            '8. Ruota la faccia blu tre volte.'
        ),

        'g3b3g1b1g1v3g3v1': (
            '1. Ruota la faccia rossa tre volte.\n'
            '2. Ruota la faccia bianca tre volte.\n'
            '3. Ruota la faccia rossa una volta.\n'
            '4. Ruota la faccia bianca una volta.\n'
            '5. Ruota la faccia rossa una volta.\n'
            '6. Ruota la faccia verde tre volte.\n'
            '7. Ruota la faccia rossa tre volte.\n'
            '8. Ruota la faccia verde una volta.'
        ),

        'a1b2a3b2a3n1a1n3': (
            '1. Ruota la faccia blu una volta.\n'
            '2. Ruota la faccia bianca due volte.\n'
            '3. Ruota la faccia blu tre volte.\n'
            '4. Ruota la faccia bianca due volte.\n'
            '5. Ruota la faccia blu tre volte.\n'
            '6. Ruota la faccia arancione una volta.\n'
            '7. Ruota la faccia blu una volta.\n'
            '8. Ruota la faccia arancione tre volte.'
        ),

        'a3b2a1b2a1g3a3g1': (
            '1. Ruota la faccia blu tre volte.\n'
            '2. Ruota la faccia bianca due volte.\n'
            '3. Ruota la faccia blu una volta.\n'
            '4. Ruota la faccia bianca due volte.\n'
            '5. Ruota la faccia blu una volta.\n'
            '6. Ruota la faccia rossa tre volte.\n'
            '7. Ruota la faccia blu tre volte.\n'
            '8. Ruota la faccia rossa una volta.'
        ),

        'a1b1a3b3a3n1a1n3': (
            '1. Ruota la faccia blu una volta.\n'
            '2. Ruota la faccia bianca una volta.\n'
            '3. Ruota la faccia blu tre volte.\n'
            '4. Ruota la faccia bianca tre volte.\n'
            '5. Ruota la faccia blu tre volte.\n'
            '6. Ruota la faccia arancione una volta.\n'
            '7. Ruota la faccia blu una volta.\n'
            '8. Ruota la faccia arancione tre volte.'
        ),

        'a3b3a1b1a1g3a3g1': (
            '1. Ruota la faccia blu tre volte.\n'
            '2. Ruota la faccia bianca tre volte.\n'
            '3. Ruota la faccia blu una volta.\n'
            '4. Ruota la faccia bianca una volta.\n'
            '5. Ruota la faccia blu una volta.\n'
            '6. Ruota la faccia rossa tre volte.\n'
            '7. Ruota la faccia blu tre volte.\n'
            '8. Ruota la faccia rossa una volta.'
        ),

        'n1b2n3b2n3v1n1v3': (
            '1. Ruota la faccia arancione una volta.\n'
            '2. Ruota la faccia bianca due volte.\n'
            '3. Ruota la faccia arancione tre volte.\n'
            '4. Ruota la faccia bianca due volte.\n'
            '5. Ruota la faccia arancione tre volte.\n'
            '6. Ruota la faccia verde una volta.\n'
            '7. Ruota la faccia arancione una volta.\n'
            '8. Ruota la faccia verde tre volte.'
        ),

        'n1b1n3b3n3v1n1v3': (
            '1. Ruota la faccia arancione una volta.\n'
            '2. Ruota la faccia bianca una volta.\n'
            '3. Ruota la faccia arancione tre volte.\n'
            '4. Ruota la faccia bianca tre volte.\n'
            '5. Ruota la faccia arancione tre volte.\n'
            '6. Ruota la faccia verde una volta.\n'
            '7. Ruota la faccia arancione una volta.\n'
            '8. Ruota la faccia verde tre volte.'
        ),

        'n3b3n1b1n1a3n3a1': (
            '1. Ruota la faccia arancione tre volte.\n'
            '2. Ruota la faccia bianca tre volte.\n'
            '3. Ruota la faccia arancione una volta.\n'
            '4. Ruota la faccia bianca una volta.\n'
            '5. Ruota la faccia arancione una volta.\n'
            '6. Ruota la faccia blu tre volte.\n'
            '7. Ruota la faccia arancione tre volte.\n'
            '8. Ruota la faccia blu una volta.'
        ),

        'v1b2v3b2v3g1v1g3': (
            '1. Ruota la faccia verde una volta.\n'
            '2. Ruota la faccia bianca due volte.\n'
            '3. Ruota la faccia verde tre volte.\n'
            '4. Ruota la faccia bianca due volte.\n'
            '5. Ruota la faccia verde tre volte.\n'
            '6. Ruota la faccia rossa una volta.\n'
            '7. Ruota la faccia verde una volta.\n'
            '8. Ruota la faccia rossa tre volte.'
        ),

        'v3b2v1b2v1n3v3n1': (
            '1. Ruota la faccia verde tre volte.\n'
            '2. Ruota la faccia bianca due volte.\n'
            '3. Ruota la faccia verde una volta.\n'
            '4. Ruota la faccia bianca due volte.\n'
            '5. Ruota la faccia verde una volta.\n'
            '6. Ruota la faccia arancione tre volte.\n'
            '7. Ruota la faccia verde tre volte.\n'
            '8. Ruota la faccia arancione una volta.'
        ),

        'v1b1v3b3v3g1v1g3': (
            '1. Ruota la faccia verde una volta.\n'
            '2. Ruota la faccia bianca una volta.\n'
            '3. Ruota la faccia verde tre volte.\n'
            '4. Ruota la faccia bianca tre volte.\n'
            '5. Ruota la faccia verde tre volte.\n'
            '6. Ruota la faccia rossa una volta.\n'
            '7. Ruota la faccia verde una volta.\n'
            '8. Ruota la faccia rossa tre volte.'
        ),

        'v3b3v1b1v1n3v3n1': (
            '1. Ruota la faccia verde tre volte.\n'
            '2. Ruota la faccia bianca tre volte.\n'
            '3. Ruota la faccia verde una volta.\n'
            '4. Ruota la faccia bianca una volta.\n'
            '5. Ruota la faccia verde una volta.\n'
            '6. Ruota la faccia arancione tre volte.\n'
            '7. Ruota la faccia verde tre volte.\n'
            '8. Ruota la faccia arancione una volta.'
        ),

        'a1g3a3g1b2g1b2g3': (
            '1. Ruota la faccia blu una volta.\n'
            '2. Ruota la faccia rossa tre volte.\n'
            '3. Ruota la faccia blu tre volte.\n'
            '4. Ruota la faccia rossa una volta.\n'
            '5. Ruota la faccia bianca due volte.\n'
            '6. Ruota la faccia rossa una volta.\n'
            '7. Ruota la faccia bianca due volte.\n'
            '8. Ruota la faccia rossa tre volte.'
        ),

        'v3g1v1g3b2g3b2g1': (
            '1. Ruota la faccia verde tre volte.\n'
            '2. Ruota la faccia rossa una volta.\n'
            '3. Ruota la faccia verde una volta.\n'
            '4. Ruota la faccia rossa tre volte.\n'
            '5. Ruota la faccia bianca due volte.\n'
            '6. Ruota la faccia rossa tre volte.\n'
            '7. Ruota la faccia bianca due volte.\n'
            '8. Ruota la faccia rossa una volta.'
        ),

        'a1g3a3g1b1g1b3g3': (
            '1. Ruota la faccia blu una volta.\n'
            '2. Ruota la faccia rossa tre volte.\n'
            '3. Ruota la faccia blu tre volte.\n'
            '4. Ruota la faccia rossa una volta.\n'
            '5. Ruota la faccia bianca una volta.\n'
            '6. Ruota la faccia rossa una volta.\n'
            '7. Ruota la faccia bianca tre volte.\n'
            '8. Ruota la faccia rossa tre volte.'
        ),

        'v3g1v1g3b3g3b1g1': (
            '1. Ruota la faccia verde tre volte.\n'
            '2. Ruota la faccia rossa una volta.\n'
            '3. Ruota la faccia verde una volta.\n'
            '4. Ruota la faccia rossa tre volte.\n'
            '5. Ruota la faccia bianca tre volte.\n'
            '6. Ruota la faccia rossa tre volte.\n'
            '7. Ruota la faccia bianca una volta.\n'
            '8. Ruota la faccia rossa una volta.'
        ),

        'n1a3n3a1b2a1b2a3': (
            '1. Ruota la faccia arancione una volta.\n'
            '2. Ruota la faccia blu tre volte.\n'
            '3. Ruota la faccia arancione tre volte.\n'
            '4. Ruota la faccia blu una volta.\n'
            '5. Ruota la faccia bianca due volte.\n'
            '6. Ruota la faccia blu una volta.\n'
            '7. Ruota la faccia bianca due volte.\n'
            '8. Ruota la faccia blu tre volte.'
        ),

        'g3a1g1a3b2a3b2a1': (
            '1. Ruota la faccia rossa tre volte.\n'
            '2. Ruota la faccia blu una volta.\n'
            '3. Ruota la faccia rossa una volta.\n'
            '4. Ruota la faccia blu tre volte.\n'
            '5. Ruota la faccia bianca due volte.\n'
            '6. Ruota la faccia blu tre volte.\n'
            '7. Ruota la faccia bianca due volte.\n'
            '8. Ruota la faccia blu una volta.'
        ),

        'n1a3n3a1b1a1b3a3': (
            '1. Ruota la faccia arancione una volta.\n'
            '2. Ruota la faccia blu tre volte.\n'
            '3. Ruota la faccia arancione tre volte.\n'
            '4. Ruota la faccia blu una volta.\n'
            '5. Ruota la faccia bianca una volta.\n'
            '6. Ruota la faccia blu una volta.\n'
            '7. Ruota la faccia bianca tre volte.\n'
            '8. Ruota la faccia blu tre volte.'
        ),

        'g3a1g1a3b3a3b1a1': (
            '1. Ruota la faccia rossa tre volte.\n'
            '2. Ruota la faccia blu una volta.\n'
            '3. Ruota la faccia rossa una volta.\n'
            '4. Ruota la faccia blu tre volte.\n'
            '5. Ruota la faccia bianca tre volte.\n'
            '6. Ruota la faccia blu tre volte.\n'
            '7. Ruota la faccia bianca una volta.\n'
            '8. Ruota la faccia blu una volta.'
        ),

        'v1n3v3n1b2n1b2n3': (
            '1. Ruota la faccia verde una volta.\n'
            '2. Ruota la faccia arancione tre volte.\n'
            '3. Ruota la faccia verde tre volte.\n'
            '4. Ruota la faccia arancione una volta.\n'
            '5. Ruota la faccia bianca due volte.\n'
            '6. Ruota la faccia arancione una volta.\n'
            '7. Ruota la faccia bianca due volte.\n'
            '8. Ruota la faccia arancione tre volte.'
        ),

        'a3n1a1n3b2n3b2n1': (
            '1. Ruota la faccia blu tre volte.\n'
            '2. Ruota la faccia arancione una volta.\n'
            '3. Ruota la faccia blu una volta.\n'
            '4. Ruota la faccia arancione tre volte.\n'
            '5. Ruota la faccia bianca due volte.\n'
            '6. Ruota la faccia arancione tre volte.\n'
            '7. Ruota la faccia bianca due volte.\n'
            '8. Ruota la faccia arancione una volta.'
        ),

        'v1n3v3n1b1n1b3n3': (
            '1. Ruota la faccia verde una volta.\n'
            '2. Ruota la faccia arancione tre volte.\n'
            '3. Ruota la faccia verde tre volte.\n'
            '4. Ruota la faccia arancione una volta.\n'
            '5. Ruota la faccia bianca una volta.\n'
            '6. Ruota la faccia arancione una volta.\n'
            '7. Ruota la faccia bianca tre volte.\n'
            '8. Ruota la faccia arancione tre volte.'
        ),

        'a3n1a1n3b3n3b1n1': (
            '1. Ruota la faccia blu tre volte.\n'
            '2. Ruota la faccia arancione una volta.\n'
            '3. Ruota la faccia blu una volta.\n'
            '4. Ruota la faccia arancione tre volte.\n'
            '5. Ruota la faccia bianca tre volte.\n'
            '6. Ruota la faccia arancione tre volte.\n'
            '7. Ruota la faccia bianca una volta.\n'
            '8. Ruota la faccia arancione una volta.'
        ),

        'g1v3g3v1b2v1b2v3': (
            '1. Ruota la faccia rossa una volta.\n'
            '2. Ruota la faccia verde tre volte.\n'
            '3. Ruota la faccia rossa tre volte.\n'
            '4. Ruota la faccia verde una volta.\n'
            '5. Ruota la faccia bianca due volte.\n'
            '6. Ruota la faccia verde una volta.\n'
            '7. Ruota la faccia bianca due volte.\n'
            '8. Ruota la faccia verde tre volte.'
        ),

        'n3v1n1v3b2v3b2v1': (
            '1. Ruota la faccia arancione tre volte.\n'
            '2. Ruota la faccia verde una volta.\n'
            '3. Ruota la faccia arancione una volta.\n'
            '4. Ruota la faccia verde tre volte.\n'
            '5. Ruota la faccia bianca due volte.\n'
            '6. Ruota la faccia verde tre volte.\n'
            '7. Ruota la faccia bianca due volte.\n'
            '8. Ruota la faccia verde una volta.'
        ),

        'g1v3g3v1b1v1b3v3': (
            '1. Ruota la faccia rossa una volta.\n'
            '2. Ruota la faccia verde tre volte.\n'
            '3. Ruota la faccia rossa tre volte.\n'
            '4. Ruota la faccia verde una volta.\n'
            '5. Ruota la faccia bianca una volta.\n'
            '6. Ruota la faccia verde una volta.\n'
            '7. Ruota la faccia bianca tre volte.\n'
            '8. Ruota la faccia verde tre volte.'
        ),

        'n3v1n1v3b3v3b1v1': (
            '1. Ruota la faccia arancione tre volte.\n'
            '2. Ruota la faccia verde una volta.\n'
            '3. Ruota la faccia arancione una volta.\n'
            '4. Ruota la faccia verde tre volte.\n'
            '5. Ruota la faccia bianca tre volte.\n'
            '6. Ruota la faccia verde tre volte.\n'
            '7. Ruota la faccia bianca una volta.\n'
            '8. Ruota la faccia verde una volta.'
        )
    },
    'de': {
        'welcome':         "Willkommen beim Rubik's Cube",
        'press_start':     'Wenn du bereit bist, drücke Start',
        'start':           'Start',
        'language':        'Sprache',
        'about':           'Info',
        'exit':            'Beenden',
        'solve_cube':      'Würfel lösen',
        'toggle_view':     '3D/Netzansicht umschalten',
        'reset_cube':      'Würfel zurücksetzen',
        'shuffle_cube':    'Würfel mischen',
        'coment':          "Funktionsweise der Lösung\n\n"
                            "- Kanonische Bahn: Wenn dein Würfel bereits zur kanonischen Bahn gehört, d.h. keine falsch orientierten Teile hat, suchen wir direkt die Zugfolge im Graphen.\n"
                            "- Andere Bahn: Wenn wir ein fehlorientiertes Teil feststellen, berechnen wir alle gültigen Orientierungen (es gibt 4 im Graphen), bitten dich anzugeben, welche falsch ist, um die richtige zu verwenden, und generieren dann die Lösung ab diesem Knoten.\n\n"
                            "Der Prozess in einer anderen Bahn hat drei Phasen:\n"
                            "  1) Erste Korrektur des fehlorientierten Teils. Behalte dies im Hinterkopf, wenn du dich am Bild rechts orientierst.\n"
                            "  2) Kanonische Züge, um die Bahn zur Lösung zu führen.\n"
                            "  3) Letzte 'Entkorrektur', um das Teil in seine ursprüngliche Bahn zurückzuführen.\n\n"
                            "Folge den Schritten im rechten Bedienfeld.\n\n"
                            "Vielen Dank für die Nutzung des Programms. Ich hoffe, es war hilfreich für dich.\n\n",
        'step':          'Schritt',
        'next_step':       'Nächster Schritt',
        'goto_menu':       'Zum Menü zurück',
        'solution_complete': 'Lösung abgeschlossen!',
        'cube_shuffled':   'Würfel gemischt',
        'already_solved':  'Der Würfel ist bereits gelöst. Ein Neustart ist nicht möglich',
        'cube_reset':      'Würfel zurückgesetzt',
        'cube_solved':     'Der Würfel ist bereits gelöst.',
        'only_9':          'Es dürfen nur 9 Felder jeder Farbe vorhanden sein.',
        'not_found':       'Zug im Graphen nicht gefunden. Möglicherweise in einer anderen Bahn.',
        'question_orbit':  'Möchtest du in einer anderen Bahn fortfahren oder den Würfel korrigieren?',
        'continue_orbit':  'In anderer Bahn fortfahren',
        'correct_cube':    'Würfel korrigieren',
        'dontknow':        'Ich weiß nicht, welches ich gedreht habe',
        'arista_flipped':  'Kante umgedreht',
        'choose_arista_flipped': 'Wähle die Kante, die du umgedreht hast',
        'random_solution': 'Ich habe eine zufällige Lösung für die Kante ausgewählt.',
        'esquina_flipped': 'Ecke umgedreht',
        'choose_esquina_flipped': 'Wähle die Ecke, die du umgedreht hast',
        'random_solution_esquina': 'Ich habe eine zufällige Lösung für die Ecke ausgewählt.',
        'select_lenguage': 'Sprache auswählen',
        'lenguage':        'Sprache',
        'lenguage_selected': 'Sprache ausgewählt',
        'about_text':      "Über den Rubik's Cube" \
                            "<b>Rubik's Cube App</b><br>Version 1.0<br>Entwickelt von RanaCGames<br>" \
                            "Dieses Programm ermöglicht es dir, die letzte Fläche eines Rubik's Cube interaktiv zu lösen.<br>" \
                            "Es berücksichtigt auch die verschiedenen Bahnen der Rubik-Gruppe.<br>" \
                            "Ein TFG-Projekt, Universidad Alfonso X, 2025<br>" \
                            "Fehler sind möglich, zögere aber nicht, sie zu melden.<br>" \
                            "Vielen Dank für die Nutzung!<br>",
        'b1': 'Drehe die weiße Fläche einmal.',

        'g1b2g3b2g3a1g1a3': (
            '1. Drehe die rote Fläche einmal.\n'
            '2. Drehe die weiße Fläche zweimal.\n'
            '3. Drehe die rote Fläche dreimal.\n'
            '4. Drehe die weiße Fläche zweimal.\n'
            '5. Drehe die rote Fläche dreimal.\n'
            '6. Drehe die blaue Fläche einmal.\n'
            '7. Drehe die rote Fläche einmal.\n'
            '8. Drehe die blaue Fläche dreimal.'
        ),

        'g3b2g1b2g1v3g3v1': (
            '1. Drehe die rote Fläche dreimal.\n'
            '2. Drehe die weiße Fläche zweimal.\n'
            '3. Drehe die rote Fläche einmal.\n'
            '4. Drehe die weiße Fläche zweimal.\n'
            '5. Drehe die rote Fläche einmal.\n'
            '6. Drehe die grüne Fläche dreimal.\n'
            '7. Drehe die rote Fläche dreimal.\n'
            '8. Drehe die grüne Fläche einmal.'
        ),

        'g1b1g3b3g3a1g1a3': (
            '1. Drehe die rote Fläche einmal.\n'
            '2. Drehe die weiße Fläche einmal.\n'
            '3. Drehe die rote Fläche dreimal.\n'
            '4. Drehe die weiße Fläche dreimal.\n'
            '5. Drehe die rote Fläche dreimal.\n'
            '6. Drehe die blaue Fläche einmal.\n'
            '7. Drehe die rote Fläche einmal.\n'
            '8. Drehe die blaue Fläche dreimal.'
        ),

        'g3b3g1b1g1v3g3v1': (
            '1. Drehe die rote Fläche dreimal.\n'
            '2. Drehe die weiße Fläche dreimal.\n'
            '3. Drehe die rote Fläche einmal.\n'
            '4. Drehe die weiße Fläche einmal.\n'
            '5. Drehe die rote Fläche einmal.\n'
            '6. Drehe die grüne Fläche dreimal.\n'
            '7. Drehe die rote Fläche dreimal.\n'
            '8. Drehe die grüne Fläche einmal.'
        ),

        'a1b2a3b2a3n1a1n3': (
            '1. Drehe die blaue Fläche einmal.\n'
            '2. Drehe die weiße Fläche zweimal.\n'
            '3. Drehe die blaue Fläche dreimal.\n'
            '4. Drehe die weiße Fläche zweimal.\n'
            '5. Drehe die blaue Fläche dreimal.\n'
            '6. Drehe die orange Fläche einmal.\n'
            '7. Drehe die blaue Fläche einmal.\n'
            '8. Drehe die orange Fläche dreimal.'
        ),

        'a3b2a1b2a1g3a3g1': (
            '1. Drehe die blaue Fläche dreimal.\n'
            '2. Drehe die weiße Fläche zweimal.\n'
            '3. Drehe die blaue Fläche einmal.\n'
            '4. Drehe die weiße Fläche zweimal.\n'
            '5. Drehe die blaue Fläche einmal.\n'
            '6. Drehe die rote Fläche dreimal.\n'
            '7. Drehe die blaue Fläche dreimal.\n'
            '8. Drehe die rote Fläche einmal.'
        ),

        'a1b1a3b3a3n1a1n3': (
            '1. Drehe die blaue Fläche einmal.\n'
            '2. Drehe die weiße Fläche einmal.\n'
            '3. Drehe die blaue Fläche dreimal.\n'
            '4. Drehe die weiße Fläche dreimal.\n'
            '5. Drehe die blaue Fläche dreimal.\n'
            '6. Drehe die orange Fläche einmal.\n'
            '7. Drehe die blaue Fläche einmal.\n'
            '8. Drehe die orange Fläche dreimal.'
        ),

        'a3b3a1b1a1g3a3g1': (
            '1. Drehe die blaue Fläche dreimal.\n'
            '2. Drehe die weiße Fläche dreimal.\n'
            '3. Drehe die blaue Fläche einmal.\n'
            '4. Drehe die weiße Fläche einmal.\n'
            '5. Drehe die blaue Fläche einmal.\n'
            '6. Drehe die rote Fläche dreimal.\n'
            '7. Drehe die blaue Fläche dreimal.\n'
            '8. Drehe die rote Fläche einmal.'
        ),

        'n1b2n3b2n3v1n1v3': (
            '1. Drehe die orange Fläche einmal.\n'
            '2. Drehe die weiße Fläche zweimal.\n'
            '3. Drehe die orange Fläche dreimal.\n'
            '4. Drehe die weiße Fläche zweimal.\n'
            '5. Drehe die orange Fläche dreimal.\n'
            '6. Drehe die grüne Fläche einmal.\n'
            '7. Drehe die orange Fläche einmal.\n'
            '8. Drehe die grüne Fläche dreimal.'
        ),

        'n3b2n1b2n1a3n3a1': (
            '1. Drehe die orange Fläche dreimal.\n'
            '2. Drehe die weiße Fläche zweimal.\n'
            '3. Drehe die orange Fläche einmal.\n'
            '4. Drehe die weiße Fläche zweimal.\n'
            '5. Drehe die orange Fläche einmal.\n'
            '6. Drehe die blaue Fläche dreimal.\n'
            '7. Drehe die orange Fläche dreimal.\n'
            '8. Drehe die blaue Fläche einmal.'
        ),
        'n1b1n3b3n3v1n1v3': (
            '1. Drehe die orange Fläche einmal.\n'
            '2. Drehe die weiße Fläche einmal.\n'
            '3. Drehe die orange Fläche dreimal.\n'
            '4. Drehe die weiße Fläche dreimal.\n'
            '5. Drehe die orange Fläche dreimal.\n'
            '6. Drehe die grüne Fläche einmal.\n'
            '7. Drehe die orange Fläche einmal.\n'
            '8. Drehe die grüne Fläche dreimal.'
        ),
        'n3b3n1b1n1a3n3a1': (
            '1. Drehe die orange Fläche dreimal.\n'
            '2. Drehe die weiße Fläche dreimal.\n'
            '3. Drehe die orange Fläche einmal.\n'
            '4. Drehe die weiße Fläche einmal.\n'
            '5. Drehe die orange Fläche einmal.\n'
            '6. Drehe die blaue Fläche dreimal.\n'
            '7. Drehe die orange Fläche dreimal.\n'
            '8. Drehe die blaue Fläche einmal.'
        ),
        'v1b2v3b2v3g1v1g3': (
            '1. Drehe die grüne Fläche einmal.\n'
            '2. Drehe die weiße Fläche zweimal.\n'
            '3. Drehe die grüne Fläche dreimal.\n'
            '4. Drehe die weiße Fläche zweimal.\n'
            '5. Drehe die grüne Fläche dreimal.\n'
            '6. Drehe die rote Fläche einmal.\n'
            '7. Drehe die grüne Fläche einmal.\n'
            '8. Drehe die rote Fläche dreimal.'
        ),
        'v3b2v1b2v1n3v3n1': (
            '1. Drehe die grüne Fläche dreimal.\n'
            '2. Drehe die weiße Fläche zweimal.\n'
            '3. Drehe die grüne Fläche einmal.\n'
            '4. Drehe die weiße Fläche zweimal.\n'
            '5. Drehe die grüne Fläche einmal.\n'
            '6. Drehe die orange Fläche dreimal.\n'
            '7. Drehe die grüne Fläche dreimal.\n'
            '8. Drehe die orange Fläche einmal.'
        ),
        'v1b1v3b3v3g1v1g3': (
            '1. Drehe die grüne Fläche einmal.\n'
            '2. Drehe die weiße Fläche einmal.\n'
            '3. Drehe die grüne Fläche dreimal.\n'
            '4. Drehe die weiße Fläche dreimal.\n'
            '5. Drehe die grüne Fläche dreimal.\n'
            '6. Drehe die rote Fläche einmal.\n'
            '7. Drehe die grüne Fläche einmal.\n'
            '8. Drehe die rote Fläche dreimal.'
        ),
        'v3b3v1b1v1n3v3n1': (
            '1. Drehe die grüne Fläche dreimal.\n'
            '2. Drehe die weiße Fläche dreimal.\n'
            '3. Drehe die grüne Fläche einmal.\n'
            '4. Drehe die weiße Fläche einmal.\n'
            '5. Drehe die grüne Fläche einmal.\n'
            '6. Drehe die orange Fläche dreimal.\n'
            '7. Drehe die grüne Fläche dreimal.\n'
            '8. Drehe die orange Fläche einmal.'
        ),
        'b3': 'Die weiße Fläche dreimal drehen.',
        
        'a1g3a3g1b2g1b2g3': (
            '1. Drehe die blaue Fläche einmal.\n'
            '2. Drehe die rote Fläche dreimal.\n'
            '3. Drehe die blaue Fläche dreimal.\n'
            '4. Drehe die rote Fläche einmal.\n'
            '5. Drehe die weiße Fläche zweimal.\n'
            '6. Drehe die rote Fläche einmal.\n'
            '7. Drehe die weiße Fläche zweimal.\n'
            '8. Drehe die rote Fläche dreimal.'
        ),

        'v3g1v1g3b2g3b2g1': (
            '1. Drehe die grüne Fläche dreimal.\n'
            '2. Drehe die rote Fläche einmal.\n'
            '3. Drehe die grüne Fläche einmal.\n'
            '4. Drehe die rote Fläche dreimal.\n'
            '5. Drehe die weiße Fläche zweimal.\n'
            '6. Drehe die rote Fläche dreimal.\n'
            '7. Drehe die weiße Fläche zweimal.\n'
            '8. Drehe die rote Fläche einmal.'
        ),

        'a1g3a3g1b1g1b3g3': (
            '1. Drehe die blaue Fläche einmal.\n'
            '2. Drehe die rote Fläche dreimal.\n'
            '3. Drehe die blaue Fläche dreimal.\n'
            '4. Drehe die rote Fläche einmal.\n'
            '5. Drehe die weiße Fläche einmal.\n'
            '6. Drehe die rote Fläche einmal.\n'
            '7. Drehe die weiße Fläche dreimal.\n'
            '8. Drehe die rote Fläche dreimal.'
        ),

        'v3g1v1g3b3g3b1g1': (
            '1. Drehe die grüne Fläche dreimal.\n'
            '2. Drehe die rote Fläche einmal.\n'
            '3. Drehe die grüne Fläche einmal.\n'
            '4. Drehe die rote Fläche dreimal.\n'
            '5. Drehe die weiße Fläche dreimal.\n'
            '6. Drehe die rote Fläche dreimal.\n'
            '7. Drehe die weiße Fläche einmal.\n'
            '8. Drehe die rote Fläche einmal.'
        ),

        'n1a3n3a1b2a1b2a3': (
            '1. Drehe die orange Fläche einmal.\n'
            '2. Drehe die blaue Fläche dreimal.\n'
            '3. Drehe die orange Fläche dreimal.\n'
            '4. Drehe die blaue Fläche einmal.\n'
            '5. Drehe die weiße Fläche zweimal.\n'
            '6. Drehe die blaue Fläche einmal.\n'
            '7. Drehe die weiße Fläche zweimal.\n'
            '8. Drehe die blaue Fläche dreimal.'
        ),

        'g3a1g1a3b2a3b2a1': (
            '1. Drehe die rote Fläche dreimal.\n'
            '2. Drehe die blaue Fläche einmal.\n'
            '3. Drehe die rote Fläche einmal.\n'
            '4. Drehe die blaue Fläche dreimal.\n'
            '5. Drehe die weiße Fläche zweimal.\n'
            '6. Drehe die blaue Fläche dreimal.\n'
            '7. Drehe die weiße Fläche zweimal.\n'
            '8. Drehe die blaue Fläche einmal.'
        ),

        'n1a3n3a1b1a1b3a3': (
            '1. Drehe die orange Fläche einmal.\n'
            '2. Drehe die blaue Fläche dreimal.\n'
            '3. Drehe die orange Fläche dreimal.\n'
            '4. Drehe die blaue Fläche einmal.\n'
            '5. Drehe die weiße Fläche einmal.\n'
            '6. Drehe die blaue Fläche einmal.\n'
            '7. Drehe die weiße Fläche dreimal.\n'
            '8. Drehe die blaue Fläche dreimal.'
        ),

        'g3a1g1a3b3a3b1a1': (
            '1. Drehe die rote Fläche dreimal.\n'
            '2. Drehe die blaue Fläche einmal.\n'
            '3. Drehe die rote Fläche einmal.\n'
            '4. Drehe die blaue Fläche dreimal.\n'
            '5. Drehe die weiße Fläche dreimal.\n'
            '6. Drehe die blaue Fläche dreimal.\n'
            '7. Drehe die weiße Fläche einmal.\n'
            '8. Drehe die blaue Fläche einmal.'
        ),

        'v1n3v3n1b2n1b2n3': (
            '1. Drehe die grüne Fläche einmal.\n'
            '2. Drehe die orange Fläche dreimal.\n'
            '3. Drehe die grüne Fläche dreimal.\n'
            '4. Drehe die orange Fläche einmal.\n'
            '5. Drehe die weiße Fläche zweimal.\n'
            '6. Drehe die orange Fläche einmal.\n'
            '7. Drehe die weiße Fläche zweimal.\n'
            '8. Drehe die orange Fläche dreimal.'
        ),

        'a3n1a1n3b2n3b2n1': (
            '1. Drehe die blaue Fläche dreimal.\n'
            '2. Drehe die orange Fläche einmal.\n'
            '3. Drehe die blaue Fläche einmal.\n'
            '4. Drehe die orange Fläche dreimal.\n'
            '5. Drehe die weiße Fläche zweimal.\n'
            '6. Drehe die orange Fläche dreimal.\n'
            '7. Drehe die weiße Fläche zweimal.\n'
            '8. Drehe die orange Fläche einmal.'
        ),

        'v1n3v3n1b1n1b3n3': (
            '1. Drehe die grüne Fläche einmal.\n'
            '2. Drehe die orange Fläche dreimal.\n'
            '3. Drehe die grüne Fläche dreimal.\n'
            '4. Drehe die orange Fläche einmal.\n'
            '5. Drehe die weiße Fläche einmal.\n'
            '6. Drehe die orange Fläche einmal.\n'
            '7. Drehe die weiße Fläche dreimal.\n'
            '8. Drehe die orange Fläche dreimal.'
        ),

        'a3n1a1n3b3n3b1n1': (
            '1. Drehe die blaue Fläche dreimal.\n'
            '2. Drehe die orange Fläche einmal.\n'
            '3. Drehe die blaue Fläche einmal.\n'
            '4. Drehe die orange Fläche dreimal.\n'
            '5. Drehe die weiße Fläche dreimal.\n'
            '6. Drehe die orange Fläche dreimal.\n'
            '7. Drehe die weiße Fläche einmal.\n'
            '8. Drehe die orange Fläche einmal.'
        ),
        'g1v3g3v1b2v1b2v3': (
            '1. Drehe die rote Fläche einmal.\n'
            '2. Drehe die grüne Fläche dreimal.\n'
            '3. Drehe die rote Fläche dreimal.\n'
            '4. Drehe die grüne Fläche einmal.\n'
            '5. Drehe die weiße Fläche zweimal.\n'
            '6. Drehe die grüne Fläche einmal.\n'
            '7. Drehe die weiße Fläche zweimal.\n'
            '8. Drehe die grüne Fläche dreimal.'
        ),
        'n3v1n1v3b2v3b2v1': (
            '1. Drehe die orange Fläche dreimal.\n'
            '2. Drehe die grüne Fläche einmal.\n'
            '3. Drehe die orange Fläche einmal.\n'
            '4. Drehe die grüne Fläche dreimal.\n'
            '5. Drehe die weiße Fläche zweimal.\n'
            '6. Drehe die grüne Fläche dreimal.\n'
            '7. Drehe die weiße Fläche zweimal.\n'
            '8. Drehe die grüne Fläche einmal.'
        ),
        'g1v3g3v1b1v1b3v3': (
            '1. Drehe die rote Fläche einmal.\n'
            '2. Drehe die grüne Fläche dreimal.\n'
            '3. Drehe die rote Fläche dreimal.\n'
            '4. Drehe die grüne Fläche einmal.\n'
            '5. Drehe die weiße Fläche einmal.\n'
            '6. Drehe die grüne Fläche einmal.\n'
            '7. Drehe die weiße Fläche dreimal.\n'
            '8. Drehe die grüne Fläche dreimal.'
        ),
        'n3v1n1v3b3v3b1v1': (
            '1. Drehe die orange Fläche dreimal.\n'
            '2. Drehe die grüne Fläche einmal.\n'
            '3. Drehe die orange Fläche einmal.\n'
            '4. Drehe die grüne Fläche dreimal.\n'
            '5. Drehe die weiße Fläche dreimal.\n'
            '6. Drehe die grüne Fläche dreimal.\n'
            '7. Drehe die weiße Fläche einmal.\n'
            '8. Drehe die grüne Fläche einmal.'
        ),
    },
    'fr': {
        'welcome':         'Bienvenue sur le Rubik\'s Cube',
        'press_start':     'Lorsque vous êtes prêt, appuyez sur Démarrer',
        'start':           'Démarrer',
        'language':        'Langue',
        'about':           'À propos',
        'exit':            'Quitter',
        'solve_cube':      'Résoudre le cube',
        'toggle_view':     'Basculer vue 3D/grille',
        'reset_cube':      'Réinitialiser le cube',
        'shuffle_cube':    'Mélanger le cube',
        'coment':          "Comment fonctionne la solution\n\n"
                            "- Orbite canonique : Si votre cube appartient déjà à l'orbite canonique, c'est-à-dire qu'il n'a aucune pièce mal orientée, nous cherchons la séquence de mouvements dans le graphe.\n"
                            "- Autre orbite : Si nous détectons une pièce désorientée, nous calculons toutes les orientations valides (il y en a 4 dans le graphe), vous demandons d'indiquer laquelle est incorrecte pour utiliser la bonne, puis générons la solution à partir de ce nœud.\n\n"
                            "Le processus dans une autre orbite comporte trois phases :\n"
                            "  1) Correction initiale de la pièce désorientée. Gardez cela à l'esprit si vous suivez l'image de droite.\n"
                            "  2) Mouvements canoniques pour amener l'orbite à la solution.\n"
                            "  3) 'Dé-correction' finale pour renvoyer la pièce dans son orbite d'origine.\n\n"
                            "Suivez les étapes dans le panneau de droite.\n\n"
                            "Merci beaucoup d'utiliser le programme et j'espère qu'il vous a été utile.\n\n",
        'step':          'Étape',
        'next_step':       'Étape suivante',
        'goto_menu':       'Retour au menu',
        'solution_complete': 'Solution terminée !',
        'cube_shuffled':   'Cube mélangé',
        'already_solved':  'Le cube est déjà résolu. Impossible de réinitialiser',
        'cube_reset':      'Cube réinitialisé',
        'cube_solved':     'Le cube est déjà résolu.',
        'only_9':          'Il ne peut y avoir que 9 cases de chaque couleur.',
        'not_found':       'Mouvement non trouvé dans le graphe. Il pourrait être dans une autre orbite.',
        'question_orbit':  'Souhaitez-vous continuer dans une autre orbite ou corriger le cube ?',
        'continue_orbit':  'Continuer dans une autre orbite',
        'correct_cube':    'Corriger le cube',
        'dontknow':        "Je ne sais pas lequel j'ai retourné",
        'arista_flipped':  'Arête inversée',
        'choose_arista_flipped': 'Choisissez l’arête que vous avez retournée',
        'random_solution': 'J’ai sélectionné une solution aléatoire pour l’arête.',
        'esquina_flipped': 'Coin inversé',
        'choose_esquina_flipped': 'Choisissez le coin que vous avez retourné',
        'random_solution_esquina': 'J’ai sélectionné une solution aléatoire pour le coin.',
        'select_lenguage': 'Sélectionnez la langue',
        'lenguage':        'Langue',
        'lenguage_selected': 'Langue sélectionnée',
        'about_text':      "À propos du Rubik's Cube" \
                            "<b>Application Rubik's Cube</b><br>Version 1.0<br>Développé par RanaCGames<br>" \
                            "Ce programme vous permet de résoudre la dernière face d'un Rubik's Cube de manière interactive.<br>" \
                            "Il prend également en compte les différentes orbites du groupe Rubik.<br>" \
                            "Projet de TFG, Universidad Alfonso X, 2025<br>" \
                            "Des erreurs peuvent survenir, n'hésitez pas à les signaler.<br>" \
                            "Merci de l'utiliser !<br>",
        'b1': 'Tournez la face blanche une fois.',

        'g1b2g3b2g3a1g1a3': (
            '1. Tournez la face rouge une fois.\n'
            '2. Tournez la face blanche deux fois.\n'
            '3. Tournez la face rouge trois fois.\n'
            '4. Tournez la face blanche deux fois.\n'
            '5. Tournez la face rouge trois fois.\n'
            '6. Tournez la face bleue une fois.\n'
            '7. Tournez la face rouge une fois.\n'
            '8. Tournez la face bleue trois fois.'
        ),

        'g3b2g1b2g1v3g3v1': (
            '1. Tournez la face rouge trois fois.\n'
            '2. Tournez la face blanche deux fois.\n'
            '3. Tournez la face rouge une fois.\n'
            '4. Tournez la face blanche deux fois.\n'
            '5. Tournez la face rouge une fois.\n'
            '6. Tournez la face verte trois fois.\n'
            '7. Tournez la face rouge trois fois.\n'
            '8. Tournez la face verte une fois.'
        ),

        'g1b1g3b3g3a1g1a3': (
            '1. Tournez la face rouge une fois.\n'
            '2. Tournez la face blanche une fois.\n'
            '3. Tournez la face rouge trois fois.\n'
            '4. Tournez la face blanche trois fois.\n'
            '5. Tournez la face rouge trois fois.\n'
            '6. Tournez la face bleue une fois.\n'
            '7. Tournez la face rouge une fois.\n'
            '8. Tournez la face bleue trois fois.'
        ),

        'g3b3g1b1g1v3g3v1': (
            '1. Tournez la face rouge trois fois.\n'
            '2. Tournez la face blanche trois fois.\n'
            '3. Tournez la face rouge une fois.\n'
            '4. Tournez la face blanche une fois.\n'
            '5. Tournez la face rouge une fois.\n'
            '6. Tournez la face verte trois fois.\n'
            '7. Tournez la face rouge trois fois.\n'
            '8. Tournez la face verte une fois.'
        ),

        'a1b2a3b2a3n1a1n3': (
            '1. Tournez la face bleue une fois.\n'
            '2. Tournez la face blanche deux fois.\n'
            '3. Tournez la face bleue trois fois.\n'
            '4. Tournez la face blanche deux fois.\n'
            '5. Tournez la face bleue trois fois.\n'
            '6. Tournez la face orange une fois.\n'
            '7. Tournez la face bleue une fois.\n'
            '8. Tournez la face orange trois fois.'
        ),

        'a3b2a1b2a1g3a3g1': (
            '1. Tournez la face bleue trois fois.\n'
            '2. Tournez la face blanche deux fois.\n'
            '3. Tournez la face bleue une fois.\n'
            '4. Tournez la face blanche deux fois.\n'
            '5. Tournez la face bleue une fois.\n'
            '6. Tournez la face rouge trois fois.\n'
            '7. Tournez la face bleue trois fois.\n'
            '8. Tournez la face rouge une fois.'
        ),

        'a1b1a3b3a3n1a1n3': (
            '1. Tournez la face bleue une fois.\n'
            '2. Tournez la face blanche une fois.\n'
            '3. Tournez la face bleue trois fois.\n'
            '4. Tournez la face blanche trois fois.\n'
            '5. Tournez la face bleue trois fois.\n'
            '6. Tournez la face orange une fois.\n'
            '7. Tournez la face bleue une fois.\n'
            '8. Tournez la face orange trois fois.'
        ),

        'a3b3a1b1a1g3a3g1': (
            '1. Tournez la face bleue trois fois.\n'
            '2. Tournez la face blanche trois fois.\n'
            '3. Tournez la face bleue une fois.\n'
            '4. Tournez la face blanche une fois.\n'
            '5. Tournez la face bleue une fois.\n'
            '6. Tournez la face rouge trois fois.\n'
            '7. Tournez la face bleue trois fois.\n'
            '8. Tournez la face rouge une fois.'
        ),

        'n1b2n3b2n3v1n1v3': (
            '1. Tournez la face orange une fois.\n'
            '2. Tournez la face blanche deux fois.\n'
            '3. Tournez la face orange trois fois.\n'
            '4. Tournez la face blanche deux fois.\n'
            '5. Tournez la face orange trois fois.\n'
            '6. Tournez la face verte une fois.\n'
            '7. Tournez la face orange une fois.\n'
            '8. Tournez la face verte trois fois.'
        ),

        'n3b2n1b2n1a3n3a1': (
            '1. Tournez la face orange trois fois.\n'
            '2. Tournez la face blanche deux fois.\n'
            '3. Tournez la face orange une fois.\n'
            '4. Tournez la face blanche deux fois.\n'
            '5. Tournez la face orange une fois.\n'
            '6. Tournez la face bleue trois fois.\n'
            '7. Tournez la face orange trois fois.\n'
            '8. Tournez la face bleue une fois.'
        ),
        'n1b1n3b3n3v1n1v3': (
            '1. Tournez la face orange une fois.\n'
            '2. Tournez la face blanche une fois.\n'
            '3. Tournez la face orange trois fois.\n'
            '4. Tournez la face blanche trois fois.\n'
            '5. Tournez la face orange trois fois.\n'
            '6. Tournez la face verte une fois.\n'
            '7. Tournez la face orange une fois.\n'
            '8. Tournez la face verte trois fois.'
        ),
        'n3b3n1b1n1a3n3a1': (
            '1. Tournez la face orange trois fois.\n'
            '2. Tournez la face blanche trois fois.\n'
            '3. Tournez la face orange une fois.\n'
            '4. Tournez la face blanche une fois.\n'
            '5. Tournez la face orange une fois.\n'
            '6. Tournez la face bleue trois fois.\n'
            '7. Tournez la face orange trois fois.\n'
            '8. Tournez la face bleue une fois.'
        ),
        'v1b2v3b2v3g1v1g3': (
            '1. Tournez la face verte une fois.\n'
            '2. Tournez la face blanche deux fois.\n'
            '3. Tournez la face verte trois fois.\n'
            '4. Tournez la face blanche deux fois.\n'
            '5. Tournez la face verte trois fois.\n'
            '6. Tournez la face rouge une fois.\n'
            '7. Tournez la face verte une fois.\n'
            '8. Tournez la face rouge trois fois.'
        ),
        'v3b2v1b2v1n3v3n1': (
            '1. Tournez la face verte trois fois.\n'
            '2. Tournez la face blanche deux fois.\n'
            '3. Tournez la face verte une fois.\n'
            '4. Tournez la face blanche deux fois.\n'
            '5. Tournez la face verte une fois.\n'
            '6. Tournez la face orange trois fois.\n'
            '7. Tournez la face verte trois fois.\n'
            '8. Tournez la face orange une fois.'
        ),
        'v1b1v3b3v3g1v1g3': (
            '1. Tournez la face verte une fois.\n'
            '2. Tournez la face blanche une fois.\n'
            '3. Tournez la face verte trois fois.\n'
            '4. Tournez la face blanche trois fois.\n'
            '5. Tournez la face verte trois fois.\n'
            '6. Tournez la face rouge une fois.\n'
            '7. Tournez la face verte une fois.\n'
            '8. Tournez la face rouge trois fois.'
        ),
        'v3b3v1b1v1n3v3n1': (
            '1. Tournez la face verte trois fois.\n'
            '2. Tournez la face blanche trois fois.\n'
            '3. Tournez la face verte une fois.\n'
            '4. Tournez la face blanche une fois.\n'
            '5. Tournez la face verte une fois.\n'
            '6. Tournez la face orange trois fois.\n'
            '7. Tournez la face verte trois fois.\n'
            '8. Tournez la face orange une fois.'
        ),
        'b3': 'Tournez la face blanche trois fois.',
        'a1g3a3g1b2g1b2g3': (
            '1. Tournez la face bleue une fois.\n'
            '2. Tournez la face rouge trois fois.\n'
            '3. Tournez la face bleue trois fois.\n'
            '4. Tournez la face rouge une fois.\n'
            '5. Tournez la face blanche deux fois.\n'
            '6. Tournez la face rouge une fois.\n'
            '7. Tournez la face blanche deux fois.\n'
            '8. Tournez la face rouge trois fois.'
        ),
        'v3g1v1g3b2g3b2g1': (
            '1. Tournez la face verte trois fois.\n'
            '2. Tournez la face rouge une fois.\n'
            '3. Tournez la face verte une fois.\n'
            '4. Tournez la face rouge trois fois.\n'
            '5. Tournez la face blanche deux fois.\n'
            '6. Tournez la face rouge trois fois.\n'
            '7. Tournez la face blanche deux fois.\n'
            '8. Tournez la face rouge une fois.'
        ),
        'a1g3a3g1b1g1b3g3': (
            '1. Tournez la face bleue une fois.\n'
            '2. Tournez la face rouge trois fois.\n'
            '3. Tournez la face bleue trois fois.\n'
            '4. Tournez la face rouge une fois.\n'
            '5. Tournez la face blanche une fois.\n'
            '6. Tournez la face rouge une fois.\n'
            '7. Tournez la face blanche trois fois.\n'
            '8. Tournez la face rouge trois fois.'
        ),
        'v3g1v1g3b3g3b1g1': (
            '1. Tournez la face verte trois fois.\n'
            '2. Tournez la face rouge une fois.\n'
            '3. Tournez la face verte une fois.\n'
            '4. Tournez la face rouge trois fois.\n'
            '5. Tournez la face blanche trois fois.\n'
            '6. Tournez la face rouge trois fois.\n'
            '7. Tournez la face blanche une fois.\n'
            '8. Tournez la face rouge une fois.'
        ),
        'n1a3n3a1b2a1b2a3': (
            '1. Tournez la face orange une fois.\n'
            '2. Tournez la face bleue trois fois.\n'
            '3. Tournez la face orange trois fois.\n'
            '4. Tournez la face bleue une fois.\n'
            '5. Tournez la face blanche deux fois.\n'
            '6. Tournez la face bleue une fois.\n'
            '7. Tournez la face blanche deux fois.\n'
            '8. Tournez la face bleue trois fois.'
        ),
        'g3a1g1a3b2a3b2a1': (
            '1. Tournez la face rouge trois fois.\n'
            '2. Tournez la face bleue une fois.\n'
            '3. Tournez la face rouge une fois.\n'
            '4. Tournez la face bleue trois fois.\n'
            '5. Tournez la face blanche deux fois.\n'
            '6. Tournez la face bleue trois fois.\n'
            '7. Tournez la face blanche deux fois.\n'
            '8. Tournez la face bleue une fois.'
        ),
        'v1n3v3n1b2n1b2n3': (
            '1. Tournez la face verte une fois.\n'
            '2. Tournez la face orange trois fois.\n'
            '3. Tournez la face verte trois fois.\n'
            '4. Tournez la face orange une fois.\n'
            '5. Tournez la face blanche deux fois.\n'
            '6. Tournez la face orange une fois.\n'
            '7. Tournez la face blanche deux fois.\n'
            '8. Tournez la face orange trois fois.'
        ),
        'a3n1a1n3b2n3b2n1': (
            '1. Tournez la face bleue trois fois.\n'
            '2. Tournez la face orange une fois.\n'
            '3. Tournez la face bleue une fois.\n'
            '4. Tournez la face orange trois fois.\n'
            '5. Tournez la face blanche deux fois.\n'
            '6. Tournez la face orange trois fois.\n'
            '7. Tournez la face blanche deux fois.\n'
            '8. Tournez la face orange une fois.'
        ),
        'v1n3v3n1b1n1b3n3': (
            '1. Tournez la face verte une fois.\n'
            '2. Tournez la face orange trois fois.\n'
            '3. Tournez la face verte trois fois.\n'
            '4. Tournez la face orange une fois.\n'
            '5. Tournez la face blanche une fois.\n'
            '6. Tournez la face orange une fois.\n'
            '7. Tournez la face blanche trois fois.\n'
            '8. Tournez la face orange trois fois.'
        ),
        'a3n1a1n3b3n3b1n1': (
            '1. Tournez la face bleue trois fois.\n'
            '2. Tournez la face orange une fois.\n'
            '3. Tournez la face bleue une fois.\n'
            '4. Tournez la face orange trois fois.\n'
            '5. Tournez la face blanche trois fois.\n'
            '6. Tournez la face orange trois fois.\n'
            '7. Tournez la face blanche une fois.\n'
            '8. Tournez la face orange une fois.'
        ),
        'g1v3g3v1b2v1b2v3': (
            '1. Tournez la face rouge une fois.\n'
            '2. Tournez la face verte trois fois.\n'
            '3. Tournez la face rouge trois fois.\n'
            '4. Tournez la face verte une fois.\n'
            '5. Tournez la face blanche deux fois.\n'
            '6. Tournez la face verte une fois.\n'
            '7. Tournez la face blanche deux fois.\n'
            '8. Tournez la face verte trois fois.'
        ),
        'n3v1n1v3b2v3b2v1': (
            '1. Tournez la face orange trois fois.\n'
            '2. Tournez la face verte une fois.\n'
            '3. Tournez la face orange une fois.\n'
            '4. Tournez la face verte trois fois.\n'
            '5. Tournez la face blanche deux fois.\n'
            '6. Tournez la face verte trois fois.\n'
            '7. Tournez la face blanche deux fois.\n'
            '8. Tournez la face verte une fois.'
        ),
        'g1v3g3v1b1v1b3v3': (
            '1. Tournez la face rouge une fois.\n'
            '2. Tournez la face verte trois fois.\n'
            '3. Tournez la face rouge trois fois.\n'
            '4. Tournez la face verte une fois.\n'
            '5. Tournez la face blanche une fois.\n'
            '6. Tournez la face verte une fois.\n'
            '7. Tournez la face blanche trois fois.\n'
            '8. Tournez la face verte trois fois.'
        ),
        'n3v1n1v3b3v3b1v1': (
            '1. Tournez la face orange trois fois.\n'
            '2. Tournez la face verte une fois.\n'
            '3. Tournez la face orange une fois.\n'
            '4. Tournez la face verte trois fois.\n'
            '5. Tournez la face blanche trois fois.\n'
            '6. Tournez la face verte trois fois.\n'
            '7. Tournez la face blanche une fois.\n'
            '8. Tournez la face verte une fois.'
        )

    }
}



def t(key, lang='es'):
    """Devuelve la traducción de `key` en el idioma `lang`."""
    return TRADUCCIONES.get(lang, TRADUCCIONES['es']).get(key, key)
