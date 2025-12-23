"""
Re: Fwd: Fw: Count
Given a string representing the subject line of an email, determine how many times the email has been forwarded or replied to.

For simplicity, consider an email forwarded or replied to if the string contains any of the following markers (case-insensitive):

"fw:"
"fwd:"
"re:"
Return the total number of occurrences of these markers.

"""
def email_chain_count(subject):
    markers =["fw:", "fwd:", "re:"]
    counter = 0
    # words_subject = subject.lower().split(" ")
    words_subject = subject.lower()

    counter = sum(words_subject.count(marker) for marker in markers)

    # for word in words_subject:
    #     if word in markers:
    #         counter += 1


    return counter

print(email_chain_count("re:Ref:fw:re:review:FW:Re:fw:report:Re:FW:followup:re:summary:Fwd:Re:fw:NextStep:RE:FW:re:Project:Fwd:Re:fw:Notes:RE:re:Update:FWD:Re:fw:Summary"))

"""
Tests
Passed:1. email_chain_count("Re: Meeting Notes") should return 1.
Passed:2. email_chain_count("Meeting Notes") should return 0.
Passed:3. email_chain_count("Re: re: RE: rE: Meeting Notes") should return 4.
Passed:4. email_chain_count("Re: Fwd: Re: Fw: Re: Meeting Notes") should return 5.
Failed:5. email_chain_count("re:Ref:fw:re:review:FW:Re:fw:report:Re:FW:followup:re:summary:Fwd:Re:fw:NextStep:RE:FW:re:Project:Fwd:Re:fw:Notes:RE:re:Update:FWD:Re:fw:Summary") should return 23.
"""
