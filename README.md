# webcrawler

Our code follows a basic loop: Visit a page (starting at our homepage), search it for secret flags, gather all links on the page (exclusive to the fakebook domain). After that, we are done with a page, add it to our visited list, and add all nonvisited gathered links to the to_visit queue. We repeat this for all pages until we have all five flags or run out of pages to visit.

The HTML parser was a simple extension of the built in python library. We added a flag to mark when we found an H2 that we should grab flags from (of the class secret_flag). It was only added if the flag hasn't been seen before.
