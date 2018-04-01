# Challenge Task 1 of 3
# I think it's a good idea for you to experiment with sets since they're a very useful part of Python.

# Start by creating a set variable named songs that has three song titles in it. You can use any titles you want, just make sure they're three different strings.

songs = set(["Fire Stone", "Good Riddance", "Don't Look Back in Anger"])



# Challenge Task 2 of 3
# Awesome. Now use the .add() method to add the title "Treehouse Hula" to songs.

songs.add("Treehouse Hula")



# Challenge Task 3 of 3
# Alright, and last task. Use .update() to add the following two sets to your songs set.

# {"Python Two-Step", "Ruby Rhumba"}

# {"My PDF Files"}

songs.update({"Python Two-Step", "Ruby Rhumba"}, {"My PDF Files"})

