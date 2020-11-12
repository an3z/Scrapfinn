from scrapy import Item, Field
from datetime import datetime
from scrapy.loader.processors import MapCompose, TakeFirst

def convert_date(text):
    # convert string March 14, 2017 to Python date
    return datetime.strptime(text, '%B %d, %Y')

def convert_year(text):
    return datetime.strptime(text,'%Y')


class FinnItems(Item):
    finn_code = Field(output_processor=TakeFirst())
    address = Field(output_processor=TakeFirst())
    total_price = Field(output_processor=TakeFirst())
    common_costs = Field(output_processor=TakeFirst())
    for_sale_price = Field(output_processor=TakeFirst())
    ownership_form = Field(output_processor=TakeFirst())
    building_type = Field(output_processor=TakeFirst())
    bedrooms = Field(output_processor=TakeFirst())
    pra = Field(output_processor=TakeFirst())
    year_built = Field(input_processor=MapCompose(convert_year),output_processor=TakeFirst())
    last_changed = Field(input_processor=MapCompose(convert_date), output_processor=TakeFirst())
    rooms = Field(output_processor=TakeFirst())


class NewFinnItems(Item):
    finn_code = Field(output_processor=TakeFirst())
    address = Field(output_processor=TakeFirst())
    total_price = Field(output_processor=TakeFirst())
    common_costs = Field(output_processor=TakeFirst())
    for_sale_price = Field(output_processor=TakeFirst())
    ownership_form = Field(output_processor=TakeFirst())
    building_type = Field(output_processor=TakeFirst())
    bedrooms = Field(output_processor=TakeFirst())
    pra = Field(output_processor=TakeFirst())
    year_built = Field(input_processor=MapCompose(convert_year),output_processor=TakeFirst())
    last_changed = Field(input_processor=MapCompose(convert_date), output_processor=TakeFirst())
    rooms = Field(output_processor=TakeFirst())


class ParkingItems(Item):
    finn_code = Field(output_processor=TakeFirst())
    title = Field(output_processor=TakeFirst())
    headline = Field(output_processor=TakeFirst())
    address = Field(output_processor=TakeFirst())
    price = Field(output_processor=TakeFirst())