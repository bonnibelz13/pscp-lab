''' MissingCard I '''
def miss():
    ''' find the missing card in deck '''
    rank = ['S', 'H', 'D', 'C']
    rank_a_to_2 = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    deck = []
    for i in range(len(rank_a_to_2)):
        for j in range(len(rank)):
            deck += [rank_a_to_2[i] + rank[j]]

    card_input = []
    while len(card_input) != 51:
        txt = input()
        card_input.append(txt)
    print(*(set(deck) - set(card_input)))
miss()
