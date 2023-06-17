
ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

flying = ((start, stop) for start in ports for stop in ports)
count = 0
for (start, stop) in flying:
    print('{} - {}'.format(start,stop))
    count += 1

print(count)


print('*'*50)

flying = ((start, stop) for start in ports for stop in ports if start != stop )
count = 0
for (start, stop) in flying:
    print("{} - {}".format(start,stop))
    count += 1

print(count)

print('*'*50)


flying = [(start, stop) for start in ports for stop in ports if start < stop ]
count = 0
for (start, stop) in flying:
    print("{} - {}".format(start,stop))
    count += 1

print(count)





