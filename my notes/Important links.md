Open mHealth-based mFHIR Implementation Guide.

NIH grant to increase adoption of Open mHealth by building the community, securing IEEE certification, and developing the mFHIR Implementation Guide.

## [Use Case Format](https://docs.google.com/document/d/13-rGGlmT2PFOS6gM9RhsAeWa_T9RmwmZa0IZL3mDLNQ/edit)


Summary of the call

Diagram attached – we will refine as the project develops. Send revisions to me.
Shimmer maps data from sensor clouds to Open mHealth schemas. Also handles authentication (currently OAuth based)
R24 server: offering Shimmer and computation as a service with mFHIR and OmH endpoints
not clear whether it needs a data store, but if we’re using it for at testbed, Mark, doesn’t it need one?
Will include basic computation (may be from open source Data Processing Units)
Provenance approach TBD from mProv project
API: needs definition, e.g., of supported commands, etc
why go through the R24 server? Normalizes data from diverse sensors into common Open mhealth schemas, with clean semantic representations and annotation to standard vocabs; ability to call and
mFHIR Implementation Guide: to include
use case(s), primarily around fetching data
define what operations are supported
mapping of OmH schemas used by those operations to FHIR Resources (conceptual and programmatic), defining FHIR extensions if needed
addressing authentication and security
specifying how to call operations, what data should look like, validation, etc
adding to SMART-on-FHIR launch parameters (don’t think I got all of this point)
build a demo FHIR app to illustrate use of the Implementation Guide, ie a reference implementation
Also assuming the IG contains narrative guidance surrounding the technical fhir artifacts, would my scope include drafting the narrative or would it be limited to the technical artifacts?

 But I looked at all the MHealth schemas

300 hrs @ $180/hr Assume:

70 total Schemas
40 are simple basic datatypes
30 more complex - ie observations and medications.

SCOPE OF Content

SCOPE OF WORK:

Creation of an Implementation Guide that contains detailed technical guidance and fhir artifacts needed to access Open mHealth data from an mHealth server:

The technical guidance scope includes:

1. Work Flow Description(s) for accessing Open mHealth data as FHIR resources from an mHealth FHIR endpoint.  
   - 10 Use case(s) as prioritized by Open mHealth team.
1. How to use the technical artifacts to implement a FHIR to Open mHealth interface.
1. Description of data element mappings between FHIR and the open MHealth schema.
1. Describe additional data computations for operations as needed.(e.g., averages, min, max) and a provenance approach and secure access approach. (leveraging the SMART on FHIR approach)
1. Creation of the following technical FHIR artifacts:
   - Profiles and Extensions (if needed)
   - ValueSets and ConceptMaps (if needed)
   - StructureMaps
   - Operations


Outline of activities:

1. Progress/Project Management
   1. Meetings
   1. Reports
1. Content Creation
   1. SME/Content/Design Meetings
   1. Authoring Narrative
    1. Data Element Mappings
    1. FHIR artifact Creation
1. Publishing
   1. Review
   1. Edit

 To Discuss:
 1. FHIR mapping languages based tooling to transform between mHealth and FHIR instances.
 1. Pilotings/Demonstration Projects/Connectathons/Demonstrations?

I estimate an average of 8-10 hrs/week through August.
for $200/hr not to exceed $40,000.
