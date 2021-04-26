#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-02-10.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from model import biologicallyderivedproduct
from model.fhirdate import FHIRDate


class BiologicallyDerivedProductTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or \
                  os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'fhir-parser', 'downloads'))
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("BiologicallyDerivedProduct", js["resourceType"])
        return biologicallyderivedproduct.BiologicallyDerivedProduct(js)

    def testBiologicallyDerivedProduct1(self):
        inst = self.instantiate_from("biologicallyderivedproduct-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a BiologicallyDerivedProduct instance")
        self.implBiologicallyDerivedProduct1(inst)

        js = inst.as_json()
        self.assertEqual("BiologicallyDerivedProduct", js["resourceType"])
        inst2 = biologicallyderivedproduct.BiologicallyDerivedProduct(js)
        self.implBiologicallyDerivedProduct1(inst2)

    def implBiologicallyDerivedProduct1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")

if __name__ == '__main__':
    unittest.main()