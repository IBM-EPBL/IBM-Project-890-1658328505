from cloudant.client import Cloudant
client = Cloudant.iam('9f458f39-44d8-46bd-bf8b-eb02c85f223c-bluemix',
                        '39FqLWsnZs_xCT-eEqB2Pim6rLghPbsDdd4h3wWcrwZo', connect=True)
my_database = client.create_database('my_db')