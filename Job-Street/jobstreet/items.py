# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class JobstreetItem(scrapy.Item):
    ID= scrapy.Field(
        output_processor = TakeFirst()
    )
    Date= scrapy.Field(
        output_processor = TakeFirst()
    )
    Location= scrapy.Field(
        output_processor = TakeFirst()
    )
    Career_Level= scrapy.Field(
        output_processor = TakeFirst()
    )
    Work_Experience= scrapy.Field(
        output_processor = TakeFirst()
    )
    Job_Specialization_1= scrapy.Field(
        output_processor = TakeFirst()
    )
    Job_Specialization_2= scrapy.Field(
        output_processor = TakeFirst()
    )
    Employment_Type= scrapy.Field(
        output_processor = TakeFirst()
    )
    Salary_Min= scrapy.Field(
        output_processor = TakeFirst()
    )
    Salary_Max= scrapy.Field(
        output_processor = TakeFirst()
    )

    Company_Name = scrapy.Field(
        output_processor=TakeFirst()
    )
    Qualifications = scrapy.Field(
        output_processor=TakeFirst()
    )

