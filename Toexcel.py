from openpyxl import Workbook
import datetime
import time


# saving result as xlxs
def saveToExcel(response, array_for_excel_sheet,listWidget):
    for item in response:
            itemresult = [item['brand'], item['sku'], item['status']]
            array_for_excel_sheet.append(itemresult) 

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H-%M") + '.xlsx'

    workbook = Workbook()
    worksheet = workbook.active



    for oneITem in array_for_excel_sheet:
        worksheet.append([oneITem[0], oneITem[1], oneITem[2]])
    
    # set column width
    worksheet.column_dimensions['A'].width = 15
    worksheet.column_dimensions['B'].width = 20
    worksheet.column_dimensions['C'].width = 10


    # save excel file named as current date and time (y-m-d h-m)
    workbook.save(current_time)
    listWidget.addItem("{}.xlxs saved on the current folder".format(current_time))
    time.sleep(2)