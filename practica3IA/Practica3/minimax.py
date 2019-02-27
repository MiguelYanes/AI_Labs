
# Minimax Search

infinity = 1.0e400


def terminal_test(state, depth):
    return depth <= 0 or state.is_terminal

def max_value(state, player, max_depth):
    """
    Completar con el codigo correspondiente a la funcion <max_value> del
    algoritmo minimax
    """

    f = open("pruebasmm.txt", "a");
    f.write("mm\n");

    if terminal_test(state, max_depth):
        return state.utility(player)
    value = -infinity

    for sucesor in state.successors():
        value = max(value, min_value(sucesor[1], sucesor[1].current_player, max_depth-1))
    return value

def min_value(state, player, max_depth):
    """
    Completar con el codigo correspondiente a la funcion <min_value> del
    algoritmo minimax
    """
    f = open("pruebasmm.txt", "a");
    f.write("mm\n");
    if terminal_test(state, max_depth):
        return state.utility(player)
    value = infinity

    for sucesor in state.successors():
        value = min(value, max_value(sucesor[1], sucesor[1].current_player, max_depth-1))
    return value


def minimax_search(game, max_depth=infinity):
    """
    Given a state in a game, calculate the best move by searching
    forward all the way to the terminal states, or until max_depth
    levels are explored
    """

    player = game.current_player

    # Searches for the action leading to the sucessor state with the highest min score
    successors = game.successors()
    best_score, best_action = -infinity, successors[0][0]
    for (action, state) in successors:
        score = min_value(state, player, max_depth)
        if score > best_score:
            best_score, best_action = score, action
    
    return best_action

