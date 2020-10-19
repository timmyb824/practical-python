# bounce.py
#
# Exercise 1.5

# A rubber ball is dropped from a height of 100 meters and each time it hits the ground, it bounces back up to 3/5 the height it fell. Write a
# program bounce.py that prints a table showing the height of the first 10 bounces.

# my solution
height = 100
bounce_height = height * .60
bounce = 1
num_bounces = 10

while bounce <=  num_bounces:
    print(bounce,  bounce_height)
    bounce = bounce + 1
    bounce_height = round(bounce_height * .60, 4)

# his solution
height = 100
bounce = 1
while bounce <= 10:
    height = height * (3/5)
    print(bounce, round(height, 4))
    bounce += 1
