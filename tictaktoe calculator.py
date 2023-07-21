import time

start_time = time.time()

CROSS = 1
CIRCLE = -1
EMPTY = 0
STILL_GOING = 6

def evaluate(position):
    if (position[0] == CROSS and position[1] == CROSS and position[2] == CROSS) or \
       (position[3] == CROSS and position[4] == CROSS and position[5] == CROSS) or \
       (position[6] == CROSS and position[7] == CROSS and position[8] == CROSS) or \
       (position[0] == CROSS and position[3] == CROSS and position[6] == CROSS) or \
       (position[1] == CROSS and position[4] == CROSS and position[7] == CROSS) or \
       (position[2] == CROSS and position[5] == CROSS and position[8] == CROSS) or \
       (position[0] == CROSS and position[4] == CROSS and position[8] == CROSS) or \
       (position[6] == CROSS and position[4] == CROSS and position[2] == CROSS):
        return CROSS
    elif (position[0] == CIRCLE and position[1] == CIRCLE and position[2] == CIRCLE) or \
         (position[3] == CIRCLE and position[4] == CIRCLE and position[5] == CIRCLE) or \
         (position[6] == CIRCLE and position[7] == CIRCLE and position[8] == CIRCLE) or \
         (position[0] == CIRCLE and position[3] == CIRCLE and position[6] == CIRCLE) or \
         (position[1] == CIRCLE and position[4] == CIRCLE and position[7] == CIRCLE) or \
         (position[2] == CIRCLE and position[5] == CIRCLE and position[8] == CIRCLE) or \
         (position[0] == CIRCLE and position[4] == CIRCLE and position[8] == CIRCLE) or \
         (position[6] == CIRCLE and position[4] == CIRCLE and position[2] == CIRCLE):
        return CIRCLE
    elif EMPTY not in position:
        return EMPTY
    else:
        return STILL_GOING

def max(a, b):
    if a < b:
        return b
    return a

def negamax(position, alpha, beta, turn):
    result = evaluate(position)
    if result != STILL_GOING:
        return turn if result == CROSS else (-turn if result == CIRCLE else 0)
    best_score = -1
    for i in range(9):
        if position[i] == EMPTY:
            new_position = position[:]
            new_position[i] = turn
            score = -negamax(new_position, -beta, -alpha, -turn)
            best_score = max(best_score, score)
            alpha = max(alpha, score)
            if alpha >= beta:
                break
    return best_score

if __name__ == "__main__":
    x = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]
    print(negamax(x, -1, 1, CROSS))
    end_time = time.time()
    duration = (end_time - start_time) * 1000
    print(f"Time taken: {duration:.2f} ms")
