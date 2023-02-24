''' Phasmophobia '''
def phasmo():
    ''' อยากเร่นเกม '''
    evidence = [input() for _ in range(3)]
    found = input()
    supernatural = input()

    ghost = {'EMF Level 5': ['Banshee', 'Demon', 'Jinn', 'Oni', 'Phantom', 'Revenant', 'Shade'], 
            'Ghost Writing': ['Demon', 'Oni', 'Revenant', 'Shade', 'Spirit', 'Yurei'], 
            'Fingerprints': ['Banshee', 'Poltergeist', 'Revenant', 'Spirit', 'Wraith'], 
            'Spirit Box': ['Demon', 'Jinn', 'Mare', 'Oni', 'Poltergeist', 'Spirit', 'Wraith', 'Yurei'], 
            'Ghost Orb': ['Jinn', 'Mare', 'Phantom', 'Poltergeist', 'Shade', 'Yurei']}
    if not evidence:
        total = set()
        for keys in ghost:
            total = total
            set(ghost[keys])
        print(*sorted(total), sep='\n')
        return
    if len(evidence) == 1:
        ghost
