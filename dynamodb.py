import boto3

# Accedemos a la tabla la cual previamente
# Tenemos creada en AWS DynamoDB
DynamoDB = boto3.resource("dynamodb")
table = DynamoDB.Table("NombreTabla")

#  Colocar objeto en tabla
table.put_item(
    Item={
        "key1":"value1",
        "key2":"value2",
        "key3":"value3"
    }
)


# Get a item from a table
# Obtener un item de la tabla
response = table.get_item(
    key={
        "key":"value"
    }
)
# imprimir el valor obtenido
print(response["Item"])



## Creacion de clase tabla dynamodb ##
class MyDDB(object):
    def __init__(self, Table_name="DynamoDB"):
        self.Table_name = Table_name
        self.db = boto3.resource("dynamodb")
        self.table = self.db.Table(Table_name)
        self.client = boto3.client("dynamodb")

    @property
    def get(self,key=""):
        response = self.table.get_item(
            key={
                "key":key
            }
        )

    @property
    def put(self, key1='',key2='',key3=''):
        self.table.put_item(
            item={
                "key1":key1,
                "key2":key2,
                "key3":key3
            }
        )

    @property
    def delete(self,key=''):
        self.table.delete_item(
            key={
                "key":key
            }
        )

    def describe(self,TableName=''):
        response = self.client.describre_table(
            TableName=TableName
        )