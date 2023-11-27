*** Settings ***
Resource    ./keywords.robot

*** Test Cases ***
General Store Application
    Open general application
    Select country
    Enter first name
    Select Gender
    Click on Lets shop
    Click on add to cart
    Go to cart
    Click on checkbox
