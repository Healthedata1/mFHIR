   DRAFT
   PUNCH LIST:

   - Mapping and example for

      1. blood glucose - done
      1. blood pressure [add property cuff position]
      1. body temperature  - done
      1. body weight
      1. heart rate [resting] - done
      1. O2 saturation
      1. respiratory rate
      1. sleep duration [--  total sleep time ]
      1. step count [change datatype of property step_count to unit_value]

   - add linke to the concept mapping
   - add links:
      1. spreadsheets
      1. terminology
      1. concept Mapping
      1. FHIR profiles
      1. sample code
   - validate examples to FHIR R4
   -  source documentation is all in markdown - consider other documentation toolilng like makedocs or Jekyll for better formatting


   Just a few points from my quick review

   1. In the section OMH DataPoint Element to FHIR Element Mapping Table
   in the table there is an * next to BP: not sure why; also while the BP schema itself does not include units, it references two schemas that do: not sure where that would go but should be documented

   update sheets first

   2. In the section OMH Header to FHIR Observation Detailed Mapping  
   in the table columns Derived mapping and Comments there are URLs I am not sure I understand
   Is "omh.org" a reference to a page on the Open mHealth website?  those are fixed system values. (which should not change)  todo fix the rendering so not a link and make clearer. see example.  uses uuid RFC4122 urn:ietf:rfc:3986  urn:uuid:  

   update sheets and example generator..  done for header - update rest.

   3. Is it necessary to display a device for each type of data? If so, we should use valid values, since Jawbone Up was a fitness tracker only.. used in examples only and stubbed in each example.  - Acme Brand for each
   Questions:

   update sample generator...  also make the order match the fhir resources

   Json schemas updated to Draft 7  across the board  used to be draft 4.

   udpated versions is there a list of changes? - see email.

   For each schema, when you go to the relevant page on the Open mHealth website, you see the most recent version (also displayed at the top of the page) and sample data at the bottom. Use the menu button to the right of "Sample Data" to see additional sample instances:

1. blood glucose: made effective_time_frame required
1. blood pressure: added property measurement_location (for cuff position) and relationship to physical activity, made effective_time_frame required, removed property user_notes  
1. body temperature: made effective_time_frame required
1. body weight: made effective_time_frame required
1. heart rate [resting]: made effective_time_frame required, removed property user_notes
1. Oxygen saturation: made effective_time_frame required
1. respiratory rate: made effective_time_frame required
1. sleep duration: please use schema total sleep time https://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_total-sleep-time
1. step count: changed datatype of property step_count to unit_value

As usual, please let me know if you have any questions.

   units now a list of enums can only list one in FHIR and made a mapping.  Yes let consumer decide.

   link to the github page on OMH site?

   Step Count / sleep. big changes


map schema source in meta source - or Provenance -

see http://build.fhir.org/provenance.html#import

 see how v2 - FHIR doing it. pinged Hans

General (transformation) Provenance - done and applied

Every transformation of a v2 message likely warrants the inclusion of a general Provenance resource that records the details of the transformation.

General Provenance resource relating to the transformation process:
Provenance.target points to all resources in the bundle
Provenance.recorded indicates the instant the v2 message was transformed to FHIR resources
Provenance.policy may point to the rules used for the transformation
Provenance.agent.type = "assembler"
Provenance.agent.who references the Organization or Device performing the transformation
Provenance.entity can optionally contain the whole v2 message as a Binary or DocumentReference in .what and a .role of "derivation" (or maybe "source"?)


Also contain the Provenance in the observation.
