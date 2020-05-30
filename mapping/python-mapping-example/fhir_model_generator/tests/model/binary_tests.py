#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-02-10.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from model import binary
from model.fhirdate import FHIRDate


class BinaryTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or \
                  os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'fhir-parser', 'downloads'))
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Binary", js["resourceType"])
        return binary.Binary(js)

    def testBinary1(self):
        inst = self.instantiate_from("binary-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Binary instance")
        self.implBinary1(inst)

        js = inst.as_json()
        self.assertEqual("Binary", js["resourceType"])
        inst2 = binary.Binary(js)
        self.implBinary1(inst2)

    def implBinary1(self, inst):
        self.assertEqual(inst.contentType, "application/pdf")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")

if __name__ == '__main__':
    unittest.main()