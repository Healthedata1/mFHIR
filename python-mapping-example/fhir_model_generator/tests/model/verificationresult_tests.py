#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-02-10.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from model import verificationresult
from model.fhirdate import FHIRDate


class VerificationResultTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or \
                  os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'fhir-parser', 'downloads'))
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("VerificationResult", js["resourceType"])
        return verificationresult.VerificationResult(js)

    def testVerificationResult1(self):
        inst = self.instantiate_from("verificationresult-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a VerificationResult instance")
        self.implVerificationResult1(inst)

        js = inst.as_json()
        self.assertEqual("VerificationResult", js["resourceType"])
        inst2 = verificationresult.VerificationResult(js)
        self.implVerificationResult1(inst2)

    def implVerificationResult1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "attested")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: example</p><p><b>status</b>: attested</p></div>")
        self.assertEqual(inst.text.status, "generated")

if __name__ == '__main__':
    unittest.main()