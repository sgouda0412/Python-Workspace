from prettytable import PrettyTable

myTable = PrettyTable(['Footballer', 'Position', 'Goals', 'Assists', 'Clean Sheets'])

myTable.add_row(['Giroud', 'ST', '1', '0', '0'])
myTable.add_row(['Werner', 'ST', '4', '2', '0'])
myTable.add_row(['Ziyech', 'RW', '1', '3', '0'])
myTable.add_row(['Havertz', 'CM', '1', '1', '1'])
myTable.add_row(['Kante', 'CM', '0', '1', '3'])
myTable.add_row(['Mount', 'CM', '1', '1', '3'])
myTable.add_row(['Chilwell', 'LB', '2', '2', '4'])
myTable.add_row(['Silva', 'CB', '1', '0', '5'])
myTable.add_row(['Zouma', 'CB', '3', '0', '4'])
myTable.add_row(['James', 'RB', '1', '2', '4'])
myTable.add_row(['Mendy', 'GK', '0', '0', '7'])

print(myTable)
