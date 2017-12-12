#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from RPI_configurator.RPI_configuratorapp import Rpi_configuratorApp


class TestRpi_configuratorApp(unittest.TestCase):
    """TestCase for Rpi_configuratorApp.
    """
    def setUp(self):
        self.app = Rpi_configuratorApp()

    def test_name(self):
        self.assertEqual(self.app.name, 'RPI_configurator')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
