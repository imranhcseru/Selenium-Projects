def state_tax(state,money,state_tax_calc):
	fedral_tax = .10
	total_money = money-money*fedral_tax;
	state_box = {'ca':10,'tx':8,'ny':9,'la':9,'sk':10}
	if state in state_box:
		return state_tax_calc(state_box[state],total_money)
	else:
		return None

def state_tax_calc(state_tax,total_money):
	net_money = total_money-(total_money*state_tax/100)
	return net_money
	
state = str(input("Enter state:"))
money_remain = state_tax(state,100000,state_tax_calc)
print(money_remain)