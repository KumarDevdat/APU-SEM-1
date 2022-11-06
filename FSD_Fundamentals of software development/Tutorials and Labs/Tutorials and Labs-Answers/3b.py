
games = ['Football', 'Tennis', 'Rugby']
games.append('Squash')
for game in games:
    print(game)
#These lines will not work becuase you can append only one element
games = ['Football', 'Tennis', 'Rugby']
games.append('Squash', 'Netball')
for game in games:
    print(game)
# untill here
# remove or commet the line to run rest of the code.
games = ['Football', 'Tennis', 'Rugby']
games.append('Squash')
games.append('Netball')
for game in games:
    print(game)

firstList = ['Football', 'Tennis', 'Rugby']
secondList = ['Squash','Netball','Cricket', 'Volleyball']
firstList.append(secondList)
for game in firstList:
    print(game)

firstList = ['Football', 'Tennis', 'Rugby']
secondList = ['Squash','Netball','Cricket', 'Volleyball']
secondList.append(firstList)
for game in secondList:
    print(game)

firstList = ['Football', 'Tennis', 'Rugby']
secondList = ['Squash','Netball','Cricket', 'Volleyball']
secondList.append(firstList)
for game in firstList:
    print(game)

firstList = ['Football', 'Tennis', 'Rugby']
secondList = ['Squash','Netball','Cricket', 'Volleyball']
for game in secondList:
    firstList.append(game)

for game in firstList:
    print(game)

firstList = ['Football', 'Tennis', 'Rugby']
secondList = ['Squash','Netball','Cricket', 'Volleyball']
firstList.extend(secondList)
for game in firstList:
    print(game)

firstList = ['Football', 'Tennis', 'Rugby']
secondList = ['Squash','Netball','Cricket', 'Volleyball']
firstList.extend(secondList)
firstList.sort()
for game in firstList:
    print(game)

firstList = ['Football', 'Tennis', 'Rugby']
secondList = ['Squash','Netball','Cricket', 'Volleyball']
firstList.extend(secondList)
firstList.sort(reverse=True)
for game in firstList:
    print(game)

