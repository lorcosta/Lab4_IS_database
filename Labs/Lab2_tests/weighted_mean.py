print 'Welcome! Insert your score and the credits of the relative exam:'
print 'If you want to stop inserting scores type "-1"'
num = 0
den = 0
while True:
    score = raw_input('Insert score:')
    credit = raw_input('Insert credit:')
    if score == '-1' or credit == '-1':
        break
    if not score.isdigit() or not credit.isdigit():
        print "Wrong input!"
        continue
    if not int(score) in range(0, 32):
        print "Write a score between 0 and 31"
        continue
    score = float(score)
    credit = float(credit)
    num += (score * credit)
    den += credit
mean = num/den
print 'Your mean is ', mean

