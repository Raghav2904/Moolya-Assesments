*** Settings ***
Library     SeleniumLibrary
Resource   .//Variables.robot


*** Keywords ***
Opening Flipkart
        Open Browser    ${url}  ${browser}
        Maximize Browser Window
        #Click Element    //span[@role="button"]

Moving to Mobile Tab
        Click Element    //a[@aria-label="Mobiles"]

Moving to Electronics Tab
        Mouse Over    //span[@class="_2I9KP_"][1]

Selecting a Mobile
        Click Element    //a[@title="Motorola g8 power lite"]
        Wait Until Element Is Visible    //div[@class="_4rR01T"]
        Click Element   //div[@class="_4rR01T"]

Add to cart
        ${current_windows}      Get Window Handles
        Switch Window   ${current_windows}[-1]
        Click Button    //button[@class="_2KpZ6l _2U9uOA _3v1-ww"]

Verifying item in the cart
        Page Should Contain    ${mobile_name}