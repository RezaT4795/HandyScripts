from Modules.evaluation_modules import input_check, id_split, digit_places, id_evaluation

length = False
while length == False:
    national_id = input("Enter code:")
    length = input_check(national_id)
ctrl_num = id_split(national_id)[9] # This is the controlling digit in ID.
places = digit_places()

if id_evaluation(id_split(national_id)[0:9], places, ctrl_num) == True:
    print("%s\nVALID." % national_id)
else:
    print("%s\nINVALID." % national_id)

    

