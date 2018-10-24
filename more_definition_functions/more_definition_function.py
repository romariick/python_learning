
def more_function(prompt, retries = 4, complaint = 'Yes or not, please'):

    while True:
        ok = raw_input(prompt)
        if(ok in ('y', 'yes', 'ye')):
            return True
        if(ok in ('n', 'no')):
            return False
        retries = retries - 1
        if retries < 0 :
            raise IOError('refusenik user')
        print complaint


more_function('Do you really want to quit?', 4, "Yes")