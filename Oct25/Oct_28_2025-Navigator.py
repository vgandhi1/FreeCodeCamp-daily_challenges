
"""
Navigator
On October 28, 1994, Netscape Navigator was released, helping millions explore the early web.

Given an array of browser commands you executed on Netscape Navigator, return the current page you are on after executing all the commands using the following rules:

You always start on the "Home" page, which will not be included in the commands array.
Valid commands are:
"Visit Page": Where "Page" is the name of the page you are visiting. For example, "Visit About" takes you to the "About" page. When you visit a new page, make sure to discard any forward history you have.
"Back": Takes you to the previous page in your history or stays on the current page if there isn't one.
"Forward": Takes you forward in the history to the page you came from or stays on the current page if there isn't one.
For example, given ["Visit About Us", "Back", "Forward"], return "About Us".
"""
def navigate(commands):
    
    current_page_idx = []
    for idx in commands:
        if idx in ("Back", "Forward"):
            current_page_idx.append(idx)
        else:
            val = idx.split(" ", 1)[1]  # get page name after "Visit "
            current_page_idx.append(val)
    

    index = 0
    page_History = ['Home'] 
    #current_page
    for page in (current_page_idx):
        
        if page not in ("Back", "Forward"):
       
            
            page_History = page_History[:index + 1] 
            page_History.append(page)
            index += 1
        elif page == "Back":
            if index > 0:
                [index]
                index -= 1

        elif page == "Forward":
            if index < len(page_History) - 1:
                [index]
                index += 1 

    return page_History[index]

print(navigate(["Visit About Us", "Back", "Forward"]))

"""
Passed:1. navigate(["Visit About Us", "Back", "Forward"]) should return "About Us".
Passed:2. navigate(["Forward"]) should return "Home".
Passed:3. navigate(["Back"]) should return "Home".
Passed:4. navigate(["Visit About Us", "Visit Gallery"]) should return "Gallery".
Passed:5. navigate(["Visit About Us", "Visit Gallery", "Back", "Back"]) should return "Home".
Passed:6. navigate(["Visit About", "Visit Gallery", "Back", "Visit Contact", "Forward"]) should return "Contact".
Passed:7. navigate(["Visit About Us", "Visit Visit Us", "Forward", "Visit Contact Us", "Back"]) should return "Visit Us".
"""


def navigate(commands):
    current = "Home"
    back_stack = []
    forward_stack = []

    for cmd in commands:
        if cmd == "Back":
            if back_stack:
                forward_stack.append(current)
                current = back_stack.pop()
        elif cmd == "Forward":
            if forward_stack:
                back_stack.append(current)
                current = forward_stack.pop()
        elif cmd.startswith("Visit "):
            page = cmd[6:]  # everything after "Visit "
            back_stack.append(current)
            current = page
            forward_stack.clear()
        else:
            # Ignore invalid commands (optional)
            pass

    return current

# Examples
print(navigate(["Visit About Us", "Back", "Forward"]))  # About Us
print(navigate(["Visit About", "Visit Gallery", "Back", "Visit Contact", "Forward"]))  # Contact

print(navigate(["Visit About Us", "Visit Visit Us", "Forward", "Visit Contact Us", "Back"]))
