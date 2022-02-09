
class bowlingGame():

    def __init__(self, rolls):
        self.rolls = rolls
        self.score = 0

    def getScoreFromSign(self, charArg):
        ret = 0
        if charArg == 'X':
            ret = 10
        elif charArg == '':
            ret = 10
        elif charArg == '/':
            ret = 10
        elif charArg == '-':
            ret = 0
        else:
            ret = int(charArg)
        return ret

    def calculateScore(self):
        # Score and list of rolls to calculate the score from the rolls
        score = 0
        bowlingscores = self.rolls
        
        # Magic Numbers
        LAST_SPARE_OFFSET = 1
        LAST_STRIKE_OFFSET = 2
        GAME_SIZE = len(bowlingscores)
        GAME_SIZE_END_OFFSET = 1
        ALLPINS = 10

        # Score definitions
        SPARE = '/'
        MISS = '-'
        STRIKE = 'X'
        
        # Booleans to keep track of bonusrolls.
        isSpareBonusRoll = False
        isStrikeBonusRoll = False

        # Loop through all rolls and sum them up. Special handling needed for strikes and spares.
        for i in range(GAME_SIZE):
            currentRoll = bowlingscores[i]
            if currentRoll == MISS:
                # Miss, do nothing.
                pass

            # Current roll is a spare. Strike gives a bonus of the the next throw.
            elif currentRoll == SPARE:
                bonus1 = 0
                if isSpareBonusRoll == True or isStrikeBonusRoll == True:
                    # Bonusroll has been handled. Do nothing
                    pass
                else:
                    prevRoll = self.getScoreFromSign(bowlingscores[i-1])
                    nextRoll = self.getScoreFromSign(bowlingscores[i+1])
                    bonus1 = nextRoll

                # Check if the spare is the last spare of the game meaning the last roll is a bonus roll.
                if i+LAST_SPARE_OFFSET == GAME_SIZE - GAME_SIZE_END_OFFSET:
                    isSpareBonusRoll = True
                score = score - prevRoll + ALLPINS + bonus1

            # Current roll is a strike. Strike gives a bonus of the simple sum of the two next throws.
            elif currentRoll == STRIKE:
                bonus1 = 0
                bonus2 = 0
                if isSpareBonusRoll == True or isStrikeBonusRoll == True:
                    pass
                else:
                    nextRoll = self.getScoreFromSign(bowlingscores[i+1])
                    nextNextRoll = self.getScoreFromSign(bowlingscores[i+2])
                    bonus1 = nextRoll
                    bonus2IsSpare = bowlingscores[i+2]
                    if bonus2IsSpare == SPARE:
                        bonus2 = ALLPINS - bonus1
                    else:
                        bonus2 = nextNextRoll
                # Check if the spare is the last strike of the game meaning the last two rolls are bonus rolls.
                if i+LAST_STRIKE_OFFSET == GAME_SIZE - GAME_SIZE_END_OFFSET:
                    isStrikeBonusRoll = True
                    score = score + ALLPINS + bonus1 + bonus2
                else:
                    if isSpareBonusRoll == True or isStrikeBonusRoll == True:
                        # Bonusroll has been handled. Do nothing.
                        pass
                    else:
                        score = score + ALLPINS + bonus1 + bonus2

            else:
                if isSpareBonusRoll == True or isStrikeBonusRoll == True:
                    # Bonusroll has been handled. Do nothing.
                    pass
                else:
                    scoreToAdd = self.getScoreFromSign(bowlingscores[i])
                    score = score + scoreToAdd

        self.score = score

    def getScore(self):
        return self.score

    def getRolls(self):
        return self.rolls

# Defining main function
def main():
    Rolls = ['4', '4', '6', '/', '7', '/', 'X', '8', '/', '1', '5', '6', '/', '3', '5', 'X', '8', '/', 'X']
    Player1Game = bowlingGame(Rolls)
    Player1Game.calculateScore()
    print("Final Score: " + str(Player1Game.getScore()))


if __name__ == '__main__':
    main()
