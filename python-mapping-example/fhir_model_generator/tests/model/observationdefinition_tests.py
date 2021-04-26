#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-02-10.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from model import observationdefinition
from model.fhirdate import FHIRDate


class ObservationDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or \
                  os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'fhir-parser', 'downloads'))
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ObservationDefinition", js["resourceType"])
        return observationdefinition.ObservationDefinition(js)

    def testObservationDefinition1(self):
        inst = self.instantiate_from("observationdefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ObservationDefinition instance")
        self.implObservationDefinition1(inst)

        js = inst.as_json()
        self.assertEqual("ObservationDefinition", js["resourceType"])
        inst2 = observationdefinition.ObservationDefinition(js)
        self.implObservationDefinition1(inst2)

    def implObservationDefinition1(self, inst):
        self.assertEqual(inst.code.coding[0].code, "15074-8")
        self.assertEqual(inst.code.coding[0].display, "Glucose [Moles/volume] in Blood")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status, "generated")

if __name__ == '__main__':
    unittest.main()