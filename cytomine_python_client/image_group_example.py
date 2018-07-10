from os import listdir, path
from os.path import isfile, join
from cytomine.models import Project, AttachedFile, ImageGroupCollection, AttachedFileCollection
from cytomine import Cytomine
import logging


def attach_swc_file_to_image_group(folder_path,id_project,host,public_key,private_key):
    file_list = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]

    with Cytomine(host=host, public_key=public_key, private_key=private_key,
                  verbose=logging.INFO) as cyto_connection:
        print(cyto_connection.current_user)
        # ... Assume we are connected

        # Get the project from server.
        # The fetch() method makes the appropriate HTTP GET request.
        # See more on the github repository to see what is accessible: https://github.com/cytomine/Cytomine-python-client/tree/master/client/cytomine/models
        image_groups = ImageGroupCollection().fetch_with_filter("project", id_project)

        for image_group in image_groups:
            # For this group, the images have all been saved into .ome.tif so we remove this file extension
            base_image_group_name = image_group.name[:-8]
            # Attach SWC file only to the RAW image, so we skip the images having a _lbl suffix.
            if base_image_group_name[-4:] != '_lbl':
                print(base_image_group_name)
                # We loop through the directory containing the SWC file
                for file_path in file_list:
                    # If one SWC file basename match a .ome.tif file base name, we attach the SWC file to the image group
                    if path.basename(file_path)[:-4] == base_image_group_name:
                        print('Matching '+path.join(folder_path, file_path))
                        AttachedFile(
                            image_group,
                            filename=path.join(folder_path, file_path)
                        ).upload()


def download_attach_files_from_image_group(id_project, host, public_key, private_key, folder_path):
    with Cytomine(host=host, public_key=public_key, private_key=private_key,
                  verbose=logging.INFO) as cyto_connection:
        print(cyto_connection.current_user)
        # ... Assume we are connected
        image_groups = ImageGroupCollection().fetch_with_filter("project", id_project)
        for image_group in image_groups:
            attached_collection=AttachedFileCollection(image_group).fetch()
            if len(attached_collection)>0:
                print(image_group.name)
                for attached_file in attached_collection:
                    print(attached_file.filename)
                    attached_file.download(path.join(folder_path, attached_file.filename), True)



# host = # the host domain name, e.g. domain.name
# id_project= # project Id number available from http://domain.name/#tabs-dashboard-1852609 , e.g. here will be 1852609
# public_key = # the public key available at http://domain.name/#account
# private_key = # the private key available at http://domain.name/#account

#download_attach_files_from_image_group(id_project, host, public_key, private_key,'/tmp')
#attach_swc_file_to_image_group('/swc_file_to_attache_path/swc_files/', id_project, host, public_key, private_key)
