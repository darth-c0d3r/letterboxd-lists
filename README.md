## Aim

This code can be used to take union or intersection of the lists on letterboxd.
In my opinion, these features can be very useful for finding movies belonging to meaningful sets.
For example: We can use it to find movies that are in the watchlists of many different people which can be used to decide the movies to watch in a group.

## How to use
1. Update the list of urls of the lists or watchlists you want to use.
2. Use `python3 main.py u` for union and `python3 main.py i` for intersection of the lists.

## Bugs
1. Different films with same names are not considered separately. Year of the film not considered.
2. Login feature not added. Only works for public lists.
3. Seems very slow. Bottleneck seems to be getting the page URL using requests. Can't help.:/
