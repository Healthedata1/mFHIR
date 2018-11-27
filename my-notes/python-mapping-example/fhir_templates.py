datapoint_variables = [
'observation_category_code',
'observation_category_display',
'observation_code_system',
'observation_code_code',
'observation_code_display',
'observation_value_quantity_value_path',
'observation_value_quantity_unit',
'observation_value_quantity_code',
'descriptive_statistic',
'descriptive_statistic_denominator',
'components'
]


omh_datatype_mapping = {
'acceleration': ('physical-activity', 'Physical Activity', 'http://loinc.org', '80493-0', 'Activity level [Acceleration]', None, None, False, False, []),
'ambient_temperature': ('None', 'None', 'http://loinc.org', '60832-3', 'Room temperature', None, None, False, False, []),
'blood_glucose': ('laboratory', 'Laboratory', 'http://loinc.org', '2339-0', 'Glucose Mass/volume in Blood', None, None, True, False, ['temporal_relationship_to_sleep', 'temporal_relationship_to_meal']),
'blood_pressure': ('vital-signs', 'Vital Signs', 'http://loinc.org', '85354-9', 'Blood pressure panel with all children optional', None, None, True, False, ['diastolic_blood_pressure', 'systolic_blood_pressure']),
'body_fat_percentage': ('exam', 'Exam', 'http://loinc.org', '41982-0', 'Percentage of body fat Measured', '%', '%', True, False, []),
'body_height': ('vital-signs', 'Vital Signs', 'http://loinc.org', '8302-2', 'Body height', 'cm', 'cm', False, False, []),
'body_mass_index': ('vital-signs', 'Vital Signs', 'http://loinc.org', '39156-5', 'Body mass index (BMI) Ratio', 'kg/m^2', 'kg/m2', True, False, []),
'body_temperature': ('vital-signs', 'Vital Signs', 'http://loinc.org', '8310-5', 'Body temperature', 'F', '[degF]', True, False, ['temporal_relationship_to_sleep']),
'body_weight': ('vital-signs', 'Vital Signs', 'http://loinc.org', '29463-7', 'Body weight', 'kg', 'kg', True, False, []),
'breath_carbon_monoxide': ('laboratory', 'Laboratory', 'http://snomed.info/id', '251900003', 'Expired carbon monoxide concentration (observable entity)', None, None, False, False, []),
'calories_burned': ('physical-activity', 'Physical Activity', 'http://loinc.org', '41981-2', 'Calories burned', None, None, False, False, []),
'diastolic_blood_pressure': ('vital-signs', 'Vital Signs', 'http://loinc.org', '8462-4', 'Diastolic blood pressure', 'mmHg', 'mm[Hg]', False, False, []),
'expiratory_time': ('exam', 'Exam', 'http://loinc.org', '60739-0', 'Expiration Time Respiratory system', None, None, False, False, []),
'geoposition': ('physical-activity', 'Physical Activity', 'http://www.fhir.org/guides/mfhir/datapoint-type', 'geoposition', 'Geoposition', None, None, False, False, []),
'heart_rate': ('vital-signs', 'Vital Signs', 'http://loinc.org', '8867-4', 'Heart rate', 'beats/min', '/min', True, False, ['temporal_relationship_to_physical_activity', 'temporal_relationship_to_sleep']),
'inspiratory_time': ('exam', 'Exam', 'http://loinc.org', '60740-8', 'Inspiration Time Respiratory system', None, None, False, False, []),
'magnetic_force': ('physical-activity', 'Physical Activity', 'http://www.fhir.org/guides/mfhir/datapoint-type', 'magnetic_force', 'Magnetic Force Panel', None, None, False, False, []),
'medication_adherence_percent': ('Survey', 'Survey', 'http://snomed.info/id', '418633004', 'Medication compliance (observable entity)', None, None, False, False, []),
'minute_volume': ('exam', 'Exam', 'http://loinc.org', '20139-2', 'Volume expired 1 minute', None, None, False, False, []),
'minutes_moderate_activity': ('physical-activity', 'Physical Activity', 'http://snomed.info/id', '408581006', 'Physical activity target moderate exercise (finding)', 'min', 'min', False, False, []),
'orientation': ('vital-signs', 'Vital Signs', 'http://www.fhir.org/guides/mfhir/datapoint-type', 'orientation', 'Gyroscope measurement Panel', None, None, False, False, []),
'oxygen_saturation': ('vital-signs', 'Vital Signs', 'http://loinc.org', '59408-5', 'Oxygen saturation in Arterial blood by Pulse oximetry', '%', '%', True, False, ['supplemental_oxygen_flow_rate', 'oxygen_therapy_mode_of_administration']),
'pace': ('physical-activity', 'Physical Activity', 'http://www.fhir.org/guides/mfhir/datapoint-type', 'pace', 'Pace', None, None, False, False, []),
'physical_activity': ('physical-activity', 'Physical Activity', 'http://snomed.info/id', '68130003', 'Physical activity (observable entity)', None, None, False, False, []),
'respiratory_rate': ('vital-signs', 'Vital Signs', 'http://loinc.org', '9279-1', 'Respiratory Rate', 'breaths/min', '/min', True, False, ['temporal_relationship_to_physical_activity']),
'rr_interval': ('exam', 'Exam', 'http://loinc.org', '8637-1', 'R_R interval by EKG', None, None, False, False, []),
'sleep_duration': ('physical-activity', 'Physical Activity', 'http://snomed.info/id', '248263006', 'Duration of sleep (observable entity)','h', 'h', True, True, []),
'sleep_episode': ('physical-activity', 'Physical Activity', 'http://snomed.info/id', '258158006', 'Sleep, function (observable entity)', None, None, False, False, []),
'speed': ('physical-activity', 'Physical Activity', 'http://ncimeta.nci.nih.gov', 'C0678536', 'Speed', None, None, False, False, []),
'step_count': ('physical-activity', 'Physical Activity', 'http://loinc.org', '55423-8', 'Number of steps in unspecified time Pedometer', 'steps', '{steps}', True, True, []),
'systolic_blood_pressure': ('vital-signs', 'Vital Signs', 'http://loinc.org', '8480-6', 'Systolic blood pressure', 'mmHg', 'mm[Hg]', False, False, []),
'ventilation_cycle_time': ('exam', 'Exam', 'http://snomed.info/id', '250818005', 'Ventilation cycle time (observable entity)', None, None, False, False, []),
}


omh_obs_templ='''{{
       "resourceType": "Observation",
       "id": "{server_assigned_resource_id}",  
       "meta": {{
       "profile" : ["http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_profile_quantitative_observation"]
     }},
     "extension" : [{{
         "url" : "{observation_specimen_code_extension_url}",
         "valueCodeableConcept": {{
         "coding": [
           {{
             "system": "{observation_specimen_code_system}",
             "code": "{observation_specimen_code_code}",
             "display": "{observation_specimen_code_display}"
           }}
         ],
         "text": "{observation_specimen_code_text}"
       }}
    }}],
       "identifier"  : [{{
       "system" : "https://omh.org/shimmer/ids",
       "value" : "{header.id}"
       }}],
       "status": "unknown", 
       "category": [  
         {{
           "coding": [
             {{
               "system": "http://hl7.org/fhir/observation-category",
               "code": "{observation_category_code}",
               "display": "{observation_category_display}"
             }}
           ]
         }}
       ],
       "code": {{ 
         "coding": [
           {{
             "system": "{observation_code_system}",
             "code": "{observation_code_code}",
             "display": "{observation_code_display}"
           }}
        ,{{
          "system" : "{addl_observation_coding_system}",
          "code" : "{addl_observation_coding_code}",
          "display" : "{addl_observation_coding_display}"
        }}
         ]
       }},
       "subject": {{
         "identifier" : {{
       "system" : "https://omh.org/shimmer/patient_ids",
       "value" : "{header.user_id}"
     }}
       }},
       "effectiveDateTime" : "{body.effective_time_frame.date_time}",
       "effectivePeriod" : {{
          "start" : "{body.effective_time_frame.time_interval.start_date_time}", 
          "end" : "{body.effective_time_frame.time_interval.end_date_time}"
          }}, 
       "issued": "{header.creation_date_time}",
       "valueQuantity" : {{
         "value" : {observation_value_quantity_value},
         "unit" : "{observation_value_quantity_unit}",
         "system" : "{observation_value_quantity_system}", 
         "code" : "{observation_value_quantity_code}"
        }},
        "comment" : "{body.user_notes}",
        "device" : {{
        "extension" : [{{
          "url" : "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
          "valueCode" : "{header.acquisition_provenance.modality}"
        }}],
        "display" : "{header.acquisition_provenance.source_name}"
        }},
        "component": [{observation_componentx}]
     }}'''
     
 
#************************************************
 
 
omh_denominator_value = {
'd': ('/day', '/d'),
'w': ('/week', '/wk'),
'm': ('/month', '/mo'),
'episode': ('/episode', '/{episode}'),
'session': ('/session', '/{session}')
}

#*********************************************


omh_component_mapping = {
'temporal_relationship_to_physical_activity':('http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes', 'relative-to-activity','OMH to FHIR Temporal Relationship To Physical Activity','valueCodeableConcept'),
'temporal_relationship_to_sleep':('http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes', 'relative-to-sleep','OMH to FHIR Temporal Relationship To Sleep','valueCodeableConcept'),
'temporal_relationship_to_meal':('http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes', 'relative-to-meal','OMH to FHIR Temporal Relationship To Meal','valueCodeableConcept'),
'body_posture':('http://snomed.info/sct', '271605009', 'Position of body and posture (observable entity)','valueCodeableConcept'),
'diastolic_blood_pressure':('http://loinc.org', '8462-4', 'Diastolic blood pressure','valueQuantity'),
'systolic_blood_pressure':('http://loinc.org', '8480-6', 'Systolic blood pressure','valueQuantity')
}

observation_componentx_template ='''{{
    "code" : {{
      "coding" : [{{
        "system" :"{observation_component_code_system}",
        "code" : "{observation_component_code_code}", 
        "display" : "{observation_component_code_display}"
         }}]
         }}, 
    "valueCodeableConcept" : {{ 
      "coding" : [{{
        "system" : "{observation_component_value_codeableconcept_system}", 
        "code" : "{observation_component_value_codeableconcept_code}", 
        "display" : "{observation_component_value_codeableconcept_display}"
        }}],
        "text" : "{observation_component_value_codeableconcept_text}"
        }},
       "valueQuantity" : {{
         "value" : {observation_component_value_quantity_value},
         "unit" : "{observation_component_value_quantity_unit}",
         "system" : "{observation_component_value_quantity_system}", 
         "code" : "{observation_component_value_quantity_code}"
        }}
     }}'''
     
     
#********************specimen_source mapping**************************     
observation_specimen_code = {
      "concept": [
        {
          "code": "258479004",
          "display": "interstitial fluid"
        },
        {
          "code": "122554006",
          "display": "capillary blood"
        },
        {
          "code": "119361006",
          "display": "plasma"
        },
        {
          "code": "119364003",
          "display": "serum"
        },
        {
          "code": "122594008",
          "display": "tears"
        },
        {
          "code": "258580003",
          "display": "whole blood"
        }
      ],
      "system": "http://snomed.info/sct"
    }
    
#****************concept mapping table******************
{'active': ('http://snomed.info/sct', '55561003', None),
 'after exercise': ('http://snomed.info/sct', '255214003', None),
 'at rest': ('http://snomed.info/sct', '263678003', None),
 'before exercise': ('http://snomed.info/sct', '307166007', None),
 'during exercise': ('http://snomed.info/sct', '309604004', None)}
     