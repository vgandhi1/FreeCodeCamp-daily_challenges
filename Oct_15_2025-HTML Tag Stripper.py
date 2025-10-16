"""
Given a string of HTML code, remove the tags and return the plain text content.

The input string will contain only valid HTML.
HTML tags may be nested.
Remove the tags and any attributes.
For example, '<a href="#">Click here</a>' should return "Click here".
"""
import re

def strip_tags(html):

    clean = re.compile('<.*?>')
    return re.sub(clean, '', html)
"""
1. strip_tags('<a href="#">Click here</a>') should return "Click here".
Passed:2. strip_tags('<p class="center">Hello <b>World</b>!</p>') should return "Hello World!".
Passed:3. strip_tags('<img src="cat.jpg" alt="Cat">') should return an empty string ("").
Passed:4. strip_tags('<main id="main"><section class="section">section</section><section class="section">section</section></main>') should return sectionsection.
"""
