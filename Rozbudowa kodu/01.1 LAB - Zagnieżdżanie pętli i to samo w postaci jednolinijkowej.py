

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

# wyświetlenie tupletu lotniska start i stop
flying = [(start, stop) for start in ports for stop in ports]
print(flying)
print(len(flying))

# wyeliminowanie lotnisk jeśli są takie same
flying = [(start, stop) for start in ports for stop in ports if start != stop ]
print(flying)
print(len(flying))

# Wyeliminowanie lotnisk jeśli a = b i b = a
flying = [(start, stop) for start in ports for stop in ports if start < stop ]
print(flying)
print(len(flying))

