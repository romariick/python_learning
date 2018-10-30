
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy', 'blue']

for q, a in zip(questions, answers):
    print 'Whate is your {0} ? It is {1}'.format(q, a)


keyvalue = {"a => " : "value a", "b => " : "value b"}

for k, v in keyvalue.iteritems():
    print k, v
