from PyQt5.QtSql import QSqlDatabase, QSqlQuery

from invoice_class import Invoice

SERVER_NAME = 'OIANSHEKPC'
DATABASE_NAME = 'pythonprint'
USERNAME = ''
PASSWORD = ''


def createConnection():
    connString = f'DRIVER={{SQL Server}};' \
                 f'SERVER={SERVER_NAME};' \
                 f'DATABASE={DATABASE_NAME}'

    global db
    db = QSqlDatabase.addDatabase('QODBC')
    db.setDatabaseName(connString)

    if db.open():
        print('connected')
        return True
    else:
        print("Not connected")
        return False


def displayData():
    if createConnection():
        items_list = []

        print('processing query')
        qry = QSqlQuery(db)
        sqlStatement = 'SELECT * FROM vw001ProductSalesByMonth'
        qry.prepare(sqlStatement)
        qry.exec()

        while qry.next():
            items_list.append(Invoice(
                qry.value('id'),
                qry.value('invoceMonth'),
                qry.value('invoiceYear'),
                qry.value('trnBranch'),
                qry.value('trnSalesPersonName'),
                qry.value('stockCode'),
                qry.value('sumQty'),
                qry.value('sumPrice'),
                qry.value('invMasterStockDescription'),
                qry.value('supplier'),
                qry.value('stockUom'),
                qry.value('productStatus'),
                qry.value('series'),
                qry.value('qtyOnHand'),
            ))

        return items_list


def get_one(id):
    if createConnection():
        qry = QSqlQuery(db)
        qry.prepare("SELECT * FROM vw001ProductSalesByMonth WHERE id = :id")
        qry.bindValue(":id", id)
        qry.exec()

        invoice = ''

        while qry.next():
            invoice = Invoice(
                qry.value('id'),
                qry.value('invoceMonth'),
                qry.value('invoiceYear'),
                qry.value('trnBranch'),
                qry.value('trnSalesPersonName'),
                qry.value('stockCode'),
                qry.value('sumQty'),
                qry.value('sumPrice'),
                qry.value('invMasterStockDescription'),
                qry.value('supplier'),
                qry.value('stockUom'),
                qry.value('productStatus'),
                qry.value('series'),
                qry.value('qtyOnHand'),
            )

        return invoice
