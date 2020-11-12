BOT_NAME = 'finndata'

SPIDER_MODULES = ['finndata.spiders']
NEWSPIDER_MODULE = 'finndata.spiders'


# Database settings
CONNECTION_STRING = "{drivername}://{user}:{passwd}@{host}:{port}/{db_name}?charset=utf8".format(
    drivername="mysql+pymysql",
    user="root",
    passwd="toor",
    host="localhost",
    port="3306",
    db_name="finndata",
)

ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
   'finndata.pipelines.FinndataPipeline': 100,
    'finndata.pipelines.NewFinndataPipeline': 200,
    'finndata.pipelines.parkingPipeline': 300,
}

