now = int (input ("Какой на дворе год: "))
research = now % 4
research2 = now % 100
research3 = now % 400
if research != 0:
	print ( now, "- год, как год" )
else:
	if research2 != 0:
		print ( now, "- cложный год" )
	else:
		if research3 == 0:
			print ( now, "- cложный год" )
		else:
		    print ( now, "- год, как год" )	
