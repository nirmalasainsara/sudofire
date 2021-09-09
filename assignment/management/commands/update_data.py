import xlrd
from django.core.management.base import BaseCommand
from assignment.models import Product


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        file_path = 'my_file.xls'
        wb = xlrd.open_workbook(file_path)
        wb_sheet = wb.sheet_by_index(0)
        total_product = wb_sheet.nrows

        for row in range(1, total_product):
            product_name = wb_sheet.cell(row, 0).value
            product_price = wb_sheet.cell(row, 1).value
            if product_name and product_price:
                Product.objects.filter(product_name=product_name).update(product_price=product_price)

        