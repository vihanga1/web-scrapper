import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# loggin system
def logginToSystem(driver, listwidget):
    driver.get("https://www.sample_url_.com")
    listwidget.addItem("Typing Username")
    print("Typing Username")
    typeInt = driver.find_element("id", "j_username")
    typeInt.send_keys("https://www.sample_url_.com")
    print("Typing password")
    listwidget.addItem("Typing Password")
    typeInt = driver.find_element("id", "j_password")
    typeInt.send_keys("https://www.sample_url_.com")
    print("Waiting 20 Seconds to solve captha")
    listwidget.addItem("Waiting 20 Seconds to solve captcha")
    time.sleep(20)



# price collecting
def priceCollector(driver, sku_list, array_for_server, array_for_excel_sheet, listwidget):
    final_result = {}
    for sku, brand in sku_list:
            #adding sku to the json obj
            final_result["sku"] = sku
            # logged in to portal
            print("Reloading Page")
            # sampleText.insert(tk.INSERT, "Reloading Page \n")
            driver.get("https://www.sample_url_.com")
            # find search box
            findSku = driver.find_element("name", "text")
            findSku.send_keys(sku)

            try:
                
                # Wait for pop up suggetions
                print("Waiting for pop up suggetions...")
                # sampleText.insert(tk.INSERT, "Waiting for pop up suggetions... \n")
                wait = WebDriverWait(driver, 5)
                
                if wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ui-id-2"]/div[3]/strong[1]'))):             
                    # Retail Price
                    findPrices = driver.find_elements(By.XPATH, value='//*[@id="ui-id-2"]/div[3]/strong[1]')
                    for findPrice in findPrices:
                        # adding retail Price to json obj
                        costprice = findPrice.text.split("£")[1].replace(",", "")
                        final_result["costprice"] = float(costprice)                
                    # Selling Price
                    findRetailPrice = driver.find_elements(By.XPATH, value='//*[@id="ui-id-2"]/div[3]/strong[2]')
                    for findPrice in findRetailPrice:
                        # adding selling price json obj
                        sellingprice = findPrice.text.split("£")[1].replace(",", "")
                        final_result["sellingprice"] = float(sellingprice)
                    # addin latest prices to the json
                    array_for_server.append(final_result)
                    # clear final_result dec
                    
                    final_result = {}
                    # -----------------
                    # Clear search box
                    findSku.clear()       
                    listwidget.addItem("{} : PRICE COLLECTED".format(sku))        
                else:
                    print("Slow Internet Connection")
                    listwidget.addItem("Slow Connection...")
            except:
                
                array_for_excel_sheet.append([brand, sku, "Not Found"])
                listwidget.addItem("{} : Item Not Found".format(sku))
    driver.quit()