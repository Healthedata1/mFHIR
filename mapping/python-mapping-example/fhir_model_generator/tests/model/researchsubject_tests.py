#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-02-10.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from model import researchsubject
from model.fhirdate import FHIRDate


class ResearchSubjectTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or \
                  os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'fhir-parser', 'downloads'))
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ResearchSubject", js["resourceType"])
        return researchsubject.ResearchSubject(js)

    def testResearchSubject1(self):
        inst = self.instantiate_from("researchsubject-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ResearchSubject instance")
        self.implResearchSubject1(inst)

        js = inst.as_json()
        self.assertEqual("ResearchSubject", js["resourceType"])
        inst2 = researchsubject.ResearchSubject(js)
        self.implResearchSubject1(inst2)

    def implResearchSubject1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://example.org/studysubjectids")
        self.assertEqual(inst.identifier[0].type.text, "Subject id")
        self.assertEqual(inst.identifier[0].value, "123")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "candidate")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")

if __name__ == '__main__':
    unittest.main()