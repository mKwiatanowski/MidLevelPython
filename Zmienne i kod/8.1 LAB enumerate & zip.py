
projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']


for p, l in list(zip(projects,leaders)):
    print('The leader of %s is %s ' %(p,l))


dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for p, l, d in list(zip(projects,leaders,dates)):
    print('The leader of %s started %s is %s' % (p,d,l))


for n, (p,l,d) in enumerate(zip(projects,leaders,dates)):
    print("{} - The leader of {} starter {} os {}".format(n+1,p,d,l))



