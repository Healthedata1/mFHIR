#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-02-10.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from model import medicinalproductinteraction
from model.fhirdate import FHIRDate


class MedicinalProductInteractionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or \
                  os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'fhir-parser', 'downloads'))
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductInteraction", js["resourceType"])
        return medicinalproductinteraction.MedicinalProductInteraction(js)

    def testMedicinalProductInteraction1(self):
        inst = self.instantiate_from("medicinalproductinteraction-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicinalProductInteraction instance")
        self.implMedicinalProductInteraction1(inst)

        js = inst.as_json()
        self.assertEqual("MedicinalProductInteraction", js["resourceType"])
        inst2 = medicinalproductinteraction.MedicinalProductInteraction(js)
        self.implMedicinalProductInteraction1(inst2)

    def implMedicinalProductInteraction1(self, inst):
        self.assertEqual(inst.effect.coding[0].code, "Increasedplasmaconcentrations")
        self.assertEqual(inst.effect.coding[0].system, "http://ema.europa.eu/example/interactionseffect")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.interactant[0].itemCodeableConcept.coding[0].code, "ketoconazole")
        self.assertEqual(inst.interactant[0].itemCodeableConcept.coding[0].system, "http://ema.europa.eu/example/interactant")
        self.assertEqual(inst.interactant[1].itemCodeableConcept.coding[0].code, "itraconazole")
        self.assertEqual(inst.interactant[1].itemCodeableConcept.coding[0].system, "http://ema.europa.eu/example/interactant")
        self.assertEqual(inst.management.text, "Coadministration not recommended in patients receiving concomitant systemic treatment strong inhibitors of both CYP3A4 and P-gp")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "StrongInhibitorofCYP3A4")
        self.assertEqual(inst.type.coding[0].system, "http://ema.europa.eu/example/interactionsType")

if __name__ == '__main__':
    unittest.main()