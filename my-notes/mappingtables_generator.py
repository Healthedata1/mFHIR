from pprint import pprint

D1 = {'OmhStepCount':'OMH Step Count Schema',
'omhHeader':'see OmhHeader Mapping tables',
'stepCount':'properties.step_count',
'effectiveTimeFrame':'properties.effective_time_frame',
'descriptiveStatistic':'properties.descriptive_statistic',
'descriptiveStatisticDenominator':'properties.descriptive_statistic_denominator'}

D2 ={'OmhStepCount':'Observation resource with Observation.code = LOINC 55423-8 (Number of steps in unspecified time Pedometer)',
'omhHeader':'see OmhHeader Mapping tables',
'stepCount':'Rule1: IF no descriptiveStatistic (descriptiveStatistic.empty()) Observation.valueQuantity.value ELSE Observation.component.valueQuantity.value',
'effectiveTimeFrame':'Observation.effectivePeriod',
'descriptiveStatistic':'Observation.component.code',
'descriptiveStatisticDenominator':'Observation.component.valueQuantity.unit|code (ConceptMap based on code and descriptiveStatisticDenominator)',
}

print('**OMH to FHIR Observation Resource mappings **')
print('|OMH element|FHIR element|')
print('|---|---|')
for k in D1:
    print('|{}|{}|'.format(D1[k],D2[k]))




