#!/usr/bin/env python
# coding: utf-8

__author__ = "Jorge Niedbalski <jorge.niedbalski@canonical.com>"

from unittest import TestCase
from charmhelpers.contrib.python import version

import sys


class VersionTestCase(TestCase):

    def setUp(self):
        TestCase.setUp(self)

    def test_current_version(self):
        """
        Check if version.current_version and version.current_version_string
        works correctly
        """
        self.assertEquals(version.current_version(),
                          sys.version_info)
        self.assertEquals(version.current_version_string(),
                          "{0}.{1}.{2}".format(sys.version_info.major,
                                               sys.version_info.minor,
                                               sys.version_info.micro))
