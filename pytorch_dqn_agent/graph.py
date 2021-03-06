import matplotlib.pyplot as plt
import csv

with open("reward.txt", 'rU') as f:
    res = csv.reader(f, delimiter=",")
    cur_win_count, cur_loss_count, cur_tie_count = 0, 0, 0

    percetage_win_so_far, percetage_loss_so_far, percetage_tie_so_far = [], [], []
    cur_win_prob_count, cur_loss_prob_count, cur_tie_prob_count = 0, 0, 0

    game_count = 0

    for row in res:
        row = ''.join(row)  # converts list to string
        game_count = game_count + 1  # game counter
        if row == "1":
            cur_win_count = cur_win_count + 1
            cur_win_prob_count = cur_win_count / game_count
            percetage_win_so_far.append(cur_win_prob_count)

            cur_loss_prob_count = cur_loss_count / game_count
            percetage_loss_so_far.append(cur_loss_prob_count)

            cur_tie_prob_count = cur_tie_count / game_count
            percetage_tie_so_far.append(cur_tie_prob_count)
        elif row == "-1":
            cur_loss_count = cur_loss_count + 1

            cur_loss_prob_count = cur_loss_count / game_count
            percetage_loss_so_far.append(cur_loss_prob_count)

            cur_tie_prob_count = cur_tie_count / game_count
            percetage_tie_so_far.append(cur_tie_prob_count)

            cur_win_prob_count = cur_win_count / game_count
            percetage_win_so_far.append(cur_win_prob_count)
        else:  # row == "0"
            cur_tie_count = cur_tie_count + 1

            cur_tie_prob_count = cur_tie_count / game_count
            percetage_tie_so_far.append(cur_tie_prob_count)

            cur_win_prob_count = cur_win_count / game_count
            percetage_win_so_far.append(cur_win_prob_count)

            cur_loss_prob_count = cur_loss_count / game_count
            percetage_loss_so_far.append(cur_loss_prob_count)
    cnt = range(game_count)
    # plots all 3 functions on same graph
    plt.title('Score Summary')
    plt.plot(cnt, percetage_win_so_far, "b", cnt,
             percetage_loss_so_far, "r", cnt, percetage_tie_so_far, "y")
    plt.legend(('Win', 'Loss', 'Tie'),
               loc='upper right')
    plt.ylabel('Win%,Loss%,Tie%')
    plt.xlabel('Episode')
    plt.show()
