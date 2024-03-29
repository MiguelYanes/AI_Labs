
# AlphaBeta Partial Search

infinity = 1.0e400


def terminal_test(state, depth):
    return depth <= 0 or state.is_terminal

def max_value(state, player, max_depth, alpha, beta, eval_function, generados):
    """
    Completar con el codigo correspondiente a la funcion <max_value> de la
    version del algoritmo minimax con poda alfa-beta
    """
    #f = open("pruebasab.txt", "a");
    #f.write("ab\n");
    if terminal_test(state, max_depth):
        value = eval_function(state, player)
        return value
    value = -infinity

    for sucesor in state.successors():
        value = max(value, min_value(sucesor[1], sucesor[1].current_player, max_depth-1, alpha, beta, eval_function, generados + 1))
        if value >= beta:
            return value
        alpha = max(alpha, value)

    return value

def min_value(state, player, max_depth, alpha, beta, eval_function, generados):
    """
    Completar con el codigo correspondiente a la funcion <min_value> de la
    version del algoritmo minimax con poda alfa-beta
    """
    #f = open("pruebasab.txt", "a");
    #f.write("ab\n");
    if terminal_test(state, max_depth):
        value = eval_function(state, player)
        return value
    value = infinity

    for sucesor in state.successors():
        value = min(value, max_value(sucesor[1], sucesor[1].current_player, max_depth - 1, alpha, beta, eval_function, generados + 1))
        if value <= alpha:
            return value
        beta = min(beta, value)

    return value


def alphabeta_search(game, max_depth, eval_function):
    """
    Search game to determine best action; use alpha-beta pruning.
    This version cuts off search and uses an evaluation function.
    """

    player = game.current_player

    # Searches for the action leading to the sucessor state with the highest min score
    successors = game.successors()
    best_score, best_action = -infinity, successors[0][0]
    for (action, state) in successors:
        score = min_value(state, player, max_depth, -infinity, infinity, eval_function, 0)
        if score > best_score:
            best_score, best_action = score, action
    
    return best_action
