# -*- coding: utf-8 -*-

# * Copyright (c) 2009-2018. Authors: see NOTICE file.
# *
# * Licensed under the Apache License, Version 2.0 (the "License");
# * you may not use this file except in compliance with the License.
# * You may obtain a copy of the License at
# *
# *      http://www.apache.org/licenses/LICENSE-2.0
# *
# * Unless required by applicable law or agreed to in writing, software
# * distributed under the License is distributed on an "AS IS" BASIS,
# * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# * See the License for the specific language governing permissions and
# * limitations under the License.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json

from cytomine import Cytomine
from cytomine.models import Project, TermCollection, ImageGroupCollection

__author__ = "Rubens Ulysse <urubens@uliege.be>"


def configure_project(id):
    # Update project configuration
    project = Project().fetch(id)
    project.blindMode = False
    project.retrievalDisable = True
    project.retrievalAllOntology = False
    project.isClosed = False
    project.isReadOnly = False
    project.isRestricted = True
    project.hideUsersLayers = False  # If user annotation not used: set to True
    project.hideAdminsLayers = False  # If user annotation not used: set to True
    project.update()

    # Update project UI configuration
    show_ontology = len(TermCollection().fetch_with_filter("project", project.id)) > 0
    n_image_groups = len(ImageGroupCollection().fetch_with_filter("project", project.id))
    show_image_group = n_image_groups > 0 or project.numberOfImages == 0
    show_image_instance = n_image_groups == 0
    configuration = {
        "project-images-tab": {
            "ADMIN_PROJECT": show_image_instance,
            "CONTRIBUTOR_PROJECT": show_image_instance
        },
        "project-imagegroups-tab": {
            "ADMIN_PROJECT": show_image_group,
            "CONTRIBUTOR_PROJECT": show_image_group
        },
        "project-annotations-tab": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": True
        },
        "project-properties-tab": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": True
        },
        "project-jobs-tab": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": True
        },
        "project-benchmark-tab": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": True
        },
        "project-usersconfiguration-tab": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-configuration-tab": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-explore-hide-tools": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": True
        },
        "project-explore-info": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": True
        },
        "project-explore-digital-zoom": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": True
        },
        "project-explore-link": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": True
        },
        "project-explore-filter": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": True
        },
        "project-explore-image-layers": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": True
        },
        "project-explore-ontology": {
            "ADMIN_PROJECT": show_ontology,
            "CONTRIBUTOR_PROJECT": show_ontology
        },
        "project-explore-annotation-panel": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": True
        },
        "project-explore-multidim": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": True
        },
        "project-explore-spectra-panel": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-explore-property": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": True
        },
        "project-explore-review": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-explore-follow": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-explore-job": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": True
        },
        "project-explore-overview": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": True
        },
        "project-explore-scaleline": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": True
        },
        "project-explore-annotation-main": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": True
        },
        "project-explore-annotation-info": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": True
        },
        "project-explore-annotation-preview": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": True
        },
        "project-explore-annotation-similarities": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-explore-annotation-comments": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-explore-annotation-properties": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": True
        },
        "project-explore-annotation-description": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": True
        },
        "project-tools-main": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": True
        },
        "project-tools-select": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": True
        },
        "project-tools-point": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-tools-line": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-tools-arrow": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-tools-rectangle": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-tools-diamond": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-tools-circle": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-tools-polygon": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-tools-magic": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-tools-freehand": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-tools-union": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-tools-diff": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-tools-fill": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-tools-edit": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-tools-resize": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-tools-move": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-tools-rotate": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-tools-delete": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-tools-rule": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": True
        },
        "project-tools-area": {
            "ADMIN_PROJECT": True,
            "CONTRIBUTOR_PROJECT": True
        },
        "project-tools-screenshot": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-annotations-term-piegraph": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-annotations-term-bargraph": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-annotations-users-graph": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-annotated-slides-term-graph": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-annotated-slides-users-graph": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-annotation-graph": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-users-global-activities-graph": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        },
        "project-users-heatmap-graph": {
            "ADMIN_PROJECT": False,
            "CONTRIBUTOR_PROJECT": False
        }
    }

    Cytomine.get_instance()._post("/custom-ui/project/{}.json".format(project.id),
                                  data=json.dumps(configuration), with_base_path=False)

    # Update list of project administrators
    # TODO

    # Update list of project contributors
    # TODO

    # Update project representative user
    # TODO


if __name__ == '__main__':
    host = ""
    public_key = ""
    private_key = ""

    id_project = 0

    with Cytomine(host, public_key, private_key) as c:
        c.open_admin_session()
        configure_project(id_project)
        c.close_admin_session()