list_of_mtn_numbers = ["0803", "0806", "0810", "0813", "0814", "0816", "0903",
       "0906", "0913", "0916", "0702", "0703", "0704", "0706"]

list_of_glo_numbers = ["0915", "0905", "0815", "0811", "0807", "0805"]

list_of_airtel_numbers = ["0701", "0708", "0802", "0808", "0812",
                          "0901", "0902", "0904", "0907", "0912"]

list_of_etisalat_numbers = ["0909", "0908", "0817", "0818", "0809"]

users_input = input("Enter your first four numbers: ")
if users_input in list_of_mtn_numbers:
    print("Your number is MTN")
elif users_input in list_of_glo_numbers:
    print("Your number is GLO")
elif users_input in list_of_airtel_numbers:
    print("Your number is AIRTEL")
elif users_input in list_of_etisalat_numbers:
    print("Your number is ETISALAT")
else:
    print("Sorry, Invalid number")


