from cytomine import Cytomine
from cytomine.models import ImageGroup
from cytomine.models import ImageGroupCollection
from cytomine.models import ImageInstance
from cytomine.models import ImageInstanceCollection
from cytomine.models import Project
from cytomine.models import ProjectCollection

host = "neubias.cytomine.be"
public_key = "97a0ab52-d787-400c-a5e1-1da0ef81530f" # check your own keys from your account page in the web interface
private_key = "ae95bcd1-5c2c-44ff-9d27-96ca8eb4681a"

project_id = 3002905

cytomine = Cytomine.connect(host, public_key, private_key)

print("Hello {}".format(cytomine.current_user.username))

groups = ImageGroupCollection().fetch_with_filter("project", project_id)

for group in groups:
    print(group)
    group.delete()

#idem for ImageInstanceCollection

#images = ImageInstanceCollection().fetch_with_filter("project", project_id)

#for image in images:
    #print(image)
#    image.delete()

