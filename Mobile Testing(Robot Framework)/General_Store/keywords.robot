*** Settings ***
Library     AppiumLibrary
Resource    ./variables.robot

*** Keywords ***
Open general application
        Open Application    http://localhost:4723/wd/hub    devicename=${device_name}     platformName=${platform_name}  appPackage=${app_package}  appActivity=${app_activity}
Select country
        Wait Until Element Is Visible    com.androidsample.generalstore:id/spinnerCountry
        Click Element    com.androidsample.generalstore:id/spinnerCountry
        sleep   10
        FOR    ${i}     IN RANGE    0   13
            Swipe    479    2024    500    701
        END
        Click Element   //android.widget.TextView[@text='India']
Enter first name
        Input Text    com.androidsample.generalstore:id/nameField    Raghav
Select Gender
        Click Element    com.androidsample.generalstore:id/radioMale
Click on Lets shop
        Click Element    com.androidsample.generalstore:id/btnLetsShop
Click on add to cart
        Wait Until Element Is Visible    //android.widget.TextView[@bounds='[540,971][1002,1009]']
        Click Element    //android.widget.TextView[@bounds='[540,971][1002,1009]']
Go to cart
        Click Element    com.androidsample.generalstore:id/appbar_btn_cart
        Wait Until Element Is Visible    //android.widget.CheckBox[@bounds='[44,1650][1019,1738]']
Click on checkbox
        Click Element    //android.widget.CheckBox[@bounds='[44,1650][1019,1738]']
