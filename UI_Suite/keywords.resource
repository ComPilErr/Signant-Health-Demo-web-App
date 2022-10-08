***Settings***
Documentation    Please select the server path:port as a first parameter and 
...              a chromedriver version as a second argument 

Library    ChromeLib.py    http://127.0.0.1:6969    90.0.4430.24

*** Variables ***
${FirstName}    Paul
${Password}    12345
${FamilyName}    Sablin
${PhoneNumber}    1234567
${LoginTitle}    User Information - Demo App
${WrongCredsTitle}    Login Failure - Demo App
${RegisterTitle}    Register - Demo App
*** Keywords ***

Login With Wrong Creds
    Open Page
    Click On Login
    Fill Login Username    ${Password}
    Fill Login Passw    ${FirstName}
    Perform Login
    Catch Wrong Creds Alert
    ${title}=    Get Title
    Should Be Equal    ${title}    ${WrongCredsTitle}

Login With Custom Wrong Creds
    [Arguments]    ${uname}    ${upassw}
    Open Page
    Click On Login
    Fill Login Username    ${uname}
    Fill Login Passw    ${upassw}
    Perform Login
    Catch Wrong Creds Alert
    ${title}=    Get Title
    Should Be Equal    ${title}    ${WrongCredsTitle}


Login With Custom Creds
    [Arguments]    ${uname}    ${upassw}    ${ulstname}    ${uphone}    ${ufstname}
    Open Page
    Click On Login
    Fill Login Username    ${uname}
    Fill Login Passw    ${upassw}
    Perform Login
    ${lstname}=    Get Lastname
    Should Be Equal    ${lstname}    ${ulstname}
    ${phone}=    Get Phone
    Should Be Equal    ${phone}    ${uphone}
    ${fstname}=    Get Firstname
    Should Be Equal    ${fstname}    ${ufstname}
    ${title}=    Get Title
    Should Be Equal    ${title}    ${LoginTitle}
    Click On Logout


Login With Default Creds
    Open Page
    Click On Login
    Fill Login Username    ${FirstName}
    Fill Login Passw    ${Password}
    Perform Login
    ${lstname}=    Get Lastname
    Should Be Equal    ${lstname}    ${FamilyName}
    ${phone}=    Get Phone
    Should Be Equal    ${phone}    ${PhoneNumber}
    ${fstname}=    Get Firstname
    Should Be Equal    ${fstname}    ${FirstName}
    ${title}=    Get Title
    Should Be Equal    ${title}    ${LoginTitle}
    Click On Logout

Register User With Default Creds
    Open Page
    Click On Register
    Fill Register Username    ${FirstName}
    Fill Register Passw    ${Password}
    Fill Register First Name    ${FirstName}
    Fill Register Family Name    ${FamilyName}
    Fill Register Phone Number    ${PhoneNumber}
    Perform Register
    ${title}=    Get Title
    Should Be Equal    ${title}    ${RegisterTitle}


Register User With Custom Creds
    [Arguments]    ${uname}    ${upassw}    ${ulstname}    ${uphone}    ${ufstname}
    Open Page
    Click On Register
    Fill Register Username    ${uname}
    Fill Register Passw    ${upassw}
    Fill Register First Name    ${ufstname}
    Fill Register Family Name    ${ulstname}
    Fill Register Phone Number    ${uphone}
    Perform Register
    ${title}=    Get Title
    Should Be Equal    ${title}    ${RegisterTitle}
