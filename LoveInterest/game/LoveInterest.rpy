init python:
    ## This is used for creating a LoveInterest. The text after  "__init__(self," tells us what are the variables the LoveInterest have.
    ## You can think of LoveInterest variables as the same thing as flags, except the LoveInterest owns them.
    ## For example: In "name = ???", we're saying LoveInterest has a "name" variable.
    ## The equals after name means we're setting a default value.
    class LoveInterest:
        def __init__(self, name = "???", bloodType = "???", major = "???", affection = 0, imageName = ""):
            self.name = name
            self.bloodType = bloodType
            self.major = major
            ## We're setting the starting affection to 0.
            self.affection = affection
            #The portraits are located in game/images/characters folder
            self.imageName = "characters/"+ imageName + ".png"

## This is how a LoveInterest Class is created.
## We're setting the name, bloodType, major, affection, and imageName.
default girl1 = LoveInterest(name="Zeil", bloodType="A", major ="CS", affection=0, imageName="zeil delighted")
## Another way of writing the code above is: (This is what I used in the Vlog)
## default girl1 = LoveInterest("Zeil", "A", "CS", 4, "zeil delighted")
## It's missing the "name=", "bloodType=", "major=", "affection=" and "imageName=".
# As long as it is in the same order, it will work.
## I don't suggest using this ^. It's confusing if you're new to coding.


## In this code, we're creating boy1 with an imageName.
default boy1 = LoveInterest(imageName = "yuki smile")
## Since we didn't specify the name and the default value is None, boy1.name is ???.
## The code above is how we usually want to code the LoveInterest.
## Then through the game, we can set the variables. Please check the script.rpy for more details.

## The selectedCharacter is the loveInterest we will display on the stats screen.
## Please check the custom_screens.rpy for more details
default selectedCharacter = girl1