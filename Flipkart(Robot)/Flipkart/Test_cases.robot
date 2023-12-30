*** Settings ***
Library     SeleniumLibrary
Resource   .//Key_words.robot
Suite Setup     Opening Flipkart

*** Test Cases ***
Flipkart
        Moving to Mobile Tab
        Moving to Electronics Tab
        Selecting a Mobile
        Add to cart
        Verifying item in the cart




