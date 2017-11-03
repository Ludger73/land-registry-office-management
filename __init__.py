# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LandRegistryOfficeManagement
                                 A QGIS plugin
 This plugin supports the management of land registry offices
                             -------------------
        begin                : 2017-11-03
        copyright            : (C) 2017 by Ludger
        email                : lusonntag@web.de
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LandRegistryOfficeManagement class from file LandRegistryOfficeManagement.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .land_registry_office_management import LandRegistryOfficeManagement
    return LandRegistryOfficeManagement(iface)
