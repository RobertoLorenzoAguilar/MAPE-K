*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${URL}  https://wokwi.com/projects/425271459919724545
${XPATH}  //*[@id="simple-tabpanel-0"]/div/div[1]/pre
${BUTTON_XPATH}  /html/body/div[1]/main/div/div/div[3]/div[2]/div/div[2]/div[2]/div[1]/button

*** Test Cases ***
Leer Datos De Un Elemento
   Open Browser  ${URL}  chrome
    # Esperar hasta que el botón esté visible antes de hacer clic
    Sleep    2s  # Espera para ver el resultado
    Execute JavaScript    (document.evaluate('/html/body/div[1]/main/div/div/div[3]/div[2]/div/div[2]/div[2]/div[1]/button', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue || console.error('No se encontró el botón'))?.click();
    Wait Until Element Is Visible  ${XPATH}  10s
    Sleep    240s  # Espera para ver el resultado
    ${value}=    Execute JavaScript    return document.evaluate('${XPATH}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue?.textContent;
    Log    El valor obtenido es: ${value}
    ${contenido}  Get Text  ${XPATH}
    Log  ${contenido}


