hourly = input('Hourly Rate: ')

while hourly != '':
    hourly = float(hourly)
    daily = hourly * 7
    biweekly = daily * 10
    monthly = biweekly * 2
    annually = monthly * 12
    print(f'{"Daily Rate:":>14}{f"${daily:,.2f}":>12}')
    print(f'{"Biweekly Rate:":>14}{f"${biweekly:,.2f}":>12}')
    print(f'{"Monthly Rate:":>14}{f"${monthly:,.2f}":>12}')
    print(f'{"Annual Rate:":>14}{f"${annually:,.2f}":>12}')
    print()
    hourly = input('Enter another hourly rate, or press enter to end session: ')

    
    
