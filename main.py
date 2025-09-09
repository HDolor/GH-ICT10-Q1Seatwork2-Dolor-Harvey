from pyscript import display

restaurant_name='Red Lobster'
owner_name="Bill Darden"
year_established=1968
popular_item_price=3500
has_delivery=True
product_names=['Live Lobster', 'Crab Alfredo' ,"Seafear's Feast", 'Cod New Orleans']
business_hours=['11:00 AM', '10:00 PM','11:00 PM', '9:00 PM']
menu_prices=[595, 1450, 525]
common_allergies=['Fish', 'Crustacean shellfish', 'Milk', 'Eggs', 'Soy']
tax_rate= 0.12

display(f'{restaurant_name}', target='name') 
display(f'By {owner_name} in {year_established}', target='own')
display(f'Opens at: {business_hours[0]}', target='open')
display(f'Closes at: {business_hours[1]} Weekdays, {business_hours[2]} Weekends, {business_hours[3]} Sunday', target='close')
display(f'{product_names[0]}', target='HOT')
display(f'{popular_item_price}', target='hot')
display(f'{product_names[1]}', target='tem0')
display(f'{menu_prices[0]}', target='pr0')
display(f'{product_names[2]}', target='tem1')
display(f'{menu_prices[1]}', target='pr1')
display(f'{product_names[3]}', target='tem2')
display(f'{menu_prices[2]}', target='pr2')
display(f'Possible allergens: {common_allergies[0]}, {common_allergies[1]}, {common_allergies[2]}, {common_allergies[3]}, {common_allergies[4]}', target='all')