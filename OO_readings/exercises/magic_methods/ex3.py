'''
- class Candidate
    - needs a name ('first last')
    - instance var `votes` assigned to 0 -> keep track of votes they get
    - needs a __iadd__ method to add votes

- class Election?
    - needs a list of candidates
    - `results` instance method -> returns given output, access candidates votes

'''

class Candidate:
    def __init__(self, full_name):
        self.full_name = full_name
        self.votes = 0

    def __str__(self):
        return self.full_name
    
    def __iadd__(self, vote):
        if not isinstance(vote, int):
            return NotImplemented
        self.votes += vote
        return self

class Election:
    @staticmethod
    def _get_percentage(part, total):
        return f'{round((part / total) * 100, 2)} %'
    
    def __init__(self, candidates_set):
        self.candidates = candidates_set
    
    def _get_winner(self):
        votes = 0
        winner = None

        for candidate in self.candidates:
            if candidate.votes > votes:
                winner, votes = candidate, candidate.votes
        
        return winner
    
    def _get_total_votes(self):
        votes = 0
        for candidate in self.candidates:
            votes += candidate.votes
        
        return votes

    def results(self):
        for candidate in self.candidates:
            print(f'{candidate}: {candidate.votes} votes')
        print()

        total_votes = self._get_total_votes()
        winner = self._get_winner()
        winning_votes = winner.votes

        print(f'{winner} won: '
              f'{self._get_percentage(winning_votes, total_votes)} of votes')
    

mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()q

# Output:
# Mike Jones: 3 votes
# Susan Dore: 4 votes
# Kim Waters: 1 votes

# Susan Dore won: 50.0% of votes