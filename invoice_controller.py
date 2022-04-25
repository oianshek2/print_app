import os
from docxtpl import DocxTemplate
from docx2pdf import convert


def generate(invoice_obj):
    dir_name = "invoice_docs"
    file_name = str(invoice_obj.id) + '_invoice.docx'
    file_path = os.path.join(dir_name, file_name)
    invoice_template = DocxTemplate("template/invoice_template.docx")

    context = {'id': invoice_obj.id,
               'invoceMonth': invoice_obj.invoiceYear,
               'invoiceYear': invoice_obj.invoiceYear,
               'trnBranch ': invoice_obj.trnBranch,
               'trnSalesPersonName': invoice_obj.trnSalesPersonName,
               'stockCode': invoice_obj.stockCode,
               'sumQty': invoice_obj.sumQty,
               'invMasterStockDescription': invoice_obj.invMasterStockDescription,
               'supplier': invoice_obj.supplier,
               'stockUom': invoice_obj.stockUom,
               'productStatus  ': invoice_obj.productStatus,
               'series': invoice_obj.series,
               'qtyOnHand': invoice_obj.qtyOnHand,
               'trnBranch ': invoice_obj.trnBranch,
               'trnBranch ': invoice_obj.trnBranch,
               }
    invoice_template.render(context)
    invoice_template.save(file_path)
    convert(file_path)
    file_name = str(invoice_obj.id) + '_invoice.pdf'
    file_path = os.path.join("\\invoice_docs", file_name)

    print(file_name)
    print(file_path)

    return file_path


