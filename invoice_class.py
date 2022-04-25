class Invoice:

    def __init__(
            self,
            id,
            invoceMonth,
            invoiceYear,
            trnBranch,
            trnSalesPersonName,
            stockCode,
            sumQty,
            sumPrice,
            invMasterStockDescription,
            supplier,
            stockUom,
            productStatus,
            series,
            qtyOnHand
    ):
        self.id = id
        self.invoceMonth = invoceMonth
        self.invoiceYear = invoiceYear
        self.trnBranch = trnBranch
        self.trnSalesPersonName = trnSalesPersonName
        self.stockCode = stockCode
        self.sumQty = sumQty
        self.sumPrice = sumPrice
        self.invMasterStockDescription = invMasterStockDescription
        self.supplier = supplier
        self.stockUom = stockUom
        self.productStatus = productStatus
        self.series = series
        self.qtyOnHand = qtyOnHand