"""
SpOoKy~CaSe
Given a string representing a variable name, convert it to "spooky case" using the following constraints:

Replace all underscores (_), and hyphens (-) with a tilde (~).
Capitalize the first letter of the string, and every other letter after that. Ignore the tilde character when counting. Make all other letters lowercase.
For example, given hello_world, return HeLlO~wOrLd.
"""
def spookify(boo):
    converted_boo = boo.replace("_","~").replace("-","~")
    spooky_case = []
    idx = 0
    for char in converted_boo:
        if char == "~":
            #spooky_case.append(char)
            spooky_case.append(char)

            continue 
        
        if idx%2 == 0:
            char = char.upper()
        else:
            char = char.lower()

        spooky_case.append(char)
        idx += 1

            

    return "".join(spooky_case)

print(spookify("TRICK-or-TREAT"))
print(spookify("c_a-n_d-y_-b-o_w_l"))
print(spookify("thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts"))


"""
Tests
Passed:1. spookify("hello_world") should return "HeLlO~wOrLd".
Passed:2. spookify("Spooky_Case") should return "SpOoKy~CaSe".
Passed:3. spookify("TRICK-or-TREAT") should return "TrIcK~oR~tReAt".
Passed:4. spookify("c_a-n_d-y_-b-o_w_l") should return "C~a~N~d~Y~~b~O~w~L".
Passed:5. spookify("thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts") should return "ThE~hAuNtEd~HoUsE~iS~fUlL~oF~gHoStS".
"""
