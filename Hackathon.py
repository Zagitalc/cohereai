import cohere
import json
from cohere.classify import Example
co = cohere.Client('lFHIj2hW8tNMFa1oDPUspENDrDHAWDV12ob8YMvO')

examples = [
    Example("you are hot trash", "Toxic"),
    Example("go to hell", "Toxic"),
    Example("get rekt moron", "Toxic"),
    Example("get a brain and use it", "Toxic"),
    Example("say what you mean, you jerk.", "Toxic"),
    Example("Are you really this stupid", "Toxic"),
    Example("I will honestly kill you", "Toxic"),
    Example("yo how are you", "Benign"),
    Example("I'm curious, how did that happen", "Benign"),
    Example("Try that again", "Benign"),
    Example("Hello everyone, excited to be here", "Benign"),
    Example("I think I saw it first", "Benign"),
    Example("That is an interesting point", "Benign"),
    Example("I love this", "Benign"),
    Example("We should try that sometime", "Benign"),
    Example("You should go for it", "Benign"),
    Example("", "Toxic"),
    Example("", "Toxic"),
    Example("", "Toxic"),
    Example("", "Toxic"),
    Example("", "Toxic"),
    Example("", "Toxic"),
    Example("", "Toxic"),
    Example("", "Toxic"),
    Example("", "Toxic"),
    Example("", "Toxic"),
    Example("", "Toxic"),
    Example("", "Toxic"),
    Example("", "Toxic"),
    Example("", "Toxic"),
    Example("", "Toxic"),
    Example("",  "Toxic"),
    Example("", "Benign"),
    Example("", "Benign"),
    Example("", "Benign"),
    Example("", "Benign"),
    Example("", "Benign"),
    Example("", "Benign"),
    Example("", "Benign"),
    # zac
    Example("I appreciate the video.", "Benign"),
    Example("Happy birthday will! ", "Benign"),
    Example(
        "You are a wise man, Will. We all felt with You during those days. ", "Benign"),
    Example("Fuck you", "Toxic"),
    Example("Peace to you man", "Benign"),
    Example("Idk if ur reading this but ur amazing dude. It’s just ur family dude they don’t deserve u they are pulling u down.", "Benign"),
    Example("Love you Will and praying for you", "Benign"),
    Example("It’s not how you fall, it’s how you get back up", "Benign"),
    Example(
        "It takes 20 years to build a reputation and five minutes to ruin it", "Toxic"),
    Example("A mistake? That’s a career defining moment that will not easily be forgotten—ever.", "Toxic"),
    Example("This is EXACTLY how he apologizes when he fuxks up. It's eerie.", "Toxic")
]

inputs = [
    "this game sucks, you suck",
    "stop being a dumbass",
    "Let's do this once and for all",
    "This is coming along nicely"
]

response = co.classify(
    model='large',
    inputs=inputs,
    examples=examples
)
f = open('dataset.json')
for data in f:
    for newData in data:
        print(newData)
inputs = open
# response = co.classify(
# model='medium',
# inputs=inputs,
# examples=examples)

# print(response.classifications)
